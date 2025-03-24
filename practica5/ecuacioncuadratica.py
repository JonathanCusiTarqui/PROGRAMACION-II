import math
#MODULAR ESTRUCTURA
"""
def getDiscriminante(a,b,c):
    discriminante=b**2-4*a*c
    return discriminante

def getRaiz1(a,b,discriminante):
    raiz1=(-b+math.sqrt(discriminante))/(2*a)
    return raiz1

def getRaiz2(a,b,discriminante):
    raiz2=(-b-math.sqrt(discriminante))/(2*a)
    return raiz2


a,b,c=map(float, input("ingrese a,b,c: ").split())

evaluar=getDiscriminante(a,b,c)

if evaluar>0:
    r1=getRaiz1(a,b,evaluar)
    r2=getRaiz2(a,b,evaluar)
    print(f"la ecuacion tiene dos raices: {r1} y {r2}")
elif evaluar==0:
    r1=getRaiz1(a,b,evaluar)
    print(f"la ecuacion tiene uan raiz: {r1}")
elif evaluar<0:
    print(f"la ecuacion no tiene raices reales") 

"""
    

"""POO"""

class EcuacionCuadratica:
    def __init__(self,a,b,c):
        self.a=a
        self.b=b
        self.c=c

    def getDiscriminante(self):
        discriminante=self.b**2-4*self.a*self.c
        return discriminante
    
    def getRaiz1(self):
        discriminante=self.getDiscriminante()
        raiz1=(-self.b+math.sqrt(discriminante))/(2*self.a)
        return raiz1

    def getRaiz2(self):
        discriminante=self.getDiscriminante()
        raiz2=(-self.b-math.sqrt(discriminante))/(2*self.a)
        return raiz2
    
    def evaluar(self):
        eval=self.getDiscriminante()
        if eval>0:
            self.r1=self.getRaiz1()
            self.r2=self.getRaiz2()
            return self.r1, self.r2
        elif eval==0:
            self.r1=self.getRaiz1()
            return self.r1
        elif eval<0:
            return 0
        
    def __str__(self):
        eval=self.getDiscriminante()
        if eval>0:
            return f"la ecuacion tiene dos raices: {self.r1} y {self.r2}"
        elif eval==0:
            return f"la ecuacion tiene uan raiz: {self.r1}"
        elif eval<0:
            return f"la ecuacion no tiene raices reales"
    
a=1
b=-3
c=2

ecuacion= EcuacionCuadratica(a,b,c)
discriminante = ecuacion.getDiscriminante()
resultado=ecuacion.evaluar()
print(resultado)

print(ecuacion)
