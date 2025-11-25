#Синтактични грешки
# Грешен код - липсват две точки
# while True print('Hello world')

# Коректен код
while True: print('Hello world')

# Изключителни ситуации
# ZeroDivisionError
10 * (1/0)

# NameError
4 + spam*3

# TypeError
'2' + 2

# Прихващане и обработка на изключения
# Базов пример с try-except
try:
    print(x)
except:
    print("An exception occurred")

# Обработка на конкретни типове грешки
try:
    print(x)
except NameError:
    print("Variable x is not defined")
except:
    print("Something else went wrong")

# Използване на else блок
try:
    print("Hello")
except:
    print("Something went wrong")
else:
    print("Nothing went wrong")

# Практически пример с файлове
import sys

for arg in sys.argv[1:]:
    try:
        f = open(arg, 'r')
    except OSError:
        print('cannot open', arg)
    else:
        print(arg, 'has', len(f.readlines()), 'lines')
        f.close()

# Използване на finally блок
try:
    print(x)
except:
    print("Something went wrong")
finally:
    print("The 'try except' is finished")

# Практически пример с файл
try:
    f = open("demofile.txt")
    f.write("Lorum Ipsum")
except:
    print("Something went wrong when writing to the file")
finally:
    f.close()

# Въвеждане на число с валидация
while True:
    try:
        x = int(input("Please enter a number: "))
        break
    except ValueError:
        print("Oops! That was no valid number. Try again...")

# Обработка на изключения във функции
def this_fails():
    x = 1/0

try:
    this_fails()
except ZeroDivisionError as err:
    print('Handling run-time error:', err)

#Обработка на изключения във функции
def this_fails():
    x = 1/0

try:
    this_fails()
except ZeroDivisionError as err:
    print('Handling run-time error:', err)

#Генериране на изключения
#Генериране на общи изключения
x = -1
if x < 0:
    raise Exception("Sorry, no numbers below zero")

#Генериране на специфични изключения
x = "hello"
if not type(x) is int:
    raise TypeError("Only integers are allowed")

#Пример с NameError
raise NameError('HiThere')

#Еквивалентни форми
# Двата реда са еквивалентни
raise ValueError
raise ValueError()

#Дефиниране на собствени изключения
class Error(Exception):
    """Base class for exceptions in this module."""
    pass

class InputError(Error):
    """Exception raised for errors in the input.

    Attributes:
        expression -- input expression in which the error occurred
        message -- explanation of the error
    """
    def __init__(self, expression, message):
        self.expression = expression
        self.message = message

class TransitionError(Error):
    """Raised when an operation attempts a state transition that's not allowed.

    Attributes:
        previous -- state at beginning of transition
        next -- attempted new state
        message -- explanation of why the specific transition is not allowed
    """
    def __init__(self, previous, next, message):
        self.previous = previous
        self.next = next
        self.message = message

#  1. Да се създаде клас BankAccount, който представя банкова сметка.
# Класът трябва да има:
# Полeта (атрибути):
# owner – име на собственика
# balance – текущ баланс (число, по начало 0)
# Методи:
# deposit(amount) – увеличава баланса със сумата amount, ако amount е положително число, добавя го към баланса в противен случай да отпечата съобщение, че сумата е невалидна.
# withdraw(amount) – намалява баланса със сумата amount, ако има достатъчно пари по сметката, да изтегли сумата, ако няма достатъчно средства, да отпечата съобщение, че балансът е недостатъчен.
# print_info() – отпечатва името на собственика и текущия баланс.
# Да се създаде обект от класа BankAccount, да се извикат методите deposit() и withdraw(), и накрая да се извика print_info(), за да се види крайният баланс.

class BankAccount:
    def __init__(self, owner):
        self.owner = owner
        self.balance = 0

    def deposit(self, amount):
        if amount > 0:
            self.balance += amount
        else:
            print("Сумата е невалидна.")

    def withdraw(self, amount):
        if amount <= self.balance:
            self.balance -= amount
        else:
            print("Балансът е недостатъчен.")

    def print_info(self):
        print(f"Собственик: {self.owner}, Текущ баланс: {self.balance}")

account = BankAccount("Ivan Petrov")
account.deposit(100)
account.withdraw(50)
account.withdraw(100)
account.print_info()

# Напишете код на метод, който приема като параметър  име на текстов файл, прочита съдържанието на файла и го връща като стринг. Какво е правилно да направи методът с възникващите изключения?
def read_file(file_name):
    try:
        with open(file_name, 'r', encoding='utf-8') as file:
            content = file.read()
            return content
    except FileNotFoundError:
        print("Файлът не е намерен.")
    except IOError:
        print("Възникна грешка при четене на файла.")

print(read_file("example.txt"))
print(read_file("e.txt"))
print(read_file("test.txt"))
