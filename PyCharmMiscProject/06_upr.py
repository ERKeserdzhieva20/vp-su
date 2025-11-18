# Пример 1: Дефиниране на клас и създаване на обект
class MyFirstClass:
    x = 5  # атрибут на класа

# Пример 2: Създаване на обект
MyFirstObject = MyFirstClass()
print(MyFirstObject.x)  # 5

# Пример 3: Конструктор __init__()
class Person:
    def __init__(self, name, age):
        self.name = name    # инстанционен атрибут
        self.age = age      # инстанционен атрибут

MyPerson = Person("Ivan", 35)
print(MyPerson.name)  # Ivan

# Пример 4: Частни атрибути и методи
class Car:
    def __init__(self, color):
        self.__color = color  # частен атрибут

    def get_color(self):  # getter
        return self.__color

    def set_color(self, color):  # setter
        self.__color = color

#Пример 5: Методи на обектите
car = Car("red")
print(car.get_color())  # red
car.set_color("blue")
print(car.get_color())  # blue


class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def greetings(self):
        print(f"Hello, my name is {self.name}")


person = Person("Ivan", 35)
person.greetings()  # Hello, my name is Ivan

#Пример 6: Наследяване
class Person:
    def __init__(self, fname, lname):
        self.firstname = fname
        self.lastname = lname

    def printname(self):
        print(self.firstname, self.lastname)


class Student(Person):  # наследява Person
    def __init__(self, fname, lname, year):
        super().__init__(fname, lname)  # извиква родителския конструктор
        self.graduationyear = year

    def welcome(self):
        print(f"Welcome {self.firstname} {self.lastname} to the class of {self.graduationyear}")


student = Student("Petar", "Vasilev", 2019)
student.printname()  # Petar Vasilev
student.welcome()  # Welcome Petar Vasilev to the class of 2019

#Пример 7: Специален метод __str__
class Person:
    def __init__(self, fname, lname):
        self.firstname = fname
        self.lastname = lname

    def __str__(self):
        return f"{self.firstname} {self.lastname}"


person = Person("Polina", "Koleva")
print(person)  # Polina Koleva (автоматично извиква __str__)

# Задача 1: Да се напише код на Python, който дефинира клас Person с полета име
# (name), фамилия (family), възраст (age), националност (nationality). Да се
# дефинира конструктор, който инициализира полетата на класа. Да се добави
# метод print, който отпечатва имената и националността на съответното лице.
# Да се създадат обекти-инстанции на класа. За тях да се извика методът print.

class Person:
    def __init__(self, name, family, age, nationality):
        self.name = name
        self.family = family
        self.age = age
        self.nationality = nationality
    def print(self):
        print(self.family, " ", self.nationality)

person1 = Person("Ivan", "Petrov", 30, "Bulgarian")
person2 = Person("Maria", "Ivanova", 25, "Bulgarian")
print("Задача 1:")
person1.print()
person2.print()

# Задача 2: Да се добави към кода от Задача 1 клас Student, наследник на класа Person с
# две нови полета – университет (university) и година на обучение
# (yearofstudy). Да се предифинира за него методът print, така, че да отпечатва
# и тези две полета. Да се създадат инстанции на новия клас и за тях да се
# извика методът print.

class Student(Person):
    def __init__(self, name, family, age, nationality, university, yearofstudy):
        super().__init__(name, family, age, nationality)
        self.university = university
        self.yearofstudy = yearofstudy
    def print(self):
        super().print()
        print(self.university, " ", self.yearofstudy)
student1 = Student("Georgi", "Kotakov", 19, "Bulgarian", "TU", 1)
student2 = Student("Elena", "Keserdzhieva", 19, "Bulgarian", "TU", 1)
print("Задача 2:")
student1.print()
student2.print()

# Задача 3: Да се добави към кода от Задача 1 и Задача 2 клас Lecturer, наследник на
# класа Person с две нови полета – университет (university) и опит (experience)
# – брой години преподавателски стаж. Да се предифинира за него методът
# print, така, че да отпечатва тези две полета. Да се създадат инстанции на
# новия клас и за тях да се извика методът print.
class Lecturer(Person):
    def __init__(self, name, family, age, nationality, university, experience):
        super().__init__(name, family, age,nationality)
        self.university = university
        self.experience = experience
    def print(self):
        super().print()
        print(self.university, " ", self.experience)

lecturer1 = Lecturer("Dragan", "Dimitrov", 45, "Bulgarian", "TU", 20)
lecturer2 = Lecturer("Petar", "Georgiev", 50, "Bulgarian", "TU", 25)
print("Зчадача 3:")
lecturer1.print()
lecturer2.print()

#Допълнителна задача
class Book:
    def __init__(self, title, author, year, status):
        self.title = title
        self.author = author
        self.year = year
        self.status = status
    def print(self):
        print(self.title, self.author, self.year, self.status)

books = [
    Book("1984", "George Orwell", 1949, "available"),
    Book("To Kill a Mockingbird", "Harper Lee", 1960, "borrowed"),
    Book("The Great Gatsby", "F. Scott Fitzgerald", 1925, "available"),
]

print("Допълнителна задача:")
for book in books:
    book.print()

def add_book(title, author, year, status):
    new_book = Book(input("Title:"), input("Authur:"), input("Year:"), input("Status:"))
    books.append(new_book)

def remove_book(title):
    for book in books:
        if book.title == title:
            books.remove(book)
            break