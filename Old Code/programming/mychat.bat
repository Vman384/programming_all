@echo off
echo hello
pause
echo what is your name? %name%
set /p name=
pause

cls
echo what is your faviourte subject %name%? %subject%
set /p subject=
pause
echo really i never had thought you'd like %subject% but i prefer science
pause

cls
echo i have a question for you
pause 
echo whats 9+10
echo a21 b19
pause
set /p choice=
if %choice%==a21 GOTO a
if %choice%==a GOTO a
if %choice%==b GOTO b
if %choice%==b19 GOTO b
pause
cls

:b
pause
echo you are correct and not stupid
echo and thats it c'ya
pause
exit

:a
pause
echo you are incorrect and very stupid
echo you should go back to kindagartin so i better go
pause
exit