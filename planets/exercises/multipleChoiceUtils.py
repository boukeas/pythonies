''' βοηθητική βιβλιοθήκη από το http://pythonies.mysch.gr/chapters/planets.pdf

Αυτή η βιβλιοθήκη περιέχει τον κώδικα για τις ερωτήσεις 
πολλαπλής επιλογής που αναπτύχθηκε στα πλαίσια αυτού του κεφαλαίου.
'''

import random

def select(nbChoices, possible, correct):
    ''' Επιλέγει από τη λίστα πιθανών απαντήσεων
    ένα ορισμένο πλήθος και τις επιστρέφει σε λίστα.
    nbChoices: πλήθος απαντήσεων που θα επιλεχθούν
    possible: λίστα όλων των πιθανών απαντήσεων,
        πρέπει len(possible) >= nbChoices
    correct: η σωστή απάντηση
    '''
    # διάλεξε τυχαία απαντήσεις
    answers = random.sample(possible, nbChoices)
    # αν η σωστή απάντηση δεν υπάρχει στη λίστα
    if correct not in answers:
        # διάλεξε τυχαία θέση για την σωστή απάντηση
        index = random.randint(0, nbChoices - 1)
        # εισαγωγή της σωστής απάντησης στη λίστα
        answers[index] = correct
    # επιστροφή λίστας απαντήσεων
    return answers

def showMultiple(answers):
    ''' Εμφανίζει αριθμημένες τις πιθανές απαντήσεις
    μιας ερώτησης, σε στυλ πολλαπλής επιλογής.
    answers: λίστα απαντήσεων
    '''
    number = 1
    # σάρωση λίστας πιθανών απαντήσεων
    for answer in answers:
        print("(", number, ") ", answer,
              sep = "", end = " ")
        number = number + 1

def readAnswer(nbChoices):
    ''' Zητάει την απάντηση του παίκτη,
    μέχρι να είναι έγκυρη, και την επιστρέφει.
    nbChoices: πλήθος έγκυρων απαντήσεων
    '''
    # επανάληψη: μέχρι να δοθεί έγκυρη απάντηση
    while True:
        # ανάγνωση απάντησης
        choice = int(input())
        # έλεγχος εγκυρότητας
        if choice < 1 or choice > nbChoices:
            print("Επίλεξε μια έγκυρη απάντηση",
                  "από 1 μέχρι", nbChoices, sep = "")
        else:
            break
    # η απάντηση επιστρέφεται
    return choice

def multipleChoice(nbChoices, possible, correct):
    ''' Ερώτηση πολλαπλής επιλογής: εμφανίζει τις
    πιθανές απαντήσεις, ζητάει την επιλογή του παίκτη
    και ελέγχει αν είναι σωστή ή λανθασμένη.
    nbChoices: πλήθος απαντήσεων που θα εμφανιστούν
    possible: λίστα όλων των πιθανών απαντήσεων
    correct: η σωστή απάντηση
    '''
    # επιλογή απαντήσεων
    answers = select(nbChoices, possible, correct)
    # προβολή απαντήσεων
    showMultiple(answers)
    # ανάγνωση έγκυρης απάντησης
    playerChoice = readAnswer(nbChoices)
    # έλεγχος και εμφάνιση αποτελέσματος
    if answers[playerChoice - 1] == correct:
        print("Μπράβο, το βρήκες!")
    else:
        print("H σωστή απάντηση είναι: ",
              correct, ".", sep = "")
