'''
Το μόνο που θα τροποποιήσουμε σε αυτή την εκδοχή είναι ο τρόπος επιλογής
της κίνησης του υπολογιστή. Αντί να είναι τελείως τυχαία, όπως στην πρώτη έκδοση του παιχνιδιού, 
θα επιλέγει τυχαία με πιθανότητα 20%, ενώ με πιθανότητα 80% θα "κλέβει", λαμβάνοντας υπόψη 
την επιλογή του χρήστη.
'''

import random
import time

def randomchoice():
    """
    Επιλέγει τυχαία έναν αριθμό από το 1 μέχρι το 3 
    και θα αντιστοιχεί στα γράμματα Π, Ψ και Χ.
    """
    computerchoice = random.randint(1,3)
    if computerchoice == 1:
        return "Π"
    if computerchoice == 2:
        return "Ψ"
    if computerchoice == 3:
        return "Χ"

# μετρητής των συνολικών παιχνιδιών
games = 0
# μετρητής των παιχνιδιών που κέρδισε ο παίκτης
wins = 0

print("Θα παίξουμε Πέτρα - Ψαλίδι - Χαρτί.")

while True:
    print("Δώσε την επιλογή σου. (Π)έτρα, (Ψ)αλίδι, (Χ)αρτί ή οτιδήποτε άλλο για τερματισμό.")
    player = input()
    # αν ο παίκτης δώσει άλλο γράμμα εκτός από Π, Ψ ή Χ τότε τερματίζουμε άμεσα την επανάληψη με break
    if player != "Π" and player != "Ψ" and player != "Χ":
        break

    # επιλέγεται ένας τυχαίος αριθμός από το 1 μέχρι το 100
    cheatprobability = random.randint(1,100)
    # αν τύχει να είναι το πολύ 20, τότε η επιλογή είναι τυχαία
    if cheatprobability <= 20:
        computer = randomchoice()
    else:
        # ζαβολιά: επιλέγεται η κίνηση που κερδίζει την επιλογή του χρήστη (αίσχος)
        if player == "Π":
            computer = "Χ"
        elif player == "Ψ":
            computer = "Π"
        else:
            computer = "Ψ"

    print("O υπολογιστής διάλεξε", computer)

    # σύγκριση των επιλογών του παίκτη και του υπολογιστή και εμφάνιση κατάλληλου μηνύματος
    if computer == player:
        print("Ισοπαλία.")
    elif (player == "Π" and computer == "Ψ") or (player == "Ψ" and computer == "Χ") or (player == "Χ" and computer == "Π"):
        print("Κέρδισες!")
        wins = wins + 1
    else:
        print("Κέρδισε ο υπολογιστής :P")

    games = games + 1
    # εκτύπωσε 20 φορές τον χαρακτήρα "-"
    print(20 * "-")
    time.sleep(2)

print("Κέρδισες σε", wins, "από τα", games, "παιχνίδια.")
