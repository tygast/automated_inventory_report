call C:\Users\User1\anaconda3\scripts\activate tracker
pushd %userprofile%\projects\automated_inventory_report\src\controllers
call python run_report.py
call conda deactivate
popd