''' επέκταση από το από το http://pythonies.mysch.gr/chapters/planets.pdf

Μπορείτε να φτιάξετε ένα παιχνίδι με ερωτήσεις πολλαπλής επιλογής
που θα αφορούν τις ημέρες της εβδομάδας, αντί για τους πλανήτες, και
θα απευθύνεται σε παιδιά πρώτης δημοτικού.

Αυτό το πρόγραμμα χρησιμοποιεί τη "βιβλιοθήκη" multipleChoiceUtils
με τον κώδικα για τις ερωτήσεις πολλαπλής επιλογής που αναπτύχθηκε
στα πλαίσια αυτού του κεφαλαίου.
'''

import multipleChoiceUtils
import random
import time

def dayArticle(day):
    ''' Επιστρέφει το ή την ανάλογα με την ημέρα
    ώστε να εμφανίζεται σωστά το άρθρο
    day: η μέρα που θέλουμε το άρθρο της
    '''
    # αν είναι το Σάββατο
    if day == "Σάββατο":
        # επιστρέφει 'το' και το όνομα της ημέρας
        return "το "+day
    # διαφορετικά
    else:
        # επιστρέφει 'την' και το όνομα της ημέρας
        return "την "+day

def findWeekend(days):
    ''' Ζητά από τον παίκτη να βρει την ημέρα
    που ανήκει στο σαββατοκύριακο
    days: λίστα με τις ημέρες
    '''
    # λίστα με τις ημέρες Σάββατο - Κυριακή
    weekend = days[5:]
    # τυχαία επιλογή σωστής απάντησης
    correct = random.choice(weekend)
    # ερώτηση πολλαπλής επιλογής στον παίκτη
    print("Ποια από τις παρακάτω ημέρες δεν πηγαίνουμε σχολείο;", sep="")
    multipleChoiceUtils.multipleChoice(4, days[:5], correct)

def previousNextDay(days, count):
    ''' Εμφανίζει στον παίκτη μια ημέρα
    και τον ρωτά ποια είναι η προηγούμενή/επόμενη
    days: λίστα με τις ημέρες
    count: -1 ή +1 για την προηγούμενη/επόμενη μέρα
    '''
    # επιλογή τυχαίας ημέρας
    position = random.randint(0, len(days)-1)
    today = days[position]

    # υπολογισμός θέσης προηγούμενης/επόμενης
    correctPosition = (position + count) % 7
    correct = days[correctPosition]

    # αντίγραφο των ημερών
    daysCopy = days.copy()
    # που δεν περιέχει τη σημερινή ημέρα
    daysCopy.remove(today)

    # εμφάνιση λέξης πριν ή μετά
    if count == -1:
        word = "πριν"
    else:
        word = "μετά"

    # ερώτηση πολλαπλής επιλογής στον παίκτη
    print("Ποια ημέρα είναι", word, dayArticle(today), ";")
    multipleChoiceUtils.multipleChoice(4, daysCopy, correct)

def daysAfter(days):
    ''' Εμφανίζει στον παίκτη μια ημέρα
    και τον ρωτά ποια θα είναι η ημέρα
    μετά από έναν αριθμό ημερών
    days: λίστα με τις ημέρες
    '''
    # επιλογή τυχαίας ημέρας
    position = random.randint(0, len(days)-1)
    today = days[position]
    # επιλογή τυχαίου αριθμού ημερών
    count = random.randint(1, 7)

    # υπολογισμός μέρας μετά από count ημέρες
    correctPosition = (position + count) % 7
    correct = days[correctPosition]

    # ερώτηση πολλαπλής επιλογής στον παίκτη
    print("Αν σήμερα είναι", today)
    print("Τι ημέρα θα είναι σε", count, "ημέρες;")
    multipleChoiceUtils.multipleChoice(4, days, correct)

