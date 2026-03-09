import os

try:
    os.remove("students_backup.txt")
    print("File deleted successfully.")

except:
    print("File does not exist")

