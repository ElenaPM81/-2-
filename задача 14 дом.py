# Требуется вывести все целые степени двойки (т.е. числа вида 2k), не превосходящие числа N.

N = int(input('Введите число N:'))
a = 2
result = 0 
for i in range(N):
    result = a**i

    if i < N:
     i+= 1

     print(result)


   
   

   