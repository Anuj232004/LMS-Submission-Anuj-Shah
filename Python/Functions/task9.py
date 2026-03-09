#data
data = [
{"name": "Alice", "age": 30, "score": 85},
{"name": "Bob", "age": 25, "score": 90},
{"name": "Charlie", "age": 35, "score": 95}
]

#function
names = list(map(lambda person:person["name"],data))
score =list(map (lambda person :person["score"],data))

avg_scores = sum(score)/len(score)
print(names)
print ("Average Score:",avg_scores)