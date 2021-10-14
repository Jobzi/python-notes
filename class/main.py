class Matematicas():
    def __init__(self,name: str, a: int, b: int):
        #run de validation
        assert a>=0, f"El valor de {a} debe ser mayor a cero"
        assert b>=0, f"El valor de {b} debe ser mayor a cero"
        #init values
        self.name = name
        self.a = a
        self.b = b
    
    def suma(self):
        return self.a + self.b

operacion = Matematicas("Operacion 1",5,3)

print(operacion.suma())
print(Matematicas.__dict__)