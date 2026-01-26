# 🏎️ CARLA Telemetry Dashboard

A real-time telemetry dashboard for CARLA Simulator 0.9.10 with battery monitoring and vehicle diagnostics.

![Python](https://img.shields.io/badge/Python-3.7.9-blue)
![CARLA](https://img.shields.io/badge/CARLA-0.9.10-orange)
![Platform](https://img.shields.io/badge/Platform-Windows-lightgrey)

---

## 📋 Table of Contents

1. [What You Need](https://claude.ai/chat/215aac55-89b6-4a5a-9ae0-97d9c276990c#-what-you-need)
2. [Step-by-Step Installation](https://claude.ai/chat/215aac55-89b6-4a5a-9ae0-97d9c276990c#-step-by-step-installation)
3. [Setting Up the Project](https://claude.ai/chat/215aac55-89b6-4a5a-9ae0-97d9c276990c#-setting-up-the-project)
4. [How to Run](https://claude.ai/chat/215aac55-89b6-4a5a-9ae0-97d9c276990c#-how-to-run)
5. [Understanding the Dashboard](https://claude.ai/chat/215aac55-89b6-4a5a-9ae0-97d9c276990c#-understanding-the-dashboard)
6. [Common Problems &amp; Solutions](https://claude.ai/chat/215aac55-89b6-4a5a-9ae0-97d9c276990c#-common-problems--solutions)

---

## 🛠️ What You Need

Before starting, you need to install these programs on your Windows PC:

### 1. Python 3.7.9 (64-bit)

> ⚠️  **IMPORTANT** : You MUST use Python 3.7.9. Newer versions will NOT work with CARLA 0.9.10!

 **Download Link** : [Python 3.7.9 Windows installer (64-bit)](https://www.python.org/ftp/python/3.7.9/python-3.7.9-amd64.exe)

 **Installation Steps** :

1. Download the installer
2. Run the installer
3. ✅ **CHECK the box** that says "Add Python 3.7 to PATH"
4. Click "Install Now"
5. Wait for installation to complete

 **Verify Installation** :

```bash
# Open Command Prompt and type:
py -3.7 --version

# You should see:
# Python 3.7.9
```

### 2. Visual C++ Redistributable

 **Download Link** : [VC++ 2015-2019 (x64)](https://aka.ms/vs/16/release/vc_redist.x64.exe)

 **Installation Steps** :

1. Download and run the installer
2. Accept the license agreement
3. Click "Install"
4. Restart your computer if prompted

### 3. DirectX End-User Runtime

 **Download Link** : [DirectX Runtime](https://www.microsoft.com/en-us/download/details.aspx?id=35)

 **Installation Steps** :

1. Download the installer
2. Run it and follow the on-screen instructions
3. Click "Yes" to accept the agreement
4. Click "Next" and let it install

### 4. CARLA Simulator 0.9.10

 **Download Link** : [CARLA 0.9.10 Windows](https://github.com/carla-simulator/carla/releases/download/0.9.10/CARLA_0.9.10.zip)

 **Installation Steps** :

1. Download the ZIP file (approximately 5GB)
2. Extract the ZIP file to a location you'll remember
   * Example: `D:\WindowsNoEditor`
   * Or: `C:\CARLA\WindowsNoEditor`
3. Remember this path - you'll need it later!

 **System Requirements** :

* **GPU** : NVIDIA GTX 1070 or better (8GB VRAM minimum)
* **RAM** : 16GB minimum
* **Storage** : 20GB free space
* **OS** : Windows 10 or Windows 11 (64-bit)

---

## 📥 Step-by-Step Installation

### Step 1: Download This Project

**Option A: Download ZIP**

1. Click the green "Code" button at the top of this page
2. Click "Download ZIP"
3. Extract the ZIP to a folder (e.g., `C:\Users\YourName\Desktop\carla-dashboard`)

**Option B: Using Git**

```bash
git clone https://github.com/yourusername/carla-telemetry-dashboard.git
cd carla-telemetry-dashboard
```

### Step 2: Install Python Packages

1. Open **Command Prompt** (press `Win + R`, type `cmd`, press Enter)
2. Navigate to the project's backend folder:
   ```bash
   cd C:\Users\YourName\Desktop\carla-dashboard\backend
   ```
3. Install the required packages:
   ```bash
   py -3.7 -m pip install -r requirements.txt
   ```
4. Wait for installation to complete. You should see:
   ```
   Successfully installed numpy-1.21.6 pygame-2.6.1 python-dotenv-0.21.1 eventlet-0.33.3 python-socketio-5.8.0
   ```

---

## ⚙️ Setting Up the Project

### Creating the .env Configuration File

The `.env` file tells the program where CARLA is installed on your computer.

1. **Open the `backend` folder** in your project
2. **Create a new file** called `.env` (exactly this name, no `.txt` extension)
   * In Windows: Right-click → New → Text Document
   * Rename it from `New Text Document.txt` to `.env`
   * If you can't see file extensions, enable them in File Explorer
3. **Open `.env` with Notepad** and copy-paste this template:

```ini
# ============================
# CARLA PATH CONFIGURATION
# ============================
CARLA_ROOT=D:\WindowsNoEditor
CARLA_EXE=D:\WindowsNoEditor\CarlaUE4.exe
CARLA_EGG=carla-0.9.10-py3.7-win-amd64.egg

# ============================
# CARLA LAUNCH SETTINGS
# ============================
CARLA_RES_X=256
CARLA_RES_Y=144
CARLA_QUALITY=Low
CARLA_NO_SOUND=true
CARLA_START_DELAY=20

# ============================
# PYTHON SETTINGS
# ============================
PYTHON_EXEC=py
PYTHON_VERSION=-3.7

# ============================
# SOCKET.IO SERVER SETTINGS
# ============================
SOCKET_HOST=127.0.0.1
SOCKET_PORT=8000

# ============================
# TELEMETRY SETTINGS
# ============================
SOC_START=100.0
SOC_DRAIN_FACTOR=0.05
SHUTDOWN_ON_SOC_ZERO=true

# ============================
# AGENT SETTINGS
# ============================
CARLA_AGENT=Roaming
CARLA_RESOLUTION=256x144
```

4. **Update the paths** to match YOUR CARLA installation:
   **Find your CARLA path** :

   * Where did you extract CARLA?
   * Example: If you extracted to `D:\WindowsNoEditor`, use that
   * Example: If you extracted to `C:\CARLA\WindowsNoEditor`, use that

   **Change these three lines** :

   ```ini
   CARLA_ROOT=YOUR_PATH_HERE
   CARLA_EXE=YOUR_PATH_HERE\CarlaUE4.exe
   ```

   **Example for D: drive** :

   ```ini
   CARLA_ROOT=D:\WindowsNoEditor
   CARLA_EXE=D:\WindowsNoEditor\CarlaUE4.exe
   ```

   **Example for C: drive** :

   ```ini
   CARLA_ROOT=C:\CARLA\WindowsNoEditor
   CARLA_EXE=C:\CARLA\WindowsNoEditor\CarlaUE4.exe
   ```
5. **Save the file** (Ctrl + S)

### Understanding the Settings

Here's what each setting means:

| Setting               | What It Does                      | Change This?                                      |
| --------------------- | --------------------------------- | ------------------------------------------------- |
| `CARLA_ROOT`        | Where CARLA is installed          | ✅ YES - Use your path                            |
| `CARLA_EXE`         | CARLA executable location         | ✅ YES - Use your path                            |
| `CARLA_EGG`         | Python API file name              | ❌ NO - Keep as is                                |
| `CARLA_RES_X`       | Window width in pixels            | 🔧 Optional - Lower for better performance        |
| `CARLA_RES_Y`       | Window height in pixels           | 🔧 Optional - Lower for better performance        |
| `CARLA_QUALITY`     | Graphics quality                  | 🔧 Optional -`Low`,`Medium`,`High`,`Epic` |
| `CARLA_NO_SOUND`    | Disable audio                     | 🔧 Optional -`true`or `false`                 |
| `CARLA_START_DELAY` | Seconds to wait for CARLA to load | 🔧 Increase if CARLA loads slowly                 |
| `SOCKET_PORT`       | Communication port                | ❌ NO - Keep as 8000                              |
| `SOC_START`         | Starting battery percentage       | 🔧 Optional - 0 to 100                            |
| `SOC_DRAIN_FACTOR`  | How fast battery drains           | 🔧 Optional - Higher = faster drain               |
| `CARLA_AGENT`       | Autopilot type                    | 🔧 Optional -`Roaming`,`Basic`,`Behavior`   |

 **Performance Tips** :

* If CARLA runs slowly, use: `CARLA_RES_X=128` and `CARLA_RES_Y=72`
* If CARLA takes long to load, increase: `CARLA_START_DELAY=30`

---

## 🚀 How to Run

### Quick Start (3 Simple Steps)

1. **Open Command Prompt**

   * Press `Win + R`
   * Type `cmd`
   * Press Enter
2. **Navigate to the backend folder**

   ```bash
   cd C:\Users\YourName\Desktop\carla-dashboard\backend
   ```

   (Replace with your actual path)
3. **Run the launcher**

   ```bash
   py -3.7 start.py
   ```

### What Happens Next

The program will automatically:

 **⏱️ Step 1 (2 seconds)** : Clean up old CARLA processes

```
Cleaning old CARLA processes...
```

 **⏱️ Step 2 (3 seconds)** : Start CARLA Simulator

```
Launching CARLA Simulator...
```

* A CARLA window will open

 **⏱️ Step 3 (20 seconds)** : Wait for CARLA to load

```
Waiting 20 seconds for CARLA to load...
```

* Watch the CARLA window - it's loading the city

 **⏱️ Step 4 (3 seconds)** : Start the telemetry bridge

```
Launching Bridge...
```

* A new window will show connection status

 **⏱️ Step 5 (1 second)** : Open dashboard in browser

```
Opening Dashboard: C:\...\frontend\index.html
```

* Your web browser will open automatically
* You should see the dashboard with live data!

### Success Indicators

✅  **Everything is working if you see** :

* CARLA window showing a city with a car
* Browser showing the dashboard
* Green "Connected" status in the dashboard
* Numbers updating in real-time

❌  **Something is wrong if** :

* CARLA window closes immediately
* Dashboard shows "Disconnected" (red)
* No car appears in CARLA
* Numbers don't update

---

## 📊 Understanding the Dashboard

### Dashboard Layout

```
┌────────────────────────────────────────────────┐
│  CARLA TELEMETRY          🟢 Connected         │
├──────────────┬──────────────────┬──────────────┤
│              │                  │              │
│  Battery     │   Speedometer    │    Gear      │
│    87%       │     45 km/h      │     3        │
│              │                  │              │
│  Controls    │                  │   Status     │
│  Throttle    │                  │   DRIVING    │
│  Brake       │                  │              │
│  Steering    │                  │              │
│              │                  │              │
├──────────────┴──────────────────┴──────────────┤
│  ⚡ Throttle: 75%  │  🛑 Brake: 0%  │ 🎯 Steer: -15° │
└────────────────────────────────────────────────┘
```

### What Each Part Means

#### 🟢 Connection Status (Top Right)

* **Green dot** : Connected - receiving live data
* **Red dot** : Disconnected - check if bridge is running

#### 🔋 Battery (Left Panel)

* Shows battery percentage (0-100%)
* Color changes:
  * Green: Above 50%
  * Yellow: 20-50%
  * Red: Below 20%
* Drains based on speed and throttle
* When it hits 0%, CARLA will shut down

#### ⚡ Speedometer (Center)

* Large circular gauge
* Shows speed in km/h
* Maximum display: 200 km/h
* Blue gradient fills as speed increases

#### 🎮 Controls (Left Panel)

* **Throttle** : How much gas pedal is pressed (0.00 to 1.00)
* **Brake** : How much brake pedal is pressed (0.00 to 1.00)
* **Steering** : Left/Right steering (-1.00 to +1.00)

#### ⚙️ Gear (Right Panel)

* **N** : Neutral (not moving)
* **R** : Reverse
* **1-6** : Forward gears

#### 📍 Status (Right Panel)

* **IDLE** : Car is stopped, no throttle
* **READY** : Engine on, waiting to move
* **DRIVING** : Car is moving

#### 📊 Footer Info Cards

* Quick reference for throttle, brake, and steering
* Shows percentages and angles

---

## 🔧 Common Problems & Solutions

### Problem 1: "Python 3.7 not found"

 **Error Message** :

```
'py' is not recognized as an internal or external command
```

 **Solution** :

1. Reinstall Python 3.7.9
2. Make sure you check "Add Python to PATH" during installation
3. Restart Command Prompt
4. Try again

 **Test if it worked** :

```bash
py -3.7 --version
# Should show: Python 3.7.9
```

---

### Problem 2: CARLA Window Closes Immediately

 **Symptoms** : CARLA opens then crashes

 **Solutions** :

 **A) Check GPU drivers** :

1. Press `Win + R`
2. Type `dxdiag`
3. Go to "Display" tab
4. Update your graphics drivers

 **B) Increase startup delay** :

1. Open `.env` file
2. Change: `CARLA_START_DELAY=30` (or even 40)
3. Save and try again

 **C) Test CARLA manually** :

1. Go to your CARLA folder (e.g., `D:\WindowsNoEditor`)
2. Double-click `CarlaUE4.exe`
3. If it crashes here too, reinstall CARLA

---

### Problem 3: Dashboard Shows "Disconnected"

 **Symptoms** : Red dot, no data updating

 **Check these in order** :

 **Step 1** : Is the bridge running?

* Look for a second Command Prompt window
* It should show: `>>> Socket.IO server running on http://127.0.0.1:8000`
* If you don't see this window, restart `start.py`

 **Step 2** : Is CARLA fully loaded?

* Look at the CARLA window
* Do you see a city with buildings?
* Do you see a car driving around?
* If not, wait 30 more seconds

 **Step 3** : Check browser console

1. In the dashboard, press `F12`
2. Click "Console" tab
3. Look for errors
4. Common error: "Failed to connect to http://127.0.0.1:8000"
   * This means bridge isn't running - restart it

 **Step 4** : Firewall blocking?

1. Press `Win + R`
2. Type `firewall.cpl`
3. Click "Allow an app through Windows Firewall"
4. Find Python and check both boxes
5. Try again

---

### Problem 4: No Car Appears in CARLA

 **Symptoms** : CARLA shows empty city

 **Solutions** :

 **Wait longer** :

* CARLA can take 30-60 seconds to spawn the car
* Watch for console message: `>>> Bridge Online: CARLA hooked`

 **Manual car spawn** :

1. Open new Command Prompt
2. Navigate to CARLA examples:
   ```bash
   cd D:\WindowsNoEditor\PythonAPI\examples
   ```
3. Spawn a car:
   ```bash
   py -3.7 spawn_npc.py -n 1
   ```

---

### Problem 5: Battery Drains Too Fast

 **Symptoms** : Battery hits 0% in less than 2 minutes

 **Solution** :

1. Open `.env` file
2. Find: `SOC_DRAIN_FACTOR=0.05`
3. Change to: `SOC_DRAIN_FACTOR=0.01` (slower drain)
4. Save file
5. Restart `start.py`

 **Drain Speed Guide** :

* `0.01` = Very slow (30+ minutes)
* `0.05` = Normal (10 minutes)
* `0.1` = Fast (5 minutes)
* `0.2` = Very fast (2 minutes)

---

### Problem 6: "ImportError: No module named 'carla'"

 **Error Message** :

```
ModuleNotFoundError: No module named 'carla'
```

 **Solution** :

 **Check your `.env` paths** :

1. Open `.env` file
2. Verify these lines match your CARLA location:
   ```ini
   CARLA_ROOT=D:\WindowsNoEditorCARLA_EGG=carla-0.9.10-py3.7-win-amd64.egg
   ```

 **Verify the egg file exists** :

1. Open File Explorer
2. Go to: `D:\WindowsNoEditor\PythonAPI\carla\dist\`
3. Look for: `carla-0.9.10-py3.7-win-amd64.egg`
4. If it's not there, re-download CARLA 0.9.10

---

### Problem 7: Port 8000 Already in Use

 **Error Message** :

```
OSError: [Errno 10048] Only one usage of each socket address
```

 **Solution A** : Change the port

1. Open `.env`
2. Change: `SOCKET_PORT=8080`
3. Open `frontend/index.html` in Notepad
4. Find: `io("http://127.0.0.1:8000"`
5. Change to: `io("http://127.0.0.1:8080"`
6. Save both files
7. Restart

 **Solution B** : Find what's using port 8000

```bash
netstat -ano | findstr :8000
taskkill /PID [number_shown] /F
```

---

### Problem 8: Slow Performance / Lag

 **Symptoms** : Low FPS, stuttering

 **Solutions** :

**1. Lower CARLA resolution** (`.env`):

```ini
CARLA_RES_X=128
CARLA_RES_Y=72
```

 **2. Set CARLA to high priority** :

1. Open Task Manager (Ctrl + Shift + Esc)
2. Find "CarlaUE4.exe"
3. Right-click → Set Priority → High

 **3. Close other programs** :

* Close Chrome/Firefox tabs
* Close Discord, Steam, etc.

 **4. Make sure laptop is plugged in** :

* Windows reduces GPU power on battery

---

---
