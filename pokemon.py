import math
import random
import pandas as pd
import pandasql as ps

class Pokemon:
  def __init__(self, name, type1, type2, hp, atk, dfn, spa, spd, spe, move1, move2, move3, move4):
    self.name = name
    self.type1 = type1
    self.type2 = type2
    self.hp = hp
    self.atk = atk
    self.dfn = dfn
    self.spa = spa
    self.spd = spd
    self.spe = spe
    self.move1 = move1
    self.move2 = move2
    self.move3 = move3
    self.move4 = move4

pokemon1 = Pokemon("Mewtwo", "Psychic", None, 322, 225, 185, 313, 185, 265, 'Thunderbolt', 'Ice Beam', 'Psystrike', 'Flamethrower')
pokemon2 = Pokemon("Arceus", "Normal", None, 350, 245, 245, 245, 245, 245, 'Earthquake', 'Shadow Claw', 'Judgment', 'Stone Edge')

def damageCalc(pokemon1, pokemon2, power):
    level = 100                # level is always 100
    random = damageRandom()    # random = random int between 85 and 100 inclusive, then divided by 100. decimals rounded down to nearest int
    STAB = 1                   # Same Type Attack Bonus (1.5)
    type = 1                   # type = type effectiveness
    critical = damageCrit(0)   # 1.5 for crit, 1/16
    attack = pokemon1.spa      # attacking stat
    defense = pokemon2.spd     # defending stat
  
    damage = ((((2 * level) / 5 + 2) * power * (attack / defense)) / 50 + 2) * critical * random * STAB * type      
    damage = damageRound(damage)
    
    if accuracy() == True:
        if critical == 1.5:
            print("A critical hit!")
        return damage
    return 0

def accuracy():
    accuracy = 100
    hit = random.randint(0, 100)
    if hit > accuracy:
        print("Miss!")
        return False
    return True    

def damageCrit(rate):
    ''' Default crit rate is 1/16'''

    if rate == 0:
        critchance = random.randint(0, 16)
    elif rate == 1:
        critchance = random.randint(0, 8)
    elif rate  == 2:
        critchance = random.randint(0, 4)
    elif rate == 3:
        critchance = random.randint(0, 3)
    elif rate >= 4:
        critchance = random.randint(0, 2)
   
    if (critchance == 1):
        return 1.5
    else:
        return 1

def damageRandom():
   ''' each move does anywhere from 85% to 100% of its damage'''
   
   num = random.randint(84, 100)/100
   return num

def damageRound(damage):
    if (damage -0.6 < math.floor(damage)):
        damage = math.floor(damage)
    else:
        damage = math.ceil(damage)
    return damage

def battleManager():
   while pokemon1.hp > 0 and pokemon2.hp > 0:
       pokemon1.hp-=1
       print(pokemon1.hp)
   return

def main():
    print('-----------------------------------')
    pokemon2currenthp = pokemon2.hp
    print(f'{pokemon1.name} used {pokemon1.move1}')
    damage = damageCalc(pokemon1, pokemon2, 90)
    if damage != 0:
        print(damage)
    pokemon2currenthp -= damage
    print(f"{pokemon2.name} {pokemon2currenthp}/{pokemon2.hp}")
    print('-----------------------------------')
    battleManager()

if __name__ == '__main__':
    main()
