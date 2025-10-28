import shutil
import os

# Backup the old file
shutil.copy('C:\\cblue-ai\\common\\knowledge_base.py', 'C:\\cblue-ai\\common\\knowledge_base_backup.py')
print("Backup created: knowledge_base_backup.py")

# Replace with new file
shutil.move('C:\\cblue-ai\\common\\knowledge_base_new.py', 'C:\\cblue-ai\\common\\knowledge_base.py')
print("File replacement completed successfully!")
print("The knowledge base has been updated with your new Q&A content.")
