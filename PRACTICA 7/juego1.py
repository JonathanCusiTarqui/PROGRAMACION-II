
import random
"""
class Juego:
    def __init__(self, numeroDeVidas):
        self.numeroDeVidas=numeroDeVidas
        self.record=0
    
    def reiniciaPartida(self):
        vidasIniciales=self.numeroDeVidas
        return vidasIniciales

    def actualizaRecord(self):
        if self.numeroDeVidas>0:
            record+=1
        else:
            record=0
        return self.record
        

    def quitaVida(self):
        if self.reiniciaPartida() > 0:
            self.numeroDeVidas-=1
            return True
        else:
            return False

class JuegoAdivinaNumero(Juego):
    def __init__(self, num_vidas):
        self.numeroAAdivinar=0
        super().__init__(num_vidas)

    def juega(self):
        super().reiniciaPartida()
        self.numeroAAdivinar=random.randint(0,10)
        print("adivine un numero entre cero y diez")
        
        while self.numeroDeVidas >0:
            
            entero= int(input("ingrese aqui: "))
            if entero==self.numeroAAdivinar:
                print("acertaste")
                super().actualizaRecord()
            elif entero!=self.numeroAAdivinar:
                super().quitaVida()
                print("el numero a adivinar es mayor o menor")
                print("intentelo de nuevo")
        else:
            print("ya no le quedan mas vidas")
        
class Aplicacion:
    
    def main():
        vidas=5
        play=JuegoAdivinaNumero(vidas)   
        play.juega() 

Aplicacion.main()


"""
class Juego:
    def __init__(self, numeroDeVidas):
        self.numeroDeVidas=numeroDeVidas
        self.record=0
    
    def reiniciaPartida(self):
        vidasIniciales=self.numeroDeVidas
        return vidasIniciales

    def actualizaRecord(self):
        if self.numeroDeVidas>0:
            self.record+=1
        else:
            self.record=0
        return self.record
        

    def quitaVida(self):
        if self.reiniciaPartida() > 0:
            self.numeroDeVidas-=1
            return True
        else:
            return False



class JuegoAdivinaNumero(Juego):
    def __init__(self, num_vidas):
        self.numeroAAdivinar=0
        super().__init__(num_vidas)
        


    def juega(self):
        super().reiniciaPartida()
        self.numeroAAdivinar=random.randint(0,3)
        print("adivine un numero entre cero y diez")
        
        while self.numeroDeVidas >0:
            
            entero= int(input("ingresa el numero: "))
            if JuegoAdivinaPar(entero)==True:
                print("felicidades adivinaste")
            else:
                super().quitaVida()
                print("intenta nuevamente")
        else:
            print("ya no le quedan mas vidas")
            #print(f"su record es: {super().actualizaRecord()}")
                  
    def validaNunmero(self, entero):
        if entero>=0 and entero<=3:
            return True
        else:
            return False
        
class JuegoAdivinaPar(JuegoAdivinaNumero):
    def __init__(self, num_vidas):
        super().__init__(num_vidas)

    def validaNumero(self, entero):
        if super().validaNumero(entero) and entero % 2 == 0:
            return True
        else:
            print("Error: El número debe ser par.")
            return False


class JuegoAdivinaImpar(JuegoAdivinaNumero):
    def __init__(self, num_vidas):
        super().__init__(num_vidas)

    def validaNumero(self, entero):
        if super().validaNumero(entero) and entero % 2 != 0:
            return True
        else:
            print("Error: El número debe ser impar.")
            return False


class Aplicacion:
    
    def main():
        vidas=4
        """"
        play=JuegoAdivinaNumero(vidas)   
        play.juega() 
        """
        play2=JuegoAdivinaPar(vidas)
        play2.juega()
        """
        play3=JuegoAdivinaImpar(vidas)
        play3.juega()"""

Aplicacion.main()