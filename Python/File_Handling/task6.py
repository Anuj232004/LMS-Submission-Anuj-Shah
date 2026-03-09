'''with open("numbers.txt","a+") as file:
    for i in range(1001):
        file.write(str(i)+"\n")'''

try:
   
   total = 0
   with open("numbers.txt", "r") as file:
        for line in file:
                total += int(line)  # convert string to int and sum
        print("The sum is:", total)

except FileNotFoundError:
    print("File does not exist")