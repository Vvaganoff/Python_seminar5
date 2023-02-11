# Задача 26:  Напишите программу, которая на вход принимает два числа A и B, и возводит число А
# в целую степень B с помощью рекурсии.
# A = 3; B = 5 -> 243 (3⁵)
# A = 2; B = 3 -> 8

def pow(n, a):
    if n==1 or n==0:
      return a
    return pow(n - 1, a) * a

a=int(input("Введите число: "))
b=int(input("Введите целую положительную степень: "))

print(f"Число {a} в степени {b} равно: {pow(b, a)}")
