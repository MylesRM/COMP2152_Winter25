import random

weapons = ["Fist", "knife", "Club", "Gun", "Bomb", "Nuclear Bomb"]
print("Weapons: ", weapons)

def get_valid_int_input(prompt):
    while True:
        try:
            return int(input(prompt))
        except ValueError:
            print("Error: Please enter a valid integere!")
            continue
try:
    weapons_selected = get_valid_int_input("Enter the index of the weapon you like")
    # Roll dice
    weaponRoll = random.randint(1, 6)
    totalNum = weapons_selected + weaponRoll

    #Print the result based on the totalNum
    if weaponRoll <= 2:
        print("You rolled a weak weapon, friend.")
    elif weaponRoll <= 4:
        print("Yor weapon is moderate.")
    else:
        print("Nice weapon.")
except IndexError:
    print("Error: Please enter a weapon index")
except Exception as e:
    print(f"An unexpected error occurred: {e}")