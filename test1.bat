@echo off
set AppName=MyPythonTrayApp

:: Remove registry key
reg delete "HKCU\Software\Microsoft\Windows\CurrentVersion\Run" /v %AppName% /f

echo [%AppName%] removed from startup
pause
