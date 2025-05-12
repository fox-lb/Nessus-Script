@echo off
echo ===== Start at %date% %time% ===== >> C:\Users\Lenovo\Downloads\nessus.log
python "C:\Users\Lenovo\Downloads\Nessus\update_nessus_plugin.py" >> C:\Users\Lenovo\Downloads\nessus.log
echo ===== End at %date% %time% ===== >> C:\Users\Lenovo\Downloads\nessus.log
