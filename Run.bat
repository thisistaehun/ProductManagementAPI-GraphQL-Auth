@echo off

:: Activate Python Environment
call %USERPROFILE%\anaconda3\condabin\conda.bat activate owner_venv
IF %ERRORLEVEL% NEQ 0 (
    echo Failed to activate environment.
    pause
    exit /b
)

:: Run Script
call python ./src/main.py
IF %ERRORLEVEL% NEQ 0 (
    echo Failed to run script.
    pause
    exit /b
)

pause
