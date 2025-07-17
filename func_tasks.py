""" #1
def hello_world() :
    return str('Hello, world!')
print(hello_world())

#2
def greet(name) :
    return f'Привіт, {name} !'
print(greet("Anna"))

#3
def square(n) :
    return n**2
print(square(int(input())))

#4
def add(a, b) :
    return a + b
print(add(1, 5)) """

""" #5
def greet(name="Гість") :
    return f'Привіт, {name} !'
print(greet())

#6
def factorial(n):
    result = 1
    for i in range(1, n + 1):
        result *= i
    return result

print(factorial(int(input()))) """

""" #7
def is_even(n):
    return n % 2 == 0
print(is_even(int(input())))

#8
def print_numbers(n):
    return [i for i in range(1, n + 1)]
print(print_numbers(int(input()))) """

""" #9
def find_name(name, name_list) :
    return name in name_list
names = ["Оля", "Андрій", "Софія", "Іван"]
print(find_name("Софія", names)) """

""" #10
def max_of_three(a, b, c) :
    return max(a, b, c)
a = int(input())
b = int(input())
c = int(input())
print(max_of_three(a, b, c)) """

""" #11
def reverse_string(s) :
    return ''.join(reversed(s))
s = 'Hello, my name is'
print(reverse_string(s)) """

""" #12
vowels = "aeiouAEIOU"
def count_vowels(s):
    count = 0
    for char in s:
        if char in vowels:
            count += 1
    return count
s = 'Hello, my name is'
print(count_vowels(s)) """

""" #13
def average(*numbers) :
    return sum(numbers) / len(numbers)
print(average(1, 3, 4, 5, 88)) """

""" #14
def print_user_info(**info) :
    return info
print(print_user_info(name = "sofia", age = 13, surname = "Stetsiuk" )) """

#15
def inner() :
    return f'Я - вкладена функція!'

def outer() :
    return inner()
print(outer())

