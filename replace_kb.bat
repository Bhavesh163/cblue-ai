@echo off
python -c "import shutil; shutil.copy(r'C:\cblue-ai\common\knowledge_base.py', r'C:\cblue-ai\common\knowledge_base_backup.py'); print('Backup created'); shutil.copy(r'C:\cblue-ai\common\knowledge_base_new.py', r'C:\cblue-ai\common\knowledge_base.py'); print('Replacement complete')"
