#sample input:[1,-3,9,-2,7]
def sample_function_name(input_list):
    output_list = []
    #for i in range(0,len(input_list)):
    #   if input_list[i] >= 0:
    #        output_list.append(input_list([i] >= 0))
    for x in input_list:
        if x>=0:
            output_list.append(x)
    
    return output_list

print(sample_function_name([1,-3,9,-2,7]))






from random import randint

def roll_dice():
    return randint(1,20)
print(roll_dice())

def roll_dice(number,sides):
    result=0
    for i in range(0,number):
        result += randint(1,sides)
    return result

print(roll_dice(2,20))

def generate_new_character():
    # rolls six sets of 3d6 dice and supplies them as stats
    #in dictionary format
    character = {}
    character['STR'] = roll_dice(3,6)
    character['DEX'] = roll_dice(3,6)
    character['CON'] = roll_dice(3,6)
    character['WIS'] = roll_dice(3,6)
    character['INT'] = roll_dice(3,6)
    character['CHA'] = roll_dice(3,6)
    return character

new_character = generate_new_character()
print(new_character)

def generate_new_character2():
    character = {}
    stats = ['STR','DEX','CON','WIS','INT','CHA']

    for stat in stats:
        character[stat]=roll_dice(3,6)
    return character
new character=generate_new_character()
