pares = [2,4,6,8,10]

"""
    [fn(i) for i in list]        # .map
    map(fn, list)                # .map, returns iterator
"""
result = [x*2 for x in pares]
print(result)

"""
filter(fn, list)                 # .filter, returns iterator
[fn(i) for i in list if i > 0]   # .filter.map
"""
result = [x for x in pares if x==2]
print(result)

c = {'name': 'Pooka', 'first_name': 'Oooka'}
result= ["{}:{}".format(k.upper(), v.upper()) for k, v in c.items()]
print(result)
