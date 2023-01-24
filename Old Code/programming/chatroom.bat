@echo off

title Login
color a
cls
echo Please Register.
echo.
set /p User=Username:
set /p Pass=Password:
cls
:A
echo Your Account %user has been created.
echo.
pause
cls
echo Please Login.
echo.
set /p u=Username:
set /p p=Password:
if %u%==%user% if %p%==%pass% goto B
cls
echo Invalid username or Password.
echo.
pause
cls
goto A

:B
echo You are now logged in as %user%
echo.
Pause
cls
