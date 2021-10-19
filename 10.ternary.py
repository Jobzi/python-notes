# <expression1> if <condition> else <expression2>

age = 15
print('kid' if age < 18 else 'adult')

age = 15
print('kid' if age < 13 else 'teenager' if age < 18 else 'adult')
