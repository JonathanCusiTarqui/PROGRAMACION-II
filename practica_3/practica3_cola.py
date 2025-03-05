class cola:
    def __init__(self, n):
        self.arreglo = [None] * (n + 1)
        self.inicio = 0
        self.fin = 0
        self.max = n
    
    def adicionar(self, d):
        if self.fin == self.max:
            print("cola llena")
        else:
            self.fin = (self.fin + 1) % (self.max + 1)
            self.arreglo[self.fin] = d
    
    def eliminar(self):
        if self.inicio == self.fin:
            return "vacio"
        else:
            self.inicio = (self.inicio + 1) % (self.max + 1)
            dato = self.arreglo[self.inicio]
            if self.inicio == self.fin:
                self.inicio = 0
                self.fin = 0
            return dato
    
    def peek(self):
        if self.inicio == self.fin:
            return "vacio"
        return self.arreglo[(self.inicio + 1) % (self.max + 1)]
    
    def is_empty(self):
        return self.inicio == self.fin
    
    def is_full(self):
        return (self.fin + 1) % (self.max + 1) == self.inicio

# Ejemplo de uso:

# Crear una cola
mi_cola = cola(4)

# Adicionar elementos
mi_cola.adicionar("1")
mi_cola.adicionar("2.45")
mi_cola.adicionar("5")
mi_cola.adicionar("89") 

# Ver el primer elemento sin eliminarlo
print("Peek:", mi_cola.peek()) 

# Eliminar elementos
print("Eliminar:", mi_cola.eliminar()) 
print("Eliminar:", mi_cola.eliminar())  

# Ver si la cola está vacía
print("¿Está vacía?", mi_cola.is_empty())  

# Eliminar el resto de los elementos
print("Eliminar:", mi_cola.eliminar())  
print("Eliminar:", mi_cola.eliminar())  

# Ver si la cola está vacía después de eliminar todos los elementos
print("¿Está vacía?", mi_cola.is_empty()) 
