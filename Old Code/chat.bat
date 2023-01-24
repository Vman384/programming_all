@echo off
title chatbox
color 0a
echo hello you are talking to your computer!
echo what is your name? %name%
set /p name=
echo hello %name%
pause

cls
echo what is your favviourte food?%food%
set /p food=
echo i like %food% too.
pause

cls
echo do you play any sports? yes or no
set /p choice=
if %choice%==yes GOTO :yes
if %choice%==yes GOTO :yes
if %choice%==no GOTO :no
if %choice%==no GOTO :no
pause

:yes
echo what sport/s do you play? %sport%
set /p sport=
echo i also play %sport%
pause
GOTO :School

:no
cls
pause
echo oh, that's ok sports aren't for everybody
pause
GOTO :School

:School
cls
echo do you get good grades in school? yes or no
set /p choice2=
if %choice2%==yes goto :done
if %choice2%==yes goto :done
if %choice2%==no goto :ok
if %choice2%==no goto :ok 

:done
:ok
cls
echo oh that is great. keep up the good work
pause
echo thats it for now c'ya
pause
exit