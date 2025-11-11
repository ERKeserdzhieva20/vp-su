# Пример 1: Проста функция без параметри
def f():
    s = '-- Inside f()'
    print(s)

print('Before calling f()')
f()
print('After calling f()')

# Пример 2: Функция с параметри по подразбиране
def f(qty=6, item='bananas', price=1.74):
    print(f'{qty} {item} cost ${price:.2f}')

f(4, 'apples', 2.24)  # 4 apples cost $2.24
f(4, 'apples')        # 4 apples cost $1.74
f(4)                  # 4 bananas cost $1.74
f()                   # 6 bananas cost $1.74
f(item='pears', qty=9)  # 9 pears cost $1.74
f(price=2.29)        # 6 bananas cost $2.29

# Пример 3: Функция с return statement
def f():
    print('foo')
    print('bar')
    return  # връща None, може да се изпусне

f()  # foo bar

# Пример 4: Функция с условен return
def f(x):
    if x < 0:
        return
    if x > 100:
        return
    print(x)

f(-3)   # (няма изход)
f(105)  # (няма изход)
f(64)   # 64

# Пример 5: Функция с проверка за грешки
def f(error_cond1=False, error_cond2=False, error_cond3=False):
    if error_cond1:
        return
    if error_cond2:
        return
    if error_cond3:
        return
    # normal processing
    print("Нормална обработка...")

# извикване
f()  # -> Нормална обработка...
f(error_cond2=True)  # -> (няма отпечатване)

# Пример 6: Функция с променлив брой аргументи
def psum(*k):
    result = 0
    for i in k:
        result += i
    return result

s = psum(1, 2, 3, 4)
print(s)  # 10

# 1. Напишете програма, която намира лицето на геометрична фигура като първо се въвежда вида на фигурата:
# 1- квадрат
# 2-правоъгълник
# 3- прав.триъгълник
# За пресмятане на лицето на отделните фигури да се напишат подходящи функции.

def square(a):
    return a ** 2

def rectangle(a, b):
    return a * b

def triangle(a, b):
    return a * b / 2

print("Задача 1:")
print(square(3))
print(rectangle(3, 4))
print(triangle(3, 4))

# 2. Напишете потребителска функция , проверяваща дали число е палиндром.
# Функцията получава като аргумент число, връща като резултат 1,
# ако числото е палиндром и 0 ако числото не е палиндром.
def palindrome(number):
    s = str(number)
    result = 1
    for i in range(0, len(s) // 2):
        if s[i] == s[len(s) - i - 1] :
            continue
        else:
            result = 0
            break
    return result

print("\nЗадача 2:")
print(palindrome(1111))
print(palindrome(100))

# 3. Програма, която реализира калкулатор за цели числа. Действията които изпълнява са :
#  Събиране +
#  Изваждане –
#  Умножение *
#  Деление /
# Потребителя въвежда вида на операцията.
# После въвежда две числа и резултата се извежда на екрана . Реализирайте отделни функции за отделните операции.
def cal(str, a, b):
    if str == '+':
        return a + b
    elif str == '-':
        return a - b
    elif str == '*':
        return a * b
    elif str == '/':
        return a / b
    else:
        return 0

print("\nЗадача 3:")
print(cal('+', 2, 4))
print(cal('-', 2, 4))
print(cal('*', 2, 4))
print(cal('/', 2, 4))



# 4. На функция се подават два аргумента: списък с числа и число.
# Променете всички елементи от списъка със стойност по-голяма от даденото число на 0(нула)
def funky(list, num):
    for i in range(len(list)):
        if list[i] > num:
            list[i] = 0
    return list

print("\nЗадача 4:")
print(funky([1, 2, 3, 4, 5], 3))