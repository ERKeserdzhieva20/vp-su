# 1. Пример 1 – първа програма
print("hello world")

#2 Пример2: дефиниране на променлива и присвояване на стойност:


a = 1
b = 2
print("a + b =", a+b)
print("a - b =",a - b)
print("a * b =",a * b)
print("a / b =",a / b)
print("a // b =",a // b)
print("a % b =",a % b)
print("stiga")

# 3
str1 = input("enter a string")
str2 = input("enter a string")

print("Hello " + "World")

# 4
arr1 = [1, 2, 3, 4, 5]
arr2 = [6, 7, 8, 9, 10]

arr1 += arr2

print(arr1)

# 5
arr = input().split()
n = int(input())
for i in range(n):
    print(arr)

# 6
letter = input('Enter a letter: ')
word = input('Enter a word: ')
print(letter in word)

# 7
student = {
  "name": input("Enter your name: "),
  "age": input("Enter your age: "),
  "speciality": input("Enter your speciality: "),
}

print(student.get('name'))
student["age"] = input("Enter your age: ")
student["city"] = input("city")
print(student)

#8
a = int(input('Enter a number: '))
b = int(input('Enter another number: '))
s = input('Enter a measurement: ')
print(a * b, s)
print(f'a = a; b = b; area = {a * b}')

#Напишете програма, която чете от конзолата три числа a, b и h и пресмята
# лицето на трапец с основи a и b и височина h.
# (a + b) * h / 2
# Принтирайте резултата на екрана, като го закръглите до втория знак след
# десетичната запетая.
a = int(input())
b = int(input())
h = int(input())
print(f"{((a + b) * h / 2):.2f}")

# Напишете програма, която чете от конзолата число r и пресмята и
# отпечатва лицето и периметъра на окръжност с радиус r. Принтирайте
# резултата, като го закръглите до 3 знака след десетичната запетая.
r = float(input())
print(f"{2 * r * 3.14:.3f}")
print(f"{r * r * 3.14:.3f}")

# Напишете програма, която да подкани потребителя да въведе броя на
# часовете и тарифа за час. Да се изчисли и принтира брутното заплащане.
hours = int(input("Enter hours: "))
rate = float(input("Enter rate: "))
print(f"Pay: {hours * rate:.2f}")