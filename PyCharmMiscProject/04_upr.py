#Пример 1: Дефиниране на кортеж и достъп до елементи
s = [1, 3, 5, 7]
print(s[1])
s[1] = 11
print(s[1])

#Пример 2: Създаване на празен списък и списък от символи
s = list()
s1 = list('Python')
print(s1)

#Пример 3: Добавяне на елементи в списък
s = []
s.append(5)
s.append(10)
s.append(20)
print(s)

#Пример 4: Генериране на списък с помощта на list comprehension
A=list( k for k in range(1,21) if k%3!=0)

#Пример 5: Срезове на списъци
s = [1, 2, 3, 4, 5, 6]
print(s[::-1]) #извеждаме елементите в обратен ред
print(s[:-1]) # принтираме без последния елемент
print(s[1:]) #принтираме без първия елемент
print(s[0:2]) #първите два елемента
print(s[-1:]) #последният елемент

#Пример 6: Събиране на списъци
s = [1, 2, 3, 4, 5, 6]
s1 = [9, 8]
s2 = s +s1
print(s2)

#Пример 7: Вложени списъци -многомерни списъци- всеки един елемент от списъка може да съдържа друг
# списък, кортеж или речник
s = [[1, 2, 3, 4], ['a', 'b', 'c'], [10, 20]]
print(s[0][3]) #достъпваме на първия списък 4-тия елемент
print(s[2][0]) #достъпваме на третия списък 1-вия елемент

#Пример 8: Итериране през елементите на списък
s = [1, 2, 3, 4, 5, 6]
for i in s:
    print(i, end=' ')

#Пример 9: Итериране през елементите на списък чрез индекси
s = [1, 2, 3, 4, 5, 6]
for i in range(len(s)):
    print(s[i], end=' ')

#Пример 10: Проверка за членство в списък
s = [2, 4, 6, 8]
print(4 in s) #True

#Пример 11: Полезни методи на списъци
s = [2, 4, 6, 8, 2]
print(s.count(2)) # 2
print(s.index(3)) #ValueError: 3 is not in list
print(min(s)) # 2
print(max(s)) # 8

#Пример 12: Промяна на списъци чрез методи
s = [2, 4, 6, 8, 2]
s.append(22) # добавя в края на списъка 22
print(s)
s += [44, 88] # добавя в края 44,88
print(s)

s.insert(0, 90) # вмъква в началото 90
print(s)
s.pop(0) # изтрива първия елемент на списъка
print(s)
s.remove(2) # изтрива елемента със стойност 2
print(s)
del s[4] # премахва елемента с индекс 4
print(s)

#Пример 13: Random и списъци
import random
s = [2, 4, 6, 8, 2]
random.shuffle(s)
print(s) #[4, 8, 6, 2, 2]
print(random.choice(s)) # 8
s.reverse()
print(s) #[2, 4, 6, 8, 2]

#Пример 14: Сортиране на списъци
s = [45, 10, 55, 5, 35]
s.sort()
print(s) #[5, 10, 35, 45, 55]
s.sort(reverse=True)
print(s) #[55, 45, 35, 10, 5]


s1 = ['s', 'T', 'a', 'E', 'f']
s1.sort(key=str.lower)
print(s1) # ['a', 'E', 'f', 's', 'T']

s1 = ['s', 'T', 'a', 'E', 'f']
s1.sort() # ['E', 'T', 'a', 'f', 's']
print(s1) # ['E', 'T', 'a', 'f', 's']

#Пример 15: Дефиниране на кортеж
k = (7, 5, 3) #създаване на кортеж от 3 елемента
print(k)

#Пример 16: Преобразуване списък в кортеж
tup = tuple([10, 20, 30])
print(tup)

#Пример 17: Преобразуване на низ в кортеж
tup1 = tuple('python')
print(tup1) #('p', 'y', 't', 'h', 'o', 'n')

#Пример 18: Създаване на празен кортеж
tup2 = tuple() #празен кортеж
print(tup2)

#Пример 19: Основни операции с кортежи
k = (7, 5, 3, 6, 1)
print(k[0]) #достъп до елемент по индекс
print(k[2:3]) # сечение
print(7 in k) # проверка за наличие на елемент
print(k * 3) #повторение
tup = k + (2, 4) #конкатенация
print(tup)

#Пример 20: Полезни методи на кортежи
tup = (7, 5, 3, 6, 1)
tup.index(1)
print(tup.index(1)) # 4

tup.count(5)
print(tup.count(5)) # 1

#Пример 21: Обхождане на елементите на кортеж
for i in tup:
    print(i, end=' ')

#Пример 22: Дефиниране на речник
d = dict()
d1 = dict(name='Ivan', l_name='Petrov', age=25)
d3 = dict([ ('name', 'Polina'), ('l_name', 'Koleva') ])
print(d1)
print(d3)

#Пример 23: Достъп до елементи на речник
d = { }
d['name'] = 'Petyr'; d['l_name'] = 'Kolev'
print(d)

d = {'name': 'Ivan', 'last_name': 'Ivanov'}
print(d)

#Пример 24: Операции с речници
d = {'name': 'Ivan', 'last_name': 'Ivanov'}
print(d['fname']) # KeyError: 'fname', опит за достъп до несъществуващ ключ

b = 'fname' in d
print(b) # False, проверка за наличие на ключ 'fname' в речника

d = {'name': 'Ivan', 'last_name': 'Ivanov'}
len(d)
print(len(d)) # 2, len връща броя на елементите в речника

d['s_name'] = 'Petrov'
print(d) # {'name': 'Ivan', 'last_name': 'Ivanov', 's_name': 'Petrov'},

