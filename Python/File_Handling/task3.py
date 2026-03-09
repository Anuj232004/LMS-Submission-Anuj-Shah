try:
    with open("students.txt","a") as file:
        file.write("Emma,20,B\n")
        file.write("Liam,23,A")
        print("Appeded Data Successfully")
except FileNotFoundError:
    print("File does not exist")