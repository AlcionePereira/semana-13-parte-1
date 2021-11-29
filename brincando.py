c = 0
zero = []
invert = []
num2 = []
n2 = []


n1 = int(input().strip())
for C in range(1,n1 +1 ):
    n2 = int(input().strip())
    zero.insert(0, 0)
    invert.insert(0, n2)
    
    num2.append(n2)
    
# zero   
if n1 == 0:
    print('[]')
else:
    print(zero)

#complete do 1 a n      
total = []
for i in range(n1):
    total.append(i+1)
    
if n1 == 0:
    print('[]')
else:
    print(total)

#Mostrar sequencia n2 até n1
if n1 == 0:
    print('[]')
else:
    print(num2)
    
#mostrar os números inverso
invert =[]
for i in range(n1):
    inv = int(input().strip())
    invert.insert(0, inv)
print(invert)
                 



