# Trainer Details and Verification
users = {
    "trainer1": "Train@123",
    "trainer2": "Learn@123"
}
print("Login System")

for attempt in range(3):
    username = input("Enter your username: ")
    password = input("Enter your password: ")
    
    
    if username in users and users[username] == password:
        print(f"Welcome {username}!")
        break
    else:
        print("Invalid username or password. Try again.")
else:
    print("Access Denied. Please contact admin.")



# Trainee Data and Validation
Trainee_count = 0
Details = {}
subject = {1: 'Python', 2: 'Data_Structure', 3: 'Control_Flows'}

Trainee_count= int(input('Enter number of trainees'))
while Trainee_count>0:
    name = input("Enter trainee name: ")
    marks = []
    for j in subject:
        while True:  # keep asking until a valid number is entered
            try:
                mark = int(input(f"Enter marks for {subject[j]}: "))
                if mark < 0 or mark > 100:
                    raise ValueError("Marks must be between 0 and 100")
                marks.append(mark)
                break  # exit the loop if input is valid
            except ValueError as e:
                print(f"Invalid input: {e}. Please enter again.")
    Details[name] = marks
    Trainee_count -=1

print("\nAll trainee details:")
print(Details)




#Performance Evaluation:
Stats = {}  # dictionary to store total and average

for name, marks in Details.items():  # iterate over each trainee
    total_marks = sum(marks)
    average_marks = total_marks / len(marks)
    Stats[name] = {
        'Total': total_marks,
        'Average': average_marks
    }

print("Stats per trainee:")
for trainee, stat in Stats.items():
    print(f"{trainee}: Total = {stat['Total']}, Average = {stat['Average']:.2f}")


# Grade Classification
for name in Stats:
    avg = Stats[name]['Average']
    
    if avg >= 85:
        grade = "Excellent"
    elif avg >= 70:
        grade = "Good"
    elif avg >= 50:
        grade = "Average"
    else:
        grade = "Needs Improvement"
    
    Stats[name]['Grade'] = grade


print("\nUpdated Stats with Grades:")
for trainee, stat in Stats.items():
    print(f"{trainee}: Total = {stat['Total']}, Average = {stat['Average']:.2f}, Grade = {stat['Grade']}")


# Analytics & Reporting
highest_name = None
highest_avg = None

lowest_name = None
lowest_avg = None

grade_count = {
    "Excellent": 0,
    "Good": 0,
    "Average": 0,
    "Needs Improvement": 0
}

failed_any_subject = []

for name in Details:
    avg = Stats[name]['Average']
    grade = Stats[name]['Grade']
    marks = Details[name]

    if highest_avg is None or avg > highest_avg:
        highest_avg = avg
        highest_name = name

    if lowest_avg is None or avg < lowest_avg:
        lowest_avg = avg
        lowest_name = name

    grade_count[grade] += 1

    for m in marks:
        if m < 40:
            failed_any_subject.append(name)
            break


print("\nAnalytics Report")
print("Highest Average Scorer:", highest_name, "-", highest_avg)
print("Lowest Average Scorer:", lowest_name, "-", lowest_avg)

print("\nCount of Trainees per Grade:")
for g in grade_count:
    print(g, ":", grade_count[g])

print("\nTrainees who failed any subject:")
for f in failed_any_subject:
    print(f)


# Trainer Decision Module
choice = input("\nDo you want to schedule remedial training? (yes/no): ")

if choice.lower() == "yes":
    print("Trainees needing remedial training:")
    for f in failed_any_subject:
        print(f)
else:
    print("Report finalized successfully")
