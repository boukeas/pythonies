import random
# αρχικό πλήθος σπίρτων
matches = random.randint(7,21)
# εμφάνιση αρχικού πλήθους σπίρτων
print("Αρχικό πλήθος σπίρτων:", matches)
# επανάληψη: συνεχίζεται μέχρι να μείνει ένα σπίρτο
while matches > 1:
    # ανάγνωση σπίρτων που θα πάρει ο παίκτης
    print("Πόσα σπίρτα θέλεις;")
    removed = int(input())
    # μείωση σπίρτων
    matches = matches - removed
    # εμφάνιση πλήθους σπίρτων που απομένουν
    print("Σπίρτα που απομένουν:", matches)

