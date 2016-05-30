import random

def selectMove(current, target):
    """ επιλέγει κι επιστρέφει την επόμενη κίνηση
        current: η τρέχουσα λίστα
        target: η λίστα "στόχος"
    """
    # ξεκίνα από την τελευταία θέση...
    index = len(current)-1
    # ... μέχρι να βρεις στοιχείο εκτός θέσης
    while index >= 0 and target[index] == current[index]:
        index -= 1
    # αν υπάρχει τέτοιο στοιχείο...
    if index >= 0:
        # ... βρες που βρίσκεται αυτό στην τρέχουσα λίστα
        next = current.index(target[index])
        if next == 0:
            # αν είναι στην πρώτη θέση, βάλτο στη θέση του
            return index+1
        else:
            # διαφορετικά, βάλτο στην πρώτη θέση
            return next+1
    else:
        # οι λίστες δεν διαφέρουν πουθενά, τέλος!
        return 0

def printlist(L):
    """ εμφανίζει σε μια γραμμή τα στοιχεία της λίστας L
    """
    for element in L:
        print(element, end=" ")
    print()

# η λίστα με τους (ταξινομημένους) αριθμούς από το 1 μέχρι το 9
ordered = [number for number in range(1,10)]
# ένα ανακατεμένο αντίγραφο της λίστας
numbers = ordered.copy()
random.shuffle(numbers)

# όσο η τρέχουσα λίστα δεν ταυτίζεται με την τελική
while numbers != ordered:
    # εμφάνιση τρέχουσας λίστας    
    printlist(numbers)
    # εμφάνιση υπόδειξης
    print("  » hint:", selectMove(numbers, ordered))
    # ανάγνωση της κίνησης του παίκτη
    count = int(input("Πόσοι αριθμοί να αντιστραφούν (2-9); "))
    if count < 2 or count > 9:
        print("Τέλος παιχνιδιού.")
        break
    # αντιστροφή των πρώτων count αριθμών της τρέχουσας λίστας
    # left = numbers[:count]
    # right = numbers[count:]
    # left.reverse()
    # numbers = left + right
    numbers = numbers[count-1::-1] + numbers[count:]
else:
    print("Τα κατάφερες")
