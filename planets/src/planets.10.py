import random
def addPluto():
    ''' Ρωτά αν ο Πλούτωνας θα θεωρηθεί πλανήτης
    κι ανάλογα επιστρέφει την τιμή True ή False
    '''
    # ερώτηση στον παίκτη για τον Πλούτωνα
    print("Nα θεωρήσουμε τον Πλούτωνα πλανήτη (ν/ο);")
    answer = input()
    # επιστροφή τιμής ανάλογα με την aπάντηση
    return answer == "Ν" or answer == "ν"
def findByName(planets):
    ''' Εμφανίζει το όνομα ενός πλανήτη και ζητά 
    από τον παίκτη τη θέση του στο ηλιακό σύστημα.
    planets: λίστα με τα ονόματα όλων των πλανητών
    '''
    # επιλογή θέσης τυχαίου πλανήτη
    nbPlanets = len(planets)
    position = random.randint(0, nbPlanets - 1)
    # αναφορά στο όνομα του πλανήτη 
    # μέσω της θέσης του στη λίστα
    planet = planets[position]
    # ερώτηση στον παίκτη
    print("Σε ποια σειρά βρίσκεται ο πλανήτης ", 
          planet, " σε σχέση με τον Ήλιο;", sep = "")
    answer = int(input())
    # έλεγχος της απάντησης του παίκτη
    if answer == position + 1:
        # αν η απάντηση είναι σωστή
        print("Μπράβο, το βρήκες!")
    else:
        # εμφάνιση της σωστής απάντησης
        print("Ο πλανήτης ", planet, " είναι ο ", 
              position + 1, "ος πλανήτης.", sep = "")
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
def findByPosition(planets):
    ''' Εμφανίζει τη θέση ενός πλανήτη στο ηλιακό 
    σύστημα και ζητά από τον παίκτη το όνομά του.
    planets: λίστα με τα ονόματα όλων των πλανητών
    '''
    # επιλογή τυχαίου πλανήτη
    nbPlanets = len(planets)
    position = random.randint(0, nbPlanets - 1)
    planet = planets[position]
    # ερώτηση πολλαπλής επιλογής στον παίκτη
    print("Ποιος είναι ο ", position + 1,
          "ος πλανήτης μετά τον Ήλιο;", sep = "")
    multipleChoice(4, planets, planet)
def findByNeighbours(planets):
    ''' Ζητά από τον παίκτη να βρει έναν πλανήτη,
    εμφανίζοντας τους γειτονικούς του πλανήτες.
    planets: λίστα με τα ονόματα όλων των πλανητών
    '''
    # επιλογή τυχαίου πλανήτη
    nbPlanets = len(planets)
    position = random.randint(0, nbPlanets - 1)
    planet = planets[position]
    # πιθανές απαντήσεις: αντίγραφο λίστας πλανητών
    answers = planets.copy()
    # ερώτημα προς τον παίκτη
    print("Ποιος πλανήτης", end = " ")
    # έλεγχος για την ύπαρξη γειτόνων
    if position == 0:
        # υπάρχει μόνο επόμενος πλανήτης
        next = planets[position + 1]
        answers.remove(next)
        print("βρίσκεται πριν από τον πλανήτη ",
              next, ";", sep = "")
    elif position == nbPlanets - 1:
        # υπάρχει μόνο προηγούμενος πλανήτης
        previous = planets[position - 1]
        answers.remove(previous)
        print("βρίσκεται μετά από τον πλανήτη ",
              previous, ";", sep = "")
    else:
        # υπάρχουν και οι δύο γειτονικοί πλανήτες
        next = planets[position + 1]
        previous = planets[position - 1]
        answers.remove(next)
        answers.remove(previous)
        print("βρίσκεται ανάμεσα στους πλανήτες ",
              previous, " και ", next, ";", sep = "")
    # πολλαπλή επιλογή
    multipleChoice(4, answers, planet)
def closestSun(planets):
    ''' Εμφανίζει τα ονόματα 4 πλανητών και καλεί τον
    παίκτη να επιλέξει τον κοντινότερο στον Ήλιο.
    planets: λίστα με τα ονόματα όλων των πλανητών
    '''
    # επιλογή τυχαίου πλανήτη
    # εξαιρούνται οι τρεις τελευταίοι πλανήτες
    nbPlanets = len(planets)
    position = random.randint(0, nbPlanets - 4)
    planet = planets[position]
    # νέα λίστα με τις πιθανές απαντήσεις:
    # είναι οι πλανήτες από τον επιλεγμένο και μετά
    following = planets[position : ]
    # ερώτηση πολλαπλής επιλογής στον παίκτη
    print("Ποιος πλανήτης είναι πιο κοντά στον Ήλιο;")
    multipleChoice(4, following, planet)
