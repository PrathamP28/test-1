@echo off
set appname=main
set path="C:\Program Files\MyPythonTrayApp\main.exe"
reg add "HKCU\Software\Microsoft\Windows\CurrentVersion\Run" /v %appname% /t REG_SZ /d %path% /f
echo [%appname%] added to startup with path: %path%
pause
