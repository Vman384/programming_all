@echo off
mode 1000
color 0a
title vedansh's game
echo 1} start
echo 2} intro
echo 3} exit
set /p menu=

if %menu%==1 goto game
if %menu%==2 goto help
if %menu%==3 exit

:help
echo hit the correct answer and press enter.
pause
echo 1} start
echo 2} intro
echo 3} exit
set /p menu=

if %menu%==1 goto game
if %menu%==2 goto help
if %menu%==3 exit

:game
echo what is your name
set /p name=
echo %name%! start game?
pause
cls
echo who was the first president of the usa
echo 1} Geogre Washington
echo 2} Abraham Lincon
set /p ab=

if %ab%==1 goto cr1
if %ab%==2 goto wr1

:cr1
echo corect
pause
goto q2

:wr1
echo wrong
pause
q2

:q2
echo who was the first man in space
echo 1} Yuri Garin
echo 2} Neil Armstrong
set /p ab=

if %ab%==1 goto cr2
if %ab%==2 goto wr2

:cr2
echo correct good job
pause
cls
goto q3

:wr2
echo wrong keep trying
pause
cls
goto q3

:q3
echo who's the founder of microsoft
echo 1} Steve Jobs
echo 2} Bill Gates
set /p ab=

if %ab%==1 goto wr3
if %ab%==2 goto cr3

:wr3
echo wrong it's ok
pause 
cls
goto q4

:cr3
echo correct your good at this game
pause
cls
goto q4

:q4
echo what's 9+10
echo 1} 19
echo 2} 21
set /p ab=

if %ab%==1 goto cr4
if %ab%==2 goto wr4

:cr4
echo correct good job that was an easy one
pause
cls
goto q5

:wr4
echo wrong you'r very stupid

:q5
echo what contenent is Zimbawe
echo 1} Africa
echo 2} Ociana
set /p ab=

if %ab%==1 goto cr5
if %ab%==2 goto wr5

:cr5
echo correct and thaks for playing here's cool thing to show you
pause
:a
echo %random%%random%%random%%random%%random%%random%%random%%random%%random%%random%%random%%random%%random%%random%%random%%random%%random%%random%%random%%random%%random%%random%%random%%random%%random%%random%%random%%random%%random%%random%%random%%random%%random%%random%%random%%random%%random%%random%%random%
goto a

:wr5
echo wrong but thanks for playing here's cool thing to show you
pause
:a
echo %random%%random%%random%%random%%random%%random%%random%%random%%random%%random%%random%%random%%random%%random%%random%%random%%random%%random%%random%%random%%random%%random%%random%%random%%random%%random%%random%%random%%random%%random%%random%%random%%random%%random%%random%%random%%random%%random%%random%
goto a