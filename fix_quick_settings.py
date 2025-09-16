#!/usr/bin/env python3
import subprocess
import sys
import ctypes

def is_admin() -> bool:
    try:
        return ctypes.windll.shell32.IsUserAnAdmin()
    except Exception:
        return False

def elevate():
    # Relaunch the script with admin rights
    params = " ".join([f'"{arg}"' for arg in sys.argv])
    ctypes.windll.shell32.ShellExecuteW(None, "runas", sys.executable, params, None, 1)

def main():
    if not is_admin():
        print("Administrator privileges required. Requesting elevation...")
        elevate()
        sys.exit(0)

    print("Restarting Windows Explorer to fix Quick Settings...")
    # Kill explorer.exe
    subprocess.run(["taskkill", "/F", "/IM", "explorer.exe"], check=False)
    # Restart explorer.exe
    subprocess.Popen(["explorer.exe"])
    print("Done.")

if __name__ == "__main__":
    main()
