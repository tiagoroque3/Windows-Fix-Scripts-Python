@echo off
:: Check for Administrator privileges
net session >nul 2>&1
if %errorlevel% neq 0 (
    echo This script requires administrator privileges. Restarting as administrator...
    powershell -Command "Start-Process '%~f0' -Verb RunAs"
    exit /b
)

:: Uninstall and rescan Bluetooth devices
powershell -Command "& { 
    Get-PnpDevice -Class Bluetooth -Status OK | ForEach-Object {
        Disable-PnpDevice -InstanceId $_.InstanceId -Confirm:$false
        Remove-PnpDevice -InstanceId $_.InstanceId -Confirm:$false
    }
    Start-Sleep -Seconds 3
    & 'pnputil.exe' /scan-devices
}"

echo Bluetooth devices have been reset. Please reconnect your device if necessary.
pause
