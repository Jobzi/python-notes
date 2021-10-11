"""
dict = {}
dict.keys()
dict.values()
"key" in dict    # let's say this returns False, then...
dict["key"]      # ...this raises KeyError
dict.get("key")  # ...this returns None
dict.setdefault("key", 1)
**dict           # expands all k/v pairs in place
"""

jipsonmurillo = {
  "pronouns": 'he/him',
  "code": [
    {
      "mobile": {
        "framework": ['Flutter', 'React Native'],
        "languages": ['Dart', 'Java', 'JS', 'TS']
      },
    }
  ],
  "database": ['MySql', 'PostgreSQL', 'MongoDB', 'Firebase'],
  "tools": [
    'VS Code ♥',
    'Node.js',
    'GraphQL',
    'Vercel',
    'RunJs',
    'Docker',
    'Jest',
    'Cypress'
  ],
}


print(jipsonmurillo.keys()) #return the keys
print(jipsonmurillo.values()) #return the values
print(jipsonmurillo.get("code")) #return the values

for key, val in jipsonmurillo.items():
    print(key)

#The fromkeys() method returns a dictionary with the specified keys and the specified value.
x = ('key1', 'key2', 'key3')
y = 0
thisdict = dict.fromkeys(x, y)
print(thisdict)

#The items() method returns a view object. The view object contains the key-value pairs of the dictionary, as tuples in a list.
car = {
    "brand": "Ford",
    "model": "Mustang",
    "year": 1964
}
x = car.items()
print(x)

#The pop() method removes the specified item from the dictionary.
car = {
    "brand": "Ford",
    "model": "Mustang",
    "year": 1964
}
car.pop("model")
print(car)

#The update() method inserts the specified items to the dictionary.
car = {
    "brand": "Ford",
    "model": "Mustang",
    "year": 1964
}
car.update({"color": "White"})
print(car)
car["uno"]=1 #shot format the assign value to dict 
print(car)
