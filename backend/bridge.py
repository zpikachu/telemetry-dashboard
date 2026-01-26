import sys
import os
import math
import socketio
import eventlet
import time
import threading
from dotenv import load_dotenv

# ==============================
# LOAD ENV
# ==============================
load_dotenv()

CARLA_ROOT = os.getenv("CARLA_ROOT")
CARLA_EGG = os.getenv("CARLA_EGG")

SOCKET_HOST = os.getenv("SOCKET_HOST", "127.0.0.1")
SOCKET_PORT = int(os.getenv("SOCKET_PORT", 8000))

SOC_START = float(os.getenv("SOC_START", 100))
SOC_DRAIN_FACTOR = float(os.getenv("SOC_DRAIN_FACTOR", 0.05))
SHUTDOWN_ON_SOC_ZERO = os.getenv("SHUTDOWN_ON_SOC_ZERO", "true").lower() == "true"

# ==============================
# CARLA PATH SETUP
# ==============================
sys.path.append(os.path.join(CARLA_ROOT, f"PythonAPI/carla/dist/{CARLA_EGG}"))
sys.path.append(os.path.join(CARLA_ROOT, "PythonAPI/carla"))
EXAMPLES_PATH = os.path.join(CARLA_ROOT, "PythonAPI/examples")
sys.path.append(EXAMPLES_PATH)

import automatic_control as ac

# ==============================
# SOCKET.IO SERVER
# ==============================
sio = socketio.Server(cors_allowed_origins='*', async_mode='eventlet')
app = socketio.WSGIApp(sio)

latest_payload = None
running = True

# 🔋 Virtual Battery SoC
soc = SOC_START

@sio.event
def connect(sid, environ):
    print(f"Client connected: {sid}")

def shutdown_system():
    print("🔴 Force shutting down CARLA + Python + Socket")

    global running
    running = False

    try:
        import pygame
        pygame.quit()
        print("Pygame closed")
    except:
        pass

    os._exit(0)

# ==============================
# TELEMETRY SPY
# ==============================
class TelemetrySpy:
    def on_tick(self, snapshot):
        global latest_payload, soc, running

        try:
            if not hasattr(ac, "world") or ac.world is None:
                return

            vehicle = ac.world.player
            if vehicle is None or not vehicle.is_alive:
                return

            v = vehicle.get_velocity()
            c = vehicle.get_control()

            speed = 3.6 * math.sqrt(v.x**2 + v.y**2 + v.z**2)

            # ⚡ SoC drain
            drain = (c.throttle * speed * SOC_DRAIN_FACTOR)
            soc -= drain
            soc = max(0.0, soc)

            latest_payload = {
                "speed": round(speed, 1),
                "throttle": round(c.throttle, 2),
                "brake": round(c.brake, 2),
                "steer": round(c.steer, 2),
                "gear": c.gear,
                "soc": round(soc, 2)
            }

            if soc <= 0 and SHUTDOWN_ON_SOC_ZERO:
                print("🔋 Battery empty! Stopping vehicle...")
                vehicle.apply_control(ac.carla.VehicleControl(throttle=0, brake=1.0))
                shutdown_system()

        except Exception as e:
            print("Telemetry error:", e)

# ==============================
# SOCKET PUSH LOOP
# ==============================
def telemetry_pusher():
    global latest_payload, running
    while running:
        sio.sleep(0.05)
        if latest_payload:
            sio.emit("telemetry", latest_payload)

# ==============================
# HOOK CARLA
# ==============================
def hook_into_carla():
    spy = TelemetrySpy()
    while not hasattr(ac, "world") and running:
        print("Waiting for CARLA world...")
        time.sleep(1)

    if hasattr(ac, "world"):
        ac.world.world.on_tick(spy.on_tick)
        print(">>> Bridge Online: CARLA hooked")

# ==============================
# START CARLA IN REAL THREAD
# ==============================
def start_carla():
    global running
    try:
        os.chdir(EXAMPLES_PATH)
        ac.main()
    except:
        pass
    finally:
        print(">>> CARLA closed. Shutting down bridge...")
        running = False
        time.sleep(1)
        os._exit(0)

# ==============================
# MAIN
# ==============================
if __name__ == "__main__":
    sio.start_background_task(telemetry_pusher)
    sio.start_background_task(hook_into_carla)

    threading.Thread(target=start_carla, daemon=True).start()

    print(f">>> Socket.IO server running on http://{SOCKET_HOST}:{SOCKET_PORT}")
    eventlet.wsgi.server(eventlet.listen((SOCKET_HOST, SOCKET_PORT)), app)
