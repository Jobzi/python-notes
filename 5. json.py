import json
"""
    Convert any json file to dictionary. Used "json.loads(value)"
"""
# some JSON:
x =  '{ "name":"John", "age":30, "city":"New York"}'
# parse x:
y = json.loads(x)
# the result is a Python dictionary:
print(y["age"])
print(y)
print(type(y))  #class dict


print("====")

# a Python object (dict):
x = {
  "name": "John",
  "age": 30,
  "city": "New York"
}
# convert into JSON:
y = json.dumps(x)
# the result is a JSON string:
print(y)
print(type(y)) #output: string
