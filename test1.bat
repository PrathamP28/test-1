@echo off
:: Change these values to your app details
set AppName=MyPythonTrayApp
set AppPath="C:\Program Files\MyPythonTrayApp\main.exe"

:: Add registry key for startup
reg add "HKCU\Software\Microsoft\Windows\CurrentVersion\Run" /v %AppName% /t REG_SZ /d %AppPath% /f

echo [%AppName%] added to startup with path: %AppPath%
pause
