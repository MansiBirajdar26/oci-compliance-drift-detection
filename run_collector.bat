@echo off
cd C:\Users\mansi\oci-compliance-drift
call .venv\Scripts\activate
python collector/collect_config.py
echo Done >> data/collection_log.txt