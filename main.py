"""""
#from src.method import Person
p1 = Person("John", 36)
p1.printname()
for i in range(rows+1):
    print('*'*i)
"""""
#https://docs.microsoft.com/es-es/cpp/c-language/escape-sequences?view=msvc-160

a=5
b=5

print(a+b)
print('---------------------------')
for i in range(5):
    print(i)
print('---------------------------')

while i < 6:
  print(i)
  i += 1


print('hola '+str(i))

value = input('ingrese un numero para la matriz: 1')
rows=int(value)
for i in range(rows):
    for j in range(rows):
        print('['+str(i)+']'+'['+str(j)+']')

