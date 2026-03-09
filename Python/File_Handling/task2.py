# Read the file and display content
try:
    with open("students.txt", "r") as file:
        # Read entire content
        content = file.read()
        print("Full content:\n", content)

        # Move pointer back to start to read line by line
        file.seek(0)
       
        #Read line by line 
        print("\nPrinting line by line:")
        for line in file:
            print(line.strip())  
except FileNotFoundError:
      print("File does not exist.")