import subprocess
import time
import os
import webbrowser
from dotenv import load_dotenv

load_dotenv()

def open_dashboard():
    frontend_path = os.path.abspath(
        os.path.join(os.path.dirname(__file__), "../frontend/index.html")
    )
    print("🌐 Opening Dashboard:", frontend_path)
    webbrowser.open(frontend_path)

def kill_old_carla():
    print("Cleaning old CARLA processes...")
    subprocess.call("taskkill /IM CarlaUE4.exe /F /T", shell=True)
    subprocess.call("taskkill /IM UE4Editor.exe /F /T", shell=True)

def main():
    kill_old_carla()

    CARLA_ROOT = os.getenv("CARLA_ROOT")
    CARLA_EXE = os.getenv("CARLA_EXE")

    RES_X = os.getenv("CARLA_RES_X", "256")
    RES_Y = os.getenv("CARLA_RES_Y", "144")
    QUALITY = os.getenv("CARLA_QUALITY", "Low")
    NO_SOUND = os.getenv("CARLA_NO_SOUND", "true").lower() == "true"
    START_DELAY = int(os.getenv("CARLA_START_DELAY", 20))

    PYTHON_EXEC = os.getenv("PYTHON_EXEC", "py")
    PYTHON_VERSION = os.getenv("PYTHON_VERSION", "-3.7")

    AGENT = os.getenv("CARLA_AGENT", "Roaming")
    RES = os.getenv("CARLA_RESOLUTION", "256x144")

    if not CARLA_EXE or not os.path.exists(CARLA_EXE):
        print("❌ CARLA_EXE not found. Check .env path.")
        return

    print("Launching CARLA Simulator...")
    carla_cmd = [
        CARLA_EXE,
        "-windowed",
        f"-ResX={RES_X}",
        f"-ResY={RES_Y}",
        f"-quality-level={QUALITY}"
    ]

    if NO_SOUND:
        carla_cmd.append("-nosound")

    subprocess.Popen(carla_cmd)

    print(f"Waiting {START_DELAY} seconds for CARLA to load...")
    time.sleep(START_DELAY)

    print("Launching Bridge...")
    subprocess.Popen([
        PYTHON_EXEC,
        PYTHON_VERSION,
        "bridge.py",
        "--agent", AGENT,
        "--res", RES
    ])

    time.sleep(3)
    open_dashboard()

if __name__ == "__main__":
    main()
