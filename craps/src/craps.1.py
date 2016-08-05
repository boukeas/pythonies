import random
# τυχαίες τιμές για τα δύο ζάρια
dice1 = random.randint(1,6)
dice2 = random.randint(1,6)
# υπολογισμός και εμφάνιση ζαριάς
roll = dice1 + dice2
print("Έριξες", dice1, dice2, "=", roll)
