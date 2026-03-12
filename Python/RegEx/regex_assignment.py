import re
import json
from collections import defaultdict

#TASK1

with open('data_log.txt', 'r') as file:
    logs = file.read()

ip_pattern = r'\b(?:\d{1,3}\.){3}\d{1,3}\b'

all_ips = re.findall(ip_pattern, logs)

unique_ips = sorted(set(all_ips))

print("Unique IP addresses in sorted order:")
for ip in unique_ips:
    print(ip)


#TASK2
with open('data_log.txt', 'r') as f:
    logs = f.readlines()

user_actions = {}

for line in logs:
    if 'INFO' in line:
       
        match = re.search(r'User (\w+) (.+)', line)
        if match:
            username = match.group(1)
            action = match.group(2).strip()
            #
            user_actions.setdefault(username, set()).add(action)


for user in user_actions:
    user_actions[user] = list(user_actions[user])


for user, actions in user_actions.items():
    print(f"{user}: {actions}")



#TASK3
with open('data_log.txt', 'r') as f:
    logs = f.readlines()

emails = set()  

for line in logs:
    matches = re.findall(r'[\w]+@[\w]+\.\w{2,6}', line)
    for email in matches:
        emails.add(email)


print("Email addresses found in the log:")
for email in emails:
    print(email)



#TASK4
with open('data_log.txt', 'r') as f:
    logs = f.readlines()

numbers = set() 

for line in logs:
    matches = re.findall(r'\b\d{3}-\d{3}-\d{4}\b', line)
    for num in matches:
        numbers.add(num)

print(numbers)



#TASK5
with open('data_log.txt', 'r') as f:
    logs = f.readlines()

urls = set() 

for line in logs:
    matches = re.findall(r'https?://[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}', line)
    for url in matches:
        urls.add(url)

print(urls)


#TASK6

with open('data_log.txt', 'r') as f:
    logs = f.readlines()


levels_count = defaultdict(int)


pattern = r'\b(INFO|WARNING|ERROR|CRITICAL)\b'

for line in logs:
    match = re.search(pattern, line)
    if match:
        level = match.group()  
        levels_count[level] += 1


levels_count = dict(levels_count)
print(levels_count)



#TASK7
with open('data_log.txt', 'r') as f:
    logs = f.readlines()

timestamp=[]

for line in logs:
    matches = re.findall(r'\[\d{4}-\d{2}-\d{2} \d{2}:\d{2}:\d{2}\]' ,line)
    timestamp.extend(matches)

timestamp.sort()
print(timestamp)



#TASK8
with open("data_log.txt", "r") as infile, open("masked_data_log.txt", "w") as outfile:

    for line in infile:

    
        line = re.sub(r"\d{1,3}(\.\d{1,3}){3}", "***.***.***.***", line)

    
        line = re.sub(r"\d{3}-\d{3}-\d{4}", "XXX-XXX-XXXX", line)

  
        line = re.sub(r"[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Za-z]{2,}", "hidden@example.com", line)

        outfile.write(line)



#TASK9
import re
error_codes=set()


with open('data_log.txt', 'r') as f:
    for line in f:
       matches = re.findall(r'DB_ERR_\d{4}' ,line)
       error_codes.update(matches)


print(list(error_codes))




#TASK10
pattern = r'\[(\d{4}-\d{2}-\d{2} \d{2}:\d{2}:\d{2})\]\s+(\w+):\s+(.*)'

parsed_logs = []

with open("data_log.txt", "r") as f:
    for line in f:
        match = re.search(pattern, line)
        if match:
            log_entry = {
                "timestamp": match.group(1),
                "level": match.group(2),
                "message": match.group(3).strip()
            }
            parsed_logs.append(log_entry)

with open("parsed_log.json", "w") as f:
    json.dump(parsed_logs, f, indent=4)

print(f"Parsed {len(parsed_logs)} log entries")