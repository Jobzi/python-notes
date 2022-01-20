aT:int=5
a=5
print("Tipado estricto", aT)
print("Tipado dinamico", a)

pares= []
pares.append(4)
print(pares)

"""
@suma recibe dos parametros a,b tipados a enteros y devuelve un valor entero
"""
def suma(a:int,b:int)->int:
    return a+b

"""
@Fullname recibe dos parametros a,b tipados a string y devuelve un string
"""
def fullName(a:str,b:str)->str:
    return a+b



print("Tengo una Suma de dos Numeros",suma(5,8))
print("Hola Soy:",fullName("Jipson"," Murillo"))

import typing
number_or_string = typing.NewType('number_or_string', typing.Union[int, str])

hola: typing.List[number_or_string] = [1, 2, 3]
print(hola)

hello2: number_or_string = [True]
print(hello2)