import random
# προτροπή για ρίψη ζαριών
print("Ρίξε τα ζάρια με ENTER...", end="")
input()
# τυχαίες τιμές για τα δύο ζάρια
dice1 = random.randint(1,6)
dice2 = random.randint(1,6)
# υπολογισμός και εμφάνιση ζαριάς
roll = dice1 + dice2
print("Έριξες", dice1, dice2, "=", roll)
# έλεγχος αποτελέσματος
if roll == 7 or roll == 11:
    # νίκη με την πρώτη
    print("Κέρδισες με την πρώτη!")
elif roll <= 3 or roll == 12:
    # ήττα με την πρώτη
    print("Έχασες με την πρώτη...")
else:
    # τίθεται ο "στόχος"
    print("Ξαναρίξε. Πρέπει να φέρεις", roll)
    # προτροπή για ρίψη ζαριών
    print("Ρίξε τα ζάρια με ENTER...", end="")
    input()
    # τυχαίες τιμές για τα δύο ζάρια
    dice1 = random.randint(1,6)
    dice2 = random.randint(1,6)
    # υπολογισμός και εμφάνιση ζαριάς
    roll = dice1 + dice2
    print("Έριξες", dice1, dice2, "=", roll)
