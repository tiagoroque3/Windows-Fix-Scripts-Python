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
    params = " ".join([f'"{arg}"' for arg in sys.argv])
    ctypes.windll.shell32.ShellExecuteW(None, "runas", sys.executable, params, None, 1)

def net_cmd(args):
    return subprocess.run(["net"] + args, capture_output=True, text=True)

def main():
    if not is_admin():
        print("Administrator privileges required. Requesting elevation...")
        elevate()
        sys.exit(0)

    print("Restarting Windows Audio Services...")
    # Stop services (audiosrv depends on AudioEndpointBuilder, so stop audiosrv first)
    net_cmd(["stop", "audiosrv"])
    net_cmd(["stop", "AudioEndpointBuilder"])

    # Start services in dependency order
    net_cmd(["start", "AudioEndpointBuilder"])
    net_cmd(["start", "audiosrv"])

    print("Audio services restarted successfully.")

if __name__ == "__main__":
    main()
