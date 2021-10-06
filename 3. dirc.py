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


print(jipsonmurillo.keys())
print(jipsonmurillo.values())
print(jipsonmurillo.get("code"))

for key, val in jipsonmurillo.items():
    print(key)