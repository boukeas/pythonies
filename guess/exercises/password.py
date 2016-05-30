'''
    Πρόγραμμα ελέγχου συνθηματικού
'''

secret = "43215678"
tries = 3
found = False

while not found and tries > 0:
    print("Απομένουν",tries,"προσπάθειες")
    tries = tries - 1
    print("Δώσε το συνθηματικό")
    userpwd = input()

    if secret == userpwd:
        print("Καλώς ήρθες")
        found = True
    else:
        print("Λάθος.")

if not found:
    print("Εξάντλησες όλες σου τις προσπάθειες")