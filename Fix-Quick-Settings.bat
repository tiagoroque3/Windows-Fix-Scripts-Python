@echo off
echo Restarting Windows Explorer to fix Quick Settings...
taskkill /f /im explorer.exe
start explorer.exe
echo Done.
pause
