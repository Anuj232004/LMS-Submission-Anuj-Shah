try:
    with open("students_backup.txt","a") as backup:
        with open ("students.txt","r") as file:
            for line in file:
              backup.write(line)
except FileNotFoundError:
    print("File does not exist")