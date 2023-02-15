import time
import numpy as np
import sys

# Print con delay
def print_con_delay(s):
    #print una letra a la vez como en pokemon XD
    for c in s:
        sys.stdout.write(c)
        sys.stdout.flush()
        time.sleep(0.05)

# Creando la clase
class Pokemon:
    def __init__(self, nombre, tipos, movimientos, EVs, puntos_de_salud='===================='):
        # Guarda las variables como atributos
        self.nombre = nombre
        self.tipos = tipos
        self.movimientos = movimientos
        self.ataque = EVs['ataque']
        self.defensa = EVs['defensa']
        self.puntos_de_salud = puntos_de_salud
        self.barras = 20 # Puntos de vida/salud
    

    def combate(self, Pokemon2):
        #Permite que dos Pokemon luchen entre ellos
        
        # Imprime información del combate
        print("-----BATALLA DE POKÉMON-----")
        print(f"\n{self.nombre}")
        print("tipo/", self.tipos)
        print("ataque/", self.ataque)
        print("defensa/", self.defensa)
        print("Nv./", 3*(1+np.mean([self.ataque,self.defensa])))
        print(f"\nVS")
        print(f"\n{Pokemon2.nombre}")
        print("tipo/", Pokemon2.tipos)
        print("ataque/", Pokemon2.ataque)
        print("defensa/", Pokemon2.defensa)
        print("Nv./", 3*(1+np.mean([Pokemon2.ataque,Pokemon2.defensa])))
        
        time.sleep(2)

        # Considera ventaja de tipos
        version = ['fuego', 'agua', 'planta']
        for i,k in enumerate(version):
            if self.tipos == k:
                    # Son el mismo tipo
                    if Pokemon2.tipos == k:
                        cadena_1_ataque = '\n'
                        cadena_2_ataque = '\n'
                        
                    # Pokemon2 es FUERTE
                    if Pokemon2.tipos == version[(i+1)%3]:
                        Pokemon2.ataque += 2
                        Pokemon2.defensa += 2
                        self.ataque /= 2
                        self.defensa /= 2
                        cadena_1_ataque = '\nNo es muy efectivo...'
                        cadena_2_ataque = '\n¡Es muy eficaz!'
                        
                    # Pokemon2 es DEBIL
                    if Pokemon2.tipos == version[(i+2)%3]:
                        self.ataque += 2
                        self.defensa += 2
                        Pokemon2.ataque /= 2
                        Pokemon2.defensa /= 2
                        cadena_1_ataque = '\n¡Es muy eficaz!'
                        cadena_2_ataque = '\nNo es muy efectivo...'    
                
                
    # Continua cuando pokemon siga con puntos_de_salud            
        while (self.barras > 0) and (Pokemon2.barras > 0):
            #Print los puntos_de_salud de cada Pokemon
            print(f"\n{self.nombre}\t\tPS\t{self.puntos_de_salud}")
            print(f"\n{Pokemon2.nombre}\t\tPS\t{Pokemon2.puntos_de_salud}\n")
                
            # TURNO POKEMON 1
            print(f"¡Adelante {self.nombre}!")
            for i, x in enumerate(self.movimientos):
                print(f"{i+1}.", x)
            index = int(input('Elige un movimiento: '))
            print_con_delay(f"\n¡{self.nombre} usó {self.movimientos[index-1]}!")
            time.sleep(1)
            print_con_delay(cadena_1_ataque)
                
            # Determina el daño
            Pokemon2.barras -= self.ataque
            Pokemon2.puntos_de_salud = ""
                
            # Agrega barras adicionales mas defensa boost
            for j in range (int(Pokemon2.barras+.1*Pokemon2.defensa)):
                Pokemon2.puntos_de_salud += "="
                    
            time.sleep(1)
            print(f"\n{self.nombre}\t\tPS\t{self.puntos_de_salud}")
            print(f"\n{Pokemon2.nombre}\t\tPS\t{Pokemon2.puntos_de_salud}\n")
            time.sleep(.5)
                
            # Comprueba si Pokemon se debilitó
            if Pokemon2.barras <= 0:
                print_con_delay(f"\n... {Pokemon2.nombre} se debilitó.")
                break
                
            # TURNO POKEMON 2
                
            print(f"¡Adelante {Pokemon2.nombre}!")
            for i, x in enumerate(Pokemon2.movimientos):
                print(f"{i+1}.", x)
            index = int(input('Elige un movimiento: '))
            print_con_delay(f"\n¡{Pokemon2.nombre} usó {Pokemon2.movimientos[index-1]}!")
            time.sleep(1)
            print_con_delay(cadena_2_ataque)
                
            # Determinar el daño
            self.barras -= Pokemon2.ataque
            self.puntos_de_salud = ""
                
            # Agregar barras adicionales mas defensa boost
            for j in range (int(self.barras+.1*self.defensa)):
                self.puntos_de_salud += "="
                    
            time.sleep(1)
            print(f"\n{Pokemon2.nombre}\t\tPS\t{Pokemon2.puntos_de_salud}")
            print(f"\n{self.nombre}\t\tPS\t{self.puntos_de_salud}\n")
            time.sleep(.5)
                
            # Comprueba si Pokemon se debilitó
            if self.barras <= 0:
                print_con_delay("\n..." + self.nombre + " se debilitó.")
                break
            
        money = np.random.choice(5000)
        print_con_delay(f"\nEl oponente te pagó ${money}.\n")        

if __name__ == '__main__':
    # Crear Pokemon
    Charizard = Pokemon('Charizard', 'fuego', ['Lanzallamas', 'Llamarada', 'Giro fuego' , 'Ascuas'],{'ataque': 12, 'defensa': 8})
    Blastoise = Pokemon('Blastoise', 'agua', ['Pistola de agua', 'Burbuja', 'Hidropulso' , 'Hidrobomba'],{'ataque': 10, 'defensa': 10})
    Venusaur = Pokemon('Venusaur', 'planta', ['Latigo Cepa', 'Hoja afilada', 'Rayo solar' , 'Abatidoras'],{'ataque': 8, 'defensa': 12})

    # Elige Pokemon1.combate(Pokemon2) para el demo
    Venusaur.combate(Charizard)
