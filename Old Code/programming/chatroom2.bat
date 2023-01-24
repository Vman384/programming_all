@echo off
:home
color 0b
title vedanshs chat room
cls
echo     chat logon
echo ____________________
echo 1. logon
echo 2. create an account
echo 3. exit
echo _____________________
set /p ch=choice number:
if %ch%==1 goto logon
if %ch%==2 goto account
if %ch%==3 exit
color 0c
echo please enter a valid  number.
ping localhost -n 2 >nul
goto home

:logon
cls
set /p un=Username:
echo ______________________
set /p pass=Password:
if NOT Exist "\\SHRIGANESH\Users\Public\chat\users\%un%.unfile" goto not
echo %pass% > "%tmp%\chtmp.tmp"  
fc  %tmp%\chtmp.tmp "\\SHRIGANESH\Us\Public\chat\users\%un%.unfile" \nul 
if errorlevel==1 goto incor
cls
goto chat
pause




:account
cls
color 0b
set /p nu=New Username:
echo _______________________
set /p np=New Password:
echo %np% > "\\SHRIGANESH\Users\Public\chat\\%nu%.unfile"
cls
goto logon

:not
cls
color 0b
echo this username does not exist please make an account
ping localhost -n 4  >nul
goto home

:icor
cls
echo you have entered the wrong username or password. (both are case sensitive)
ping localhost -n 2 >nul
goto home

:chat
start \\SHRIGANESH\Users\Public\chat\program_files\msgbox.bat
:chat1
set %com%=efwheretrnhgeds
set name=%un%
set /p com=Com:
goto ifs
goto chat1
cls
color 0b




:exit
cls
echo %name% has left the chatroom. >>\\SHRIGANESH\Users\Public\chat\program_files\msgbox
taskkill /im cmd.exe
exit

:clear
cls
echo _________chatroom__________
echo >>\\SHRIGANESH\Users\Public\chat\program_files\msgbox
goto chat1

:ifs
if %com%==exit goto exit
if %com%==cls goto cls
goto echo
goto chat1

:echo
echo %name% : %text% >>\\SHRIGANESH\Users\Public\chat\program_files\msgbox
ping localhost -n 1 >nul