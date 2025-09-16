#!/usr/bin/env python3
import subprocess
import sys
import ctypes
import shutil

def is_admin() -> bool:
    try:
        return ctypes.windll.shell32.IsUserAnAdmin()
    except Exception:
        return False

def elevate():
    params = " ".join([f'"{arg}"' for arg in sys.argv])
    ctypes.windll.shell32.ShellExecuteW(None, "runas", sys.executable, params, None, 1)

def run_powershell(ps_script: str):
    # Use PowerShell to access PnP cmdlets
    pwsh = shutil.which("powershell") or shutil.which("pwsh")
    if pwsh is None:
        raise RuntimeError("PowerShell not found on PATH.")
    cmd = [pwsh, "-NoProfile", "-ExecutionPolicy", "Bypass", "-Command", ps_script]
    return subprocess.run(cmd, capture_output=True, text=True)

def main():
    if not is_admin():
        print("Administrator privileges required. Requesting elevation...")
        elevate()
        sys.exit(0)

    print("Resetting Bluetooth devices (disable/remove) and rescanning...")
    ps = r'''
    $ErrorActionPreference = "Stop"
    $bt = Get-PnpDevice -Class Bluetooth -Status OK
    foreach ($d in $bt) {
        try {
            Disable-PnpDevice -InstanceId $d.InstanceId -Confirm:$false -ErrorAction SilentlyContinue
        } catch {}
        try {
            Remove-PnpDevice -InstanceId $d.InstanceId -Confirm:$false -ErrorAction SilentlyContinue
        } catch {}
    }
    Start-Sleep -Seconds 3
    & pnputil.exe /scan-devices
    '''
    result = run_powershell(ps)
    if result.returncode != 0:
        print("PowerShell error:\n", result.stderr.strip())
    else:
        if result.stdout.strip():
            print(result.stdout.strip())
        print("Bluetooth devices have been reset. Please reconnect your device if necessary.")

if __name__ == "__main__":
    main()
