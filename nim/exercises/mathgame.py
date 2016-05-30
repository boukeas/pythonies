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
