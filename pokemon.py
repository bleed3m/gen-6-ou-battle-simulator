import math
import random
import pymysql

conn = pymysql.connect(
    host='localhost',
    user='root',
    password='lijlijlij',
    db='pokemon',
    charset='utf8mb4',
    cursorclass=pymysql.cursors.DictCursor
)

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

pokemon1 = Pokemon("Mewtwo", "psychic", None, 322, 225, 185, 313, 185, 265)
pokemon2 = Pokemon("Arceus", "normal", None, 350, 245, 245, 245, 245, 245)

def damageCalc(pokemon1, pokemon2, power):
    level = 100
    random = damageRandom()  # random = random int between 85 and 100 inclusive, then divided by 100. decimals rounded down to nearest int
    STAB = 1
    type = 1          # type = type effectiveness
    critical = damageCrit()  # 1.5 for crit decimals rounded down, 1/16
    attack = pokemon1.spa
    defense = pokemon2.spd
    
    damage = ((((2 * level) / 5 + 2) * power * (attack / defense)) / 50 + 2) * critical * random * STAB * type
    damage = damageRound(damage)

    return damage

def damageCrit():
   critchance = random.randint(1, 16)
   if (critchance == 1):
      print("A critical hit")
      return 1.5
   else:
      return 1

def damageRandom():
   num = random.randint(84, 100)/100
   return num

def damageRound(damage):
    if (damage -0.6 < math.floor(damage)):
        damage = math.floor(damage)
    else:
        damage = math.ceil(damage)
    return damage

damage = damageCalc(pokemon1, pokemon2, 90)
print(damage)
pokemon2.hp -= damage
print(f"{pokemon2.name} has {pokemon2.hp} HP left")