def between(planets):
    ''' Εμφανίζει 4 πλανήτες, από τους οποίους μόνο 
    οι 3 αποτελούν τμήμα μιας διαδρομής. Καλεί τον
    παίκτη να επιλέξει τον 4ο "παράταιρο" πλανήτη.
    planets: λίστα με τα ονόματα όλων των πλανητών
    '''
    # τυχαία επιλογή αφετηρίας και τερματισμού
    nbPlanets = len(planets)
    start = random.randint(0, nbPlanets - 5)
    stop = random.randint(start + 4, nbPlanets - 1)
    # πλανήτες μεταξύ αφετηρίας και τερματισμού
    between = planets[start + 1 : stop]
    # υπόλοιποι πλανήτες
    out = planets[ : start] + planets[stop + 1 : ]
    # τυχαία επιλογή μιας σωστής απάντησης
    correct = random.choice(out)
    # ερώτημα προς τον παίκτη
    print("Ποιον πλανήτη δεν θα συναντήσουμε ",
          "ταξιδεύοντας από τον πλανήτη ", 
          planets[start], " στον πλανήτη ", 
          planets[stop], ";", sep = "")
    # πολλαπλή επιλογή
    multipleChoice(4, between + [correct], correct)
def outOfOrder(planets):
    ''' Καλεί τον παίκτη να βάλει στη σειρά
    τα ονόματα 4 διαδοχικών πλανητών.
    planets: λίστα με τα ονόματα όλων των πλανητών
    '''
    # τυχαία επιλογή θέσης αρχικού πλανήτη
    nbPlanets = len(planets)
    start = random.randint(0, nbPlanets - 5)
    # δημιουργία λίστας 4 διαδοχικών πλανητών
    fourPlanets = planets[start : start + 4]
    # αντίγραφο της λίστας των 4 διαδοχικών πλανητών
    shuffled = fourPlanets.copy()
    # ανακάτεμα των 4 πλανητών σε τυχαίες θέσεις
    random.shuffle(shuffled)
    # ερώτηση στον παίκτη
    print("Βάλε τους πλανήτες με τη σωστή σειρά:")
    showMultiple(shuffled)
    print("\nΔώσε 4 αριθμούς με κενά ανάμεσά τους.")
    # η απάντηση "χωρίζεται" όπου υπάρχουν κενά
    # και τα συστατικά της τοποθετούνται σε μια λίστα
    answer = input().split()
    # λίστα που θα περιέχει την σωστή απάντηση
    correct = []
    # για κάθε έναν από τους 4 διαδοχικούς πλανήτες
    for planet in fourPlanets:
        # σειρά του πλανήτη στην ανακατεμένη λίστα
        position = shuffled.index(planet) + 1
        # προσθήκη σωστής σειράς στην απάντηση
        correct.append(str(position))
    # έλεγχος απάντησης
    if answer == correct:
        print("Μπράβο, η σειρά είναι σωστή.")
    else:
        print("Η σωστή σειρά είναι:")
        print(correct)
# η λίστα με τα ονόματα όλων των πλανητών
planets = ["Ερμής", "Αφροδίτη", "Γη", "Άρης", "Δίας",
           "Κρόνος", "Ουρανός", "Ποσειδώνας"]
# ερώτηση για προσθήκη του Πλούτωνα
if addPluto():
    # προσάρτηση του Πλούτωνα στο τέλος της λίστας
    planets.append("Πλούτωνας")
# εύρεση του πλανήτη από το όνομα
print("\nΕρώτηση 1:")
findByName(planets)
# εύρεση του πλανήτη από τη θέση
print("\nΕρώτηση 2:")
findByPosition(planets)
# εύρεση του πλανήτη από τους γείτονές του
print("\nΕρώτηση 3:")
findByNeighbours(planets)
# εύρεση του κοντινότερου στον ήλιο
print("\nΕρώτηση 4:")
closestSun(planets)
# εύρεση του "παράταιρου" πλανήτη
print("\nΕρώτηση 5:")
between(planets)
# εύρεση της σωστής σειράς των πλανητών
print("\nΕρώτηση 6:")
outOfOrder(planets)
