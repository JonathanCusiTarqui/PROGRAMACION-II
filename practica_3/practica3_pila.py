class pila:
    def __init__(self, n):
        self.top = 0
        self.n = n
        self.arreglo = [0] * (n + 1)  # Crear un arreglo de tamaño n+1
    
    def push(self, e):
        if self.top < self.n:
            self.top += 1
            self.arreglo[self.top] = e
        else:
            print("Pila llena")

    def pop(self):
        if self.top == 0:
            print("Pila vacía")
            return None
        dato = self.arreglo[self.top]
        self.top -= 1
        return dato

    def peek(self):
        if self.top == 0:
            print("Pila vacía")
            return None
        return self.arreglo[self.top]

    def is_empty(self):
        return self.top == 0

    def is_full(self):
        return self.top == self.n

# Ej:

# Crear una pila 
mi_pila = pila(3)

# Añadir elementos a la pila
mi_pila.push(10)
mi_pila.push(20.0)
mi_pila.push(3046564)

# Intentar añadir un elemento cuando la pila esté llena
mi_pila.push(40.0) 

# Ver el elemento en la parte superior de la pila
print("Elemento en el tope:", mi_pila.peek())  

# Eliminar elementos de la pila
print("Eliminar elemento:", mi_pila.pop())  
print("Eliminar elemento:", mi_pila.pop())  

# Verificar si la pila está vacía
print("¿Está vacía?", mi_pila.is_empty())  

# Eliminar el resto de los elementos
print("Eliminar elemento:", mi_pila.pop())  
print("Eliminar elemento:", mi_pila.pop())  

# Verificar si la pila está vacía después de vaciarla
print("¿Está vacía?", mi_pila.is_empty())  
