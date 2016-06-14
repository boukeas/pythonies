''' άσκηση από το http://pythonies.mysch.gr/chapters/nim.pdf

Τα παιδιά στο δημοτικό μαθαίνουν πρόσθεση μέσα από ασκήσεις αυξανό-
μενης δυσκολίας. Αρχικά, τους ζητείται να προσθέσουν δύο μονοψήφιους
αριθμούς, το άθροισμα των οποίων δεν ξεπερνά το 9.

Παράδειγμα: 4 + 2 = _

Μετά τους ζητείται να προσθέσουν δύο μονοψήφιους αριθμούς, το άθροι-
σμα των οποίων ξεπερνά το 10.

Παράδειγμα: 4 + 8 = _

Το επόμενο στάδιο είναι η πρόσθεση ενός διψήφιου κι ενός μονοψήφιου,
το άθροισμα των οποίων πιθανώς να ξεπερνά τη δεκάδα του διψήφιου,
αλλά όχι το 99.

Παράδειγμα: 42 + 9 = _

Μπορείτε να φτιάξετε ένα πρόγραμμα εξάσκησης για τα παιδιά του Δη-
μοτικού. Αρχικά, το πρόγραμμά σας θα πρέπει να ρωτά ποιο είναι το επι-
θυμητό επίπεδο ασκήσεων και να παράγει πέντε από αυτές. Εδώ έχουμε
περιγράψει τα τρία πρώτα επίπεδα, αλλά εσείς μπορείτε να φτιάξετε κι
άλλα ή ακόμα και να περάσετε σε άλλες πράξεις εκτός από την πρό-
σθεση. Μην σας απασχολεί αν καμιά φορά τυχαίνει να εμφανίζονται δι-
πλότυπες ασκήσεις, αυτό προς το παρόν είναι δύσκολο να το αποφύγετε.
'''

import random

def readlevel():
    """
    Ζητάει το επίπεδο δυσκολίας από τον χρήστη, κάνοντας έλεγχο ότι είναι στο διάστημα [1,5].
    Σε αντίθετη περίπτωση το ξαναζητάει μέχρι να δοθεί σωστή τιμή.
    """
    print("Δώσε επίπεδο δυσκολίας (1-5): ", end=" ")
    level = int(input())
    while level < 1 or level > 5:
        print("Δώσε επίπεδο δυσκολίας (1-5): ", end=" ")
        level = int(input())
    return level

def readcheckanswer(num1,num2):
    """
    Εμφανίζει την πράξη num1 + num2 στο χρήστη και ζητάει την απάντησή του. 
    Ο χρήστης έχει 3 ευκαιρίες το πολύ για ν' απαντήσει σωστά. 
    Σε διαφορετική περίπτωση εμφανίζεται η σωστή απάντηση.
    """
    print()
    print(num1,"+",num2,"=",end=" ")

    tries = 3
    found = False
    while tries > 0 and found == False:
        answer = int(input())
        tries = tries - 1
        if answer == num1 + num2:
            print("Μπράβο.")
            found = True
        else:
            if tries > 0:
                print("Προσπάθησε ξανά")
    if not found:
        print("Η σωστή απάντηση είναι", num1 + num2)

level = readlevel()
if level == 1:
    counter = 0
    while counter < 5:
        # μονοψήφιοι αριθμοί με άθροισμα μικρότερο του 10
        num1 = random.randint(1,8)
        num2 = random.randint(1,9 - num1)
        readcheckanswer(num1,num2)
        counter = counter + 1
elif level == 2:
    counter = 0
    while counter < 5:
        # μονοψήφιοι αριθμοί με άθροισμα μεγαλύτερο ή ίσο του 10
        num1 = random.randint(1,9)
        num2 = random.randint(10 - num1,9)
        readcheckanswer(num1,num2)
        counter = counter + 1
elif level == 3:
    counter = 0
    while counter < 5:
        # μονοψήφιος και διψήφιος αριθμός με άθροισμα μικρότερο του 100
        num2 = random.randint(1,9)
        num1 = random.randint(10,99 - num2)
        readcheckanswer(num1,num2)
        counter = counter + 1
elif level == 4:
    counter = 0
    while counter < 5:
        # διψήφιοι αριθμοί με άθροισμα μικρότερο του 100
        num1 = random.randint(10,98)
        num2 = random.randint(10,99 - num1)
        readcheckanswer(num1,num2)
        counter = cunter + 1
else:
    counter = 0
    while counter < 5:
        # διψήφιοι αριθμοί με άθροισμα μεγαλύτερο ή ίσο του 100
        num1 = random.randint(10,99)
        num2 = random.randint(100 - num1,99)
        readcheckanswer(num1,num2)
        counter = counter + 1   
