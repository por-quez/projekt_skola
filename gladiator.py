#importerar random
import random

#Karaktär Val 






#olika kropps attacker
class Attack:
    def __init__(self, namn, chans, skada):
        self.namn = namn
        self.chans = chans  # Träffprocent (0-100)
        self.skada = skada  # Hur mycket skada attacken gör

    def forsok_träffa(self):
        # Slumpmässigt tal mellan 1 och 100 avgör om attacken träffar
        return random.randint(1, 100) <= self.chans

# Definiera attacker
slag = Attack("Slag", 70, 10)  # 70% chans att träffa, gör 10 skada
spark = Attack("Spark", 60, 12)  # 60% chans att träffa, gör 12 skada
bitas = Attack("Bita", 50, 15)  # 50% chans att träffa, gör 15 skada
blinda = Attack("Blinda", 30, 5)  # 30% chans att träffa, gör 5 skada
kast = Attack("Kast", 10, 20)  # 10% chans att träffa, gör 20 skada

Attacker = Attack

