try:
    total_students = 0
    grade_A_count = 0

    with open("students.txt", "r") as file:
        next(file)  # skip header line: Name, Age, Grade
        for line in file:
            line = line.strip()  # remove newline
            if not line:
                continue  # skip empty lines
            total_students += 1
            # Check if grade is 'A'
            if line.endswith("A"):
                grade_A_count += 1

    print("Total students:", total_students)
    print("Number of students with grade A:", grade_A_count)

except FileNotFoundError:
    print("File does not exist.")