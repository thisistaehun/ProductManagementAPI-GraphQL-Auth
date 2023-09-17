@echo off

:: Create Python Environment
call conda create -n owner_venv python=3.11 -y

:: Activate Python Environment
call conda activate owner_venv

:: Install Packages
call pip install -r ./requirements.txt

:: Success Message
echo.
echo ------------------------------------
echo Environment Name: owner_venv 
echo Installation completed successfully!
echo ------------------------------------
echo.
