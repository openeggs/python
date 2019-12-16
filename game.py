import random
wings = '#better wings#'
speed = '#faster#'
health = 0
strength = 0
stamina = 0
food = 30
water = 30
year = 0
exp = 0
level = 1
forty = 40
terain_list = ['land','water','air']
terain = input('''choose you scecies type:
land
water
air
''')
if terain == 'air':
    stamina += 20
    strength += 5
    health += 10
elif terain == 'water':
    stamina += 30
    strength += 10
    health += 20
else:
    stamina += 25
    strength += 10
    stamina += 15
if terain not in terain_list:
    print('error')
eats_list = ['carnivor','omnivor','herbevor' ]
eats = input('''what does it eat:
carnivor
omnivor
herbevor
''')
if eats not in eats_list:
    print('error')
if eats == 'carnivor':
    health += 50
    strength += 50
    stamina = 20
elif eats == 'herbevor':
    health += 50
    strength += 30
    stamina += 70
else:
    health += 50
    strength += 45
    stamina += 60

def skill_tree(terain,strength,stamina,food,water,health,wings,speed):
    skill_list = []
    if terain == 'air':
        skill = input('''
        
             | ''',speed,'''
        air -
             | ''',wings,''' -
        
''')
        if skill =='better wings' and wings == '#better wings#':
            print('''better wings mutated
stamina +10
strength +10
''')
            wings = 'better wings'
            strength += 10
            stamina += 10
            skill_list.append(skill)
        elif skill == 'faster' and speed == '#faster#':
            print('''faster flight mutated
stamina +15
strength +10
''')
            strength += 15
            stamina += 10
            skill_list.append(skill)
def migrate(food,water,stamina,health,strength):
    migrate = input('migrate y/n ')
    if migrate == 'y':
        if stamina > 80:
            reward = input('''you made it north
food + 20
water + 20

choose reward 
stamina +5
or
strength +5
    ''')
            if reward == 'strength':
                strength += 5
                print('strength is now ', strength)
            else:
                stamina += 5
                print('stamina is now ', stamina)
        else:
            print('''you failed to make it north
health -10
food -10
water - 10
    ''')
            health -= 10
            food -= 10
            water -= 10
            print('health is now ', health)
            print('food is now ', food)
            print('water is now ', water)
    else:
        print('''you don't migrate north
food -5
water -5
health -5
    ''')
        food -= 5
        water -= 5
        health -= 5
        print('health is now ', health)
        print('water is now ', water)
        print('food is now ', food)
def hibernate(food,water):
    hibernate = input('''hibernate y/n''')
    if hibernate == 'y':
        print(food - 40)
        if food > forty:
            print('''hibernation was sucesfull
food -5
water -5
''')
            food -= 5
            water -= 5
            print('food is now ',food)
            print('water is now ',water)
        else:
            if eats == 'omnivor':
                hunting = input('''hibernation is not possible
not enough food

hunt y/n
''')
                if hunting == 'y':
                    hunt(food,water,stamina)
                else:
                    game(stamina, strength, health, food, water, year,exp,level)
            elif eats == 'carnivor':
                hunting = input('''hibernation is not possible
not enough food

hunt y/n
''')
                if hunting == 'y':
                    hunt(food,water,stamina)
                else:
                    game(stamina, strength, health, food, water, year,exp,level)
            else:
                print('''hibernation is not possible
not enough food
''')
                game(stamina, strength, health, food, water, year,exp,level)
    else:
        game(stamina, strength, health, food, water, year,exp,level)
def forage(food,water):
    forage = input('forage y/n')
    if forage == 'y':
        print('''forage is sucessful
food +15
water +15
''')
        food += 15
        water += 15
        return food
        return water
        print('food is now ',food)
        print('water is now ',water)
    else:
        print('no forage\n')


def hunt(food,water,stamina):
    if 1 == 1:
        if strength > 55 and stamina > 75:
            print('''hunt is sucessful
food +20
stamina - 5
''')
            food += 20
            stamina -= 5
        else:
            print('hunt is unsucess ful\n')
            if eats == 'omnivor':
                forage(food,water)
    else:
        print('no hunt ')
        game(stamina, strength, health, food, water, year,exp,level)
def game(stamina, strength, health, food, water, year,exp,level):
    #random_encounter = random.randrange(1,2)
    if random_encounter == 1:
        if terain == 'air':
            if 1 == 1:
                migrate(food,water,stamina,health,strength)
            else:
                if eats == 'herbevor':
                    forage(water,food)
                else:
                    game(stamina,strength,health,food,water)
        if terain == 'land':
            hibernate(food,water)
        elif terain == 'water':
            if eats == 'herbevor':
                forage(food,water)
            elif eats == 'omnivor':
                hunt(stamina,food,water)
                forage(stamina,food,water)
            else:
                hunt(stamina,strength,health,food,water)
    elif random_encounter == '2':
        if 1 == 1:
            print('')
            year += 1
            if exp >= 100:
                level += 1
                print('level up, level is now ',level)
                skill_tree()

while True:
    random_encounter = random.randrange(1,3)
    game(stamina,strength,health,food,water,year,level,exp)
