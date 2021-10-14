# Hello This is a Review about Python and Typing

- type
```python
variable:int|str|bool|float ...

def holaMundo( say:str ) -> str:
    return "Hola "+say
```
- Guide [devhints]("https://devhints.io/python") of Python
- Guide [w3school]("https://www.w3schools.com/python") of Python

#### API REST BUIL WITH FASTAPI OF PYTHON
FastAPI framework, alto desempeño, fácil de aprender, rápido de programar, listo para producción
```terminal
$ pip install fastapi
$ pip install uvicorn[standard]
```
Basic Example
```python
from fastapi import FastAPI
from typing import Optional

app = FastAPI()

@app.get("/")
def read_root():
    return {"Hello": "World"}

```