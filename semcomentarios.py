import math

num = []
soma = 0

for c in range(1, 11):
    num.append(int(input().strip()))
    soma = sum(num)
    mult = math.prod(num) 
   
    
print(num)
print(soma)
print(mult)
