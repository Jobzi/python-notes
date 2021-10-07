TEST WITH PYTEST
----
## ___"DON'T REPEAT YOURSELF"___

**My Firts Test** 
Test para la funcion de suma de dos elementos
````python
import pytest

def my_sum_function(a,b):
    return a + b

def test_my_sum_function():
    expected = 5
    result = my_sum_function(2,3)
    assert expected == result
````
**Run test**
`-vv` para que sea mas verboso la informacion que devuelve
````terminal
$ pytest -vv
````
### MARKS
Para correr test especificos en pytest tiene una anotacion `@pytest.mark.NOMBRE_MARCA`
````python
import pytest
@pytest.mark.MYMARCA
def test_some_calculator():
    assert some_calculator(1,2)==3 #
````
para ejecutar los test con la marca espeficica
````terminal
$ pytest -m MYMARCA -vvv
````
para ejecutar los test que tiene la marca

````terminal
$ pytest -m "not MYMARCA" -vvv
````
Otra forma de pasar test dado un caso de uso especificos se utiliza la bande `-k` 
ejemplo `test.talk.py:: test_my_VALUE`
`VALUE` iria despues de la bandera para correr las funciones que solo tenga esa palabra
````terminal
$ pytest -k VALUE -vvv

````
### FIXTURES
No dupliques valores para REALIZAR TEST

**ASI NO DEBES HACERLO**
````python
def test_years_util_retirement():
    person = Person(
        name='foo',
        age=30,
        profession='student'
    )
    assert years_util_retirement(person)==35

def test_name_and_age():
    person = Person(
        name='foo',
        age=30,
        profession='student'
    )
    assert name_and_age(person)==('foo',30)
"""
Esto no deberia pasar al realizar cualquier tipo de test para eso pytest utiliza lo que es Fixtures
"""
````
````python
#decorador
#@FIXTURE es una funcion que se ejecuta antes de realizar cualquier tipo de test
@pytest.fixture
def person(): 
    return Person(
        name='foo',
        age=30,
        profession='student'
    )

def test_years_util_retirement(person):
    assert years_util_retirement(person)==35

def test_name_and_age(person):
    assert name_and_age(person)==('foo',30)
````
### **Ejemplo de test a probar**

````python
#Este es una funcion cualquierra para realizar un test
def test_some_calculation():
    assert some_calculator(1,2) ==3
````

### PARAMETRIZE
`@pytest.mark.parametrize` es un decorador de pytest para dar valores iniciales
````python
@pytest.mark.parametrize("a,b,expected_result",[
    (1,2,3), # (a:1,b:2,expected_result:3)
    (3,3,6),
    (3,-2,1),
    ])
def test_some_calculation_param(a,b,expected_result):
    assert some_calculation(a,b)===expected_result
````
otro ejemplo utilizando el caso de uso PALINDROMO
````python
@pytest.mark.parametrize("maybe_palindrome, expected_result", [
    ("", True),
    ("a", True),
    ("Bob", True),
    ("Never odd or even", True),
    ("Do geese see God?", True),
    ("abc", False),
    ("abab", False),
])
def test_is_palindrome(maybe_palindrome, expected_result):
    assert is_palindrome(maybe_palindrome) == expected_result
````

### PYTEST MOCK
Es una libreria aparte para realizar el test `pip install pytest-mock`

````python
def test_make_a_dict(mocker):
    mocker.patch(
        "test_talk.some_calculation",
        return_value=5,
        autospec=True, #Validar la Interfaz
    )
    my_dict = make_a_dict(2,3)
    expected_dict = {"a":2,"b":3,"result":5}

    assert my_dict == expected_dict
````
