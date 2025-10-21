# 1. Да се напише програма, която въвежда n цели числа (n &gt; 0) и намира най-
# голямото между тях. Първо се въвежда броят на числата n. След това се
# въвеждат n цели числа
#
# a = input("Enter a number:")
# for i in range(0, int(a)):
#     b = input("Enter a number:")
#     if i == 0:
#         max = b
#     if b > max:
#         max = b
# print("The largest number is:", max)

# 2. Да се напише програма, която въвежда n цели числа и ги сумира.
# a = input("Enter a number:")
# sum = 0
# for i in range(0, int(a)):
#     b = input("Enter a number:")
#     sum += int(b)
# print("The sum is:", sum)

#  3. Да се напише програма, която въвежда число n и печата триъгълник от
# звездички
# a = input("Enter a number:")
# for i in range(1, int(a)+1):
#     for j in range(1, i+1):
#         print("*", end="")
#     print()

# 4. Напишете програма, която проверява дали дадено число е просто, числото се
# въвежда от потребителя.
# a = int(input("Enter a number:"))
# is_prime = True
# for i in range(2, int(a / 2) + 1):
#     if a % i == 0:
#         is_prime = False
#         break
#
# if is_prime and a > 1:
#     print(f"{a} is a prime number.")
# else:
#     print(f"{a} is not a prime number.")