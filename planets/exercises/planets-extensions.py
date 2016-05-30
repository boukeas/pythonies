import random

planets = ["Ερμής","Αφροδίτη","Γη","Άρης","Δίας","Κρόνος","Ουρανός","Ποσειδώνας"]

def addPluto():
    ''' Ρωτά αν ο Πλούτωνας θα θεωρηθεί πλανήτης
    κι ανάλογα επιστρέφει την τιμή True ή False
    '''
    answers = ["ν","ναι"]
    # ερώτηση στον παίκτη για τον Πλούτωνα
    print("Nα θεωρήσουμε τον Πλούτωνα πλανήτη (ν/ο);")
    answer = input().lower()
    # επιστροφή τιμής ανάλογα με την aπάντηση
    return answer in answers

def select(nbChoices, possible, correct):
    ''' Επιλέγει από τη λίστα πιθανών απαντήσεων
    ένα ορισμένο πλήθος και τις επιστρέφει σε λίστα.
    nbChoices: πλήθος απαντήσεων που θα επιλεχθούν
    possible: λίστα όλων των πιθανών απαντήσεων,
        πρέπει len(possible) >= nbChoices
    correct: η σωστή απάντηση
    '''

    answers = []
    # μέχρι να συμπληρωθούν όλες οι απαντήσεις στη λίστα
    while len(answers) < nbChoices:
        # επέλεξε τυχαία μια ακόμα απάντηση
        answer = random.choice(possible)
        # αν δεν υπάρχει στη λίστα των απαντήσεων
        if answer not in answers:
            # προσάρτησέ την στη λίστα
            answers.append(answer)

    # αν η σωστή απάντηση δεν υπάρχει στη λίστα
    if correct not in answers:
        # διάλεξε τυχαία θέση για την σωστή απάντηση
        index = random.randint(0, nbChoices - 1)
        # εισαγωγή της σωστής απάντησης στη λίστα
        answers[index] = correct
    # επιστροφή λίστας απαντήσεων
    return answers

def selectSlice(nbChoices, possible, correct):
    ''' Επιλέγει από τη λίστα πιθανών απαντήσεων
    ένα ορισμένο πλήθος και τις επιστρέφει σε λίστα.
    nbChoices: πλήθος απαντήσεων που θα επιλεχθούν
    possible: λίστα όλων των πιθανών απαντήσεων,
        πρέπει len(possible) >= nbChoices
    correct: η σωστή απάντηση
    '''

    # φτιάξε ένα αντιγραφό των πιθανών απαντήσεων
    answers = possible.copy()
    # ανακάτεψέ το
    random.shuffle(answers)
    # τεμάχισε το, ώστε να περιλαμβάνει τον επιθυμητό αριθμό στοιχείων
    answers = answers[:nbChoices]

    # αν η σωστή απάντηση δεν υπάρχει στη λίστα
    if correct not in answers:
        # διάλεξε τυχαία θέση για την σωστή απάντηση
        index = random.randint(0, nbChoices - 1)
        # εισαγωγή της σωστής απάντησης στη λίστα
        answers[index] = correct
    # επιστροφή λίστας απαντήσεων
    return answers

