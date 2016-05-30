import random
def rollDice():
    """ Ρίχνει δύο ζάρια και επιστρέφει 
    το άθροισμα των ενδείξεών τους.
    """
    # προτροπή για ρίψη ζαριών
    print("Ρίξε τα ζάρια με ENTER...", end="")
    input()
    # τυχαίες τιμές για τα δύο ζάρια
    dice1 = random.randint(1,6)
    dice2 = random.randint(1,6)
    # υπολογισμός και εμφάνιση ζαριάς
    roll = dice1 + dice2
    print("Έριξες", dice1, dice2, "=", roll)
    return roll
# ρίψη αρχικής ζαριάς
roll = rollDice()
# έλεγχος αποτελέσματος
if roll == 4 or roll == 7:
    # νίκη με την πρώτη
    print("Κέρδισες με την πρώτη!")
elif roll <= 3 or roll == 11:
    # ήττα με την πρώτη
    print("Έχασες με την πρώτη...")
else:
    # τίθεται το "σημείο"
    point = roll
    print("Πρέπει να φέρεις", point)
    # το παιχνίδι δεν έχει τελειώσει
    over = False
    # επανάληψη ρίψεων
    while not over:
        # ρίψη ζαριάς (επαναληπτική)
        roll = rollDice()
        # έλεγχος αποτελέσματος
        if roll == point:
            print("Κέρδισες!")
            # το παιχνίδι τελείωσε
            over = True
        elif roll == 7:
            print("Έχασες...")
            # το παιχνίδι τελείωσε
            over = True
