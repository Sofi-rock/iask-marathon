#1
students = ["Anna", "Ivan", "Olha", "Taras", "Katya"]
grades = [95, 62, 47, 88, 53]
  # Ім’я студента з найвищою оцінкою
max_index = grades.index(max(grades))
print("Найвища оцінка у:", students[max_index])
  # Імена студентів з оцінкою > 60
passed = [students[i] for i in range(len(grades)) if grades[i] > 60]
print("Студенти з оцінкою понад 60:", passed)
  # Кількість студентів, які не склали (< 60)
failed_count = sum(1 for grade in grades if grade < 60)
print("Кількість студентів, які не склали:", failed_count)

#2 
logs = ["ok", "error", "fail", "ok", "error", "warning", "ok", "fail"]
print("Повідомлень ok =", logs.count("ok"))
print("Повідомлень error =",logs.count("error"))
print("Повідомлень fail =",logs.count("fail"))
print("Повідомлень warning =",logs.count("warning"))
відсоток_повідомлень_error = 2/8*100
print("Відсоток повідомлень зі словом Error =", відсоток_повідомлень_error, "%")

#3
expenses = [
    ["Понеділок", 45],
    ["Вівторок", 110],
    ["Середа", 78],
    ["Четвер", 130],
    ["Пʼятниця", 65],
    ["Субота", 160],
    ["Неділя", 90]
]
# День з найбільшими витратами
print("День з найбільшими витратами =",max(expenses, key=lambda x: x[1]))
# Загальні витрати за тиждень
print("Загальні витрати за тиждень =",sum(day[1] for day in expenses))
# Дні з витратами понад 100
print("Дні з витратами понад 100 =",[expenses[i] for i in range(len(expenses)) if expenses[i][1] > 100])

#4
products = [
    ["яблуко", 2, 12.5],
    ["банан", 5, 8.0],
    ["молоко", 1, 34.0],
    ["хліб", 2, 16.0]
]
# Загальна сума чеку
print("Загальна сума чеку =", sum(p[1] * p[2] for p in products))
# Найдорожчий товар (за одиницю)
print("Найдорожчий товар =", max(products, key=lambda x: x[2])[0])
# Новий список "товар - сума грн"
new_list = [f"{p[0]} - {p[1] * p[2]} грн" for p in products]
print("Рядки нового списку:")
for item in new_list:
    print(item)

#5
squares = [x**2 for x in range(1, 31) if x % 2 == 0 and x % 4 != 0 and x not in [10, 14, 18]]
print(squares)

