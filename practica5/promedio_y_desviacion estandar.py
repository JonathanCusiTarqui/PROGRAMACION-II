import math

#MODULAR ESTRUCTURA
"""
def promedio(lista):
    prom=sum(lista)/len(lista)
    return prom


def desviacion(prom,lista):
    sumatoria=0
    for i in range(len(lista)):
        sumatoria+=(lista[i]-prom)**2
    
    desviacion=math.sqrt(sumatoria/(len(lista)-1))

    return desviacion

lista=list(map(float, input().split()))

calcular_promedio=promedio(lista)
print("el promedio es: "+ str(calcular_promedio))
calcular_desviacion=desviacion(calcular_promedio,lista)
print("la desviacion estandar es: "+ str(calcular_desviacion))

"""
#POO

class promedio_y_desviacion:

    def __init__(self,lista):
        self.lista=lista
        
    def promedio(self):
        prom=sum(self.lista)/len(self.lista)
        return prom

    def desviacion(self):
        prom=self.promedio()
        sumatoria=0
        for i in range(len(self.lista)):
            sumatoria+=(self.lista[i]-prom)**2
        
        desviacion=math.sqrt(sumatoria/(len(self.lista)-1))

        return desviacion
    
    def __str__(self):
        
        return f"el promedio es:  {self.promedio()} y la desviacion es: {self.desviacion()}"
    
   
lista=list(map(float, input().split()))    

calcular=promedio_y_desviacion(lista)

print(calcular)