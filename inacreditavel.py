par = []
impar = []
lista = []

for c in range(1, 21):
    num = int(input().strip())
    lista.append(num)
    if num % 2 == 0:
        par.append(num)
    else:
        impar.append(num)
        
print(lista)    
print(f'{par[:]}')
print(f'{impar[:]}')