del d['s_name']
print(d) # {'name': 'ivan', 'last_name': 'ivanov'}, 'del' премахва елемента с ключ 's_name'

d = {"name": "Ivan", "last_name": "Ivanov"}
for key in d.keys(): # .keys() не е задължително
    print("({0} =&gt; {1})".format(key, d[key]), end=" ") # обхождане на елементите на речника
    
d = {"name": "Ivan", "last_name": "Ivanov"}
keys = list(d.keys())
keys.sort() # сортиране на ключовете на речника
for key in keys:
    print("{0} =&gt; {1} ".format(key, d[key]), end=" ")
    # last_name =&gt; Ivanov name =&gt; Ivan
    print(f"{key} =&gt; {d[key]}", end=" ")


# Множества (sets) - неупорядочени колекции от уникални елементи
#Пример 24: Дефиниране на множество
s = set([1, 2, 3, 1]) #list
print(s)
s2 = set("hello") #string

#Пример 25: Обхождане на елементите на множество
s2 = set("hello")
for i in s2:
    print(i, end='') # l h e o

#Пример 26: Фнкция len() с множества
print(len(s2)) # 4

#Пример 27: Обединение на множества : оператор |, в новосъздаденото множество попадат
#само уникални елементи
s = set([1, 2, 3])
s1 = set([4, 2, 6])
s3 = s | s1
print(s3) # {1, 2, 3, 4, 6}

#Пример 28: Разлика на множества: оператор -
s = set([1, 2, 3, 4])
s1 = set([2, 4, 6])
s2 = s - s1 # {1, 3}
s3 = s1 - s # {6 }

#Пример 29: Пресичане на множества: оператор &
s = set([1, 2, 3, 4])
s1 = set([2, 4, 6])
s4 = s & s1 # {2, 4}

#Пример 30: Симетрична разлика на множества: оператор ^
s = set([1, 2, 3, 4])
s1 = set([2, 4, 6])
s5 = s ^ s1 # {1, 3, 6}

#Пример 31: Полезни методи на множеса
s1 = set([2, 4, 6])
s1.add(8) # {8, 2, 4, 6}
s1.remove(2) # {8, 4, 6}
print(s1)
s1.remove(2) # KeyError: 2

#Низове (strings)
#Пример 32: Дефиниране на низ
S=""" hello ,
*****
World!!! """

#Пример 33: Достъп до елементи на низ
S="123"
print(S[0]) # 1
s1="Hello"
s1[:] #фрагмент от позиция 0 до края на низа
s1[:-1:] #изрязваме последния символ на низа &#39;Hell&#39;
s1[1::2] #започва от втория символ до края,стъпка 2 &#39;el&#39;
s1[1::] #изрязваме първия символ 'ello'

#Пример 34: Събиране на низове
print("Hello"+"world")

#Пример 35: Проверка за членство в низ
"hell" in "Hello" # False
"hell" in "hello" # True

#Пример 36: Повторение на низ
print("f" * 5) # fffff

#Пример 37: Дължина на низ
s = "Здравей"
print(len(s)) # 6

#Пример 38: Преобразуване между типове данни
print(str(123)) # "123"

#Пример 39: repr(обект) – връща низова репрезентация на обекта. Използва се в IDLE за
# извеждане на обекти
s = "Hello World"
print(repr(s))


#Задачи

#1. Напишете програма, в която потребителя въвежда цяло число, а
# програмата формира два кортежа, състоящи се от цифрите , влизащи в
# това число. Единият с цифрите на числото в прав ред и втори , в който
# цифрите са в обратен ред.

num = input("Enter an integer: ")
tuple1 = tuple(int(digit) for digit in num)
tuple2 = tuple(int(digit) for digit in reversed(num))

print("Tuple in original order:", tuple1)
print("Tuple in reverse order:", tuple2)


# 2. Напишете програма, в която се създава числов списък. Той се запълва със
# случайни числа. След това между всяка двойка елементи от този списък се
# вмъква нов , равен на сумата от стойностите на съседните елементи.

import random

size = int(input("Enter the size of the list: "))
num_list =  list()
for i in range(size):
    num_list.append(random.randint(1, 100))

print("Original list:", num_list)

i = 1
while i < len(num_list):
    sum_neighbors = num_list[i - 1] + num_list[i]
    num_list.insert(i, sum_neighbors)
    i += 2

print("Modified list:", num_list)

# 3. Напишете програма , в която потребителя въвежда текст и на негова база
# се създава речник. За ключове на речника служат символите от текста, а
# стойността на елементите се определя от броя на съответните символи в
# текста.
# Примерен вход : SSWTWWTAAA
# Речникът ще се състои от 4 елемента :
# А:3 S:2 T:2 W:3

text = input("Enter a text: ")
char_count = {}
for char in text:
    if char in char_count:
        char_count[char] += 1
    else:
        char_count[char] = 1
print("Character count dictionary:", char_count)

# 4. Напишете програма, в която потребителя въвежда чяло число. От него се
# създава списък състоящ се от числата от 1 до това число . Въз основа на
# този списък се създава речник, в който елементите на списъка служат за
# ключове на елементите на речника , а стойностите на тези елементи в
# речника са елементите на списъка но в обратен ред.
# Пример : ако сме въвели числото 4 , създава се списъка [1,2,3,4 ] и на
# негова основа се създава речник с 4 елемента : {1:4, 2:3, 3:2, 4:1}

num = int(input("Enter an integer: "))
num_list = list(range(1, num + 1))

num_dict = dict()
for i in range(len(num_list)):
    num_dict[i + 1] = num_list[num - i - 1]

print("Generated dictionary:", num_dict)