def daysBetween(days):
    ''' Εμφανίζει στον παίκτη δύο ημέρες
    και τον ρωτά πόσες ημέρες μεσολαβούν
    από τη μία στην άλλη
    days: λίστα με τις ημέρες
    '''
    # επιλογή πρώτης τυχαίας ημέρας
    first = random.randint(0, len(days)-1)
    # επιλογή δεύτερης τυχαίας ημέρας
    second = random.randint(0, len(days)-1)
    # έλεγχος ότι δεν είναι ίδιες
    while second == first:
        second = random.randint(0, len(days)-1)

    # έλεγχος αν η πρώτη είναι μεγαλύτερη
    if first > second:
        # βάλε την μικρότερη στην πρώτη και αντιστρόφως
        first, second = second, first

    # ερώτηση προς τον παίκτη
    print("Αν σήμερα είναι", days[second])
    print("Πόσες ημέρες έχουν περάσει από", dayArticle(days[first]), ";")

    # εισαγωγή απάντησης
    answer = int(input())
    # έλεγχος και εμφάνιση αποτελέσματος
    if answer == second - first:
        print("Μπράβο, το βρήκες")
    else:
        print("Η σωστή απάντηση είναι:", second-first)

def outOfOrder(days):
    ''' Καλεί τον παίκτη να βάλει στη σειρά
    τα ονόματα 4 διαδοχικών ημερών.
    days: λίστα με τις ημέρες
    '''
    # τυχαία επιλογή θέσης αρχικής ημέρας
    nbDays = len(days)
    start = random.randint(0, nbDays - 5)
    # δημιουργία λίστας 4 διαδοχικών ημερών
    fourDays = days[start : start + 4]
    # αντίγραφο της λίστας των 4 διαδοχικών ημερών
    shuffled = fourDays.copy()
    # ανακάτεμα των 4 ημερών σε τυχαίες θέσεις
    random.shuffle(shuffled)
    # ερώτηση στον παίκτη
    print("Βάλε τις ημέρες με τη σωστή σειρά:")
    multipleChoiceUtils.showMultiple(shuffled)
    print("\nΔώσε 4 αριθμούς με κενά ανάμεσά τους.")
    # η απάντηση "χωρίζεται" όπου υπάρχουν κενά
    # και τα συστατικά της τοποθετούνται σε μια λίστα
    answer = input().split()
    # λίστα που θα περιέχει την σωστή απάντηση
    correct = []
    # για κάθε μία από τις 4 διαδοχικές ημέρες
    for day in fourDays:
        # σειρά της ημέρας στην ανακατεμένη λίστα
        position = shuffled.index(day) + 1
        # προσθήκη σωστής σειράς στην απάντηση
        correct.append(str(position))
    # έλεγχος απάντησης
    if answer == correct:
        print("Μπράβο, η σειρά είναι σωστή.")
    else:
        print("Η σωστή σειρά είναι:")
        for n in correct:
            print(n, end=" ")
        print()

# λίστα με τις ημέρες της εβδομάδας
days = ["Δευτέρα", "Τρίτη", "Τετάρτη", "Πέμπτη", "Παρασκευή", "Σάββατο", "Κυριακή"]

# οδηγίες προς τον παίκτη
print("Παιχνίδι για να μάθεις τις ημέρες")
time.sleep(0.5)
print("Απάντησε στις ερωτήσεις που ακολουθούν")
time.sleep(0.5)
# εμφάνισε την πρώτη ημέρα της εβδομάδας
print("Η πρώτη ημέρα της εβδομάδας είναι", days[0])
time.sleep(0.5)
# εμφάνισε την τελευταία ημέρα της εβδομάδας
print("Η τελευταία ημέρα της εβδομάδας είναι", days[-1])
time.sleep(1)
print()
# ερώτηση για την ημέρα χωρίς σχολείο
findWeekend(days)
# ερώτηση για την προηγούμενη ημέρα
previousNextDay(days, -1)
# ερώτηση για την επόμενη ημέρα
previousNextDay(days, 1)
# ερώτηση για την ημέρα μετά από n ημέρες
daysAfter(days)
# ερώτηση για το πόσες ημέρες έχουν περάσει
daysBetween(days)
# εύρεση της σωστής σειράς των ημερών
outOfOrder(days)

