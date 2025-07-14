import json

def dict_to_json(slovnyk) :
    return json.dumps(slovnyk)


#First task

""" contacts = {
 "Anna": "093-123-45-67",
 "Ivan": "050-888-99-00",
 "Olha": "097-777-33-22"
}

contacts["Taras"] = "063-000-11-22"
del contacts["Ivan"]
dict_to_json(contacts)
print("Всі імена :", ", ".join(list(contacts.keys())))
print("Всі номери :", ", ".join(list(contacts.values())))

if "Katya" in contacts:
    print("Katya є в книзі.")
else:
    print("Katya відсутня в книзі.")
    #Була проблема з тим, як вивести все списком, але розібралася
 """
   
#Second task

grades = {
"math": 88,
"physics": 75,
"english": 93,
"history": 59
}

max_subject = max(grades, key=grades.get)
print("Найвища оцінка =", max_subject)

average = sum(grades.values()) / len(grades)
print("Середня оцінка =", average)

high_scores = [subject for subject, score in grades.items() if score > 80]
print("Предмети де оцінка > 80 =", high_scores)
#трохи легше ніж перше завдання

#Third task

transactions = [
    ("Anna", 200),
    ("Ivan", -50),
    ("Anna", 100),
    ("Olha", 500),
    ("Ivan", 150),
    ("Olha", -100),
]

balances = {}

for name, amount in transactions:
    balances[name] = balances.get(name, 0) + amount

richest = max(balances, key=balances.get)
print("Найбільший баланс у клієнта:", richest)

negative_balances = [name for name, balance in balances.items() if balance < 0]
print("Клієнти з від’ємним балансом:", negative_balances)

#Fourth task

text = "hello world hello again hello world test world"

words = text.split()
word_count = {}

for word in words:
    word_count[word] = word_count.get(word, 0) + 1

print(word_count)

#Fifth task

import json

student = {
    "name": "Anna",
    "age": 20,
    "courses": ["math", "physics", "english"]
}

json_str = json.dumps(student)
print(json_str)

student_back = json.loads(json_str)
student_back["courses"].append("history")
print(student_back)
