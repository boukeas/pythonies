''' επέκταση από το από το http://pythonies.mysch.gr/chapters/planets.pdf

Μπορείτε να φτιάξετε ένα παιχνίδι με παρόμοιες ερωτήσεις πολλαπλής
επιλογής που θα αφορούν τους μήνες και τις εποχές, αντί για τους πλα-
νήτες, και θα απευθύνεται σε παιδιά πρώτης και δευτέρας δημοτικού.

Αυτό το πρόγραμμα χρησιμοποιεί τη "βιβλιοθήκη" multipleChoiceUtils
με τον κώδικα για τις ερωτήσεις πολλαπλής επιλογής που αναπτύχθηκε
στα πλαίσια αυτού του κεφαλαίου.
'''

import multipleChoiceUtils
import random
import time

def cutS(word):
    ''' Επιστρέφει τη λέξη χωρίς το τελευταίο της γράμμα. 
    Χρησιμοποιείται για να κόψει το τελικό ς
    word: η λέξη
    '''
    return word[:-1]

def findByName(months):
    ''' Εμφανίζει το όνομα ενός μήνα και 
    ζητά από τον παίκτη τη θέση του
    months: λίστα με τους μήνες
    '''
    # επιλογή θέσης τυχαίου μήνα
    nbMonths = len(months)
    position = random.randint(0, nbMonths - 1)
    # αναφορά στο όνομα του μήνα
    # μέσω της θέσης του στη λίστα
    month = months[position]
    # ερώτηση στον παίκτη
    print("Σε ποια σειρά βρίσκεται ο μήνας ", month, ";", sep = "")
    answer = int(input())
    # έλεγχος της απάντησης του παίκτη
    if answer == position + 1:
        # αν η απάντηση είναι σωστή
        print("Μπράβο, το βρήκες!")
    else:
        # εμφάνιση της σωστής απάντησης
        print("Ο μήνας ", month, " είναι ο ", 
              position + 1, "ος μήνας.", sep = "")

def findByPosition(months):
    ''' Εμφανίζει τη θέση ενός μήνα και 
    ζητά από τον παίκτη το όνομά του.
    months: λίστα με τους μήνες
    '''
    # επιλογή τυχαίου μήνα
    nbMonths = len(months)
    position = random.randint(0, nbMonths - 1)
    month = months[position]
    # ερώτηση πολλαπλής επιλογής στον παίκτη
    print("Ποιος είναι ο ", position + 1, 
          "ος μήνας του χρόνου;", sep = "")
    multipleChoiceUtils.multipleChoice(4, months, month)

def previousNextMonth(months, count):
    ''' Εμφανίζει στον παίκτη ένα μήνα
    και τον ρωτά ποιος είναι ο προηγούμενος/επόμενος
    months: λίστα με τους μήνες
    count: -1 ή +1 για τον προηγούμενο/επόμενο μήνα
    '''
    # επιλογή τυχαίου μήνα
    position = random.randint(0, len(months)-1)
    month = months[position]

    # υπολογισμός θέσης προηγούμενου/επόμενου
    correctPosition = (position + count) % 12
    correct = months[correctPosition]

    # αντίγραφο των μηνών
    monthsCopy = months.copy()
    # που δεν περιέχει τον μήνα
    monthsCopy.remove(month)

    # εμφάνιση λέξης πριν ή μετά
    if count == -1:
        word = "πριν"
    else:
        word = "μετά"

    # ερώτηση πολλαπλής επιλογής στον παίκτη
    print("Ποιος μήνας είναι ", word, " τον ", cutS(month), ";", sep="")
    multipleChoiceUtils.multipleChoice(4, monthsCopy, correct)

def smaller(months):
    ''' Εμφανίζει τα ονόματα 4 μηνών και καλεί τον παίκτη 
    να επιλέξει τον κοντινότερο στην αρχή του χρόνου.
    months: λίστα με τους μήνες
    '''
    # επιλογή τυχαίου μήνα
    # εξαιρούνται οι τρεις τελευταίοι μήνες
    nbMonths = len(months)
    position = random.randint(0, nbMonths - 4)
    month = months[position]
    # νέα λίστα με τις πιθανές απαντήσεις:
    # είναι οι μήνες από τον επιλεγμένο και μετά
    following = months[position : ]
    # ερώτηση πολλαπλής επιλογής στον παίκτη
    print("Ποιος μήνας είναι πιο κοντά στην αρχή του χρόνου;")
    multipleChoiceUtils.multipleChoice(4, following, month)

def outOfOrder(months):
    ''' Καλεί τον παίκτη να βάλει στη σειρά τα ονόματα 4 διαδοχικών μηνών.
    months: λίστα με τους μήνες
    '''
    # τυχαία επιλογή θέσης αρχικού μήνα
    nbMonths = len(months)
    start = random.randint(0, nbMonths - 5)
    # δημιουργία λίστας 4 διαδοχικών μηνών
    fourMonths = months[start : start + 4]
    # αντίγραφο της λίστας των 4 διαδοχικών μηνών
    shuffled = fourMonths.copy()
    # ανακάτεμα των 4 μηνών σε τυχαίες θέσεις
    random.shuffle(shuffled)
    # ερώτηση στον παίκτη
    print("Βάλε τους μήνες με τη σωστή σειρά:")
    multipleChoiceUtils.showMultiple(shuffled)
    print("\nΔώσε 4 αριθμούς με κενά ανάμεσά τους.")
    # η απάντηση "χωρίζεται" όπου υπάρχουν κενά
    # και τα συστατικά της τοποθετούνται σε μια λίστα
    answer = input().split()
    # λίστα που θα περιέχει την σωστή απάντηση
    correct = []
    # για κάθε έναν από τους 4 διαδοχικές μήνες
    for month in fourMonths:
        # σειρά του μήνα στην ανακατεμένη λίστα
        position = shuffled.index(month) + 1
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

def findBySeason(months, seasons):
    ''' Επιλέγει έναν τυχαίο μήνα και 
    ζητά από τον παίκτη να βρει σε ποια εποχή ανήκει
    months: λίστα με τους μήνες (ξεκινάει από το Δεκέμβρη)
    seasons: λίστα με τις εποχές
    '''
    # επιλογή τυχαίου μήνα
    position = random.randint(0, len(months)-1)
    month = months[position]

    # υπολογισμός αντίστοιχης εποχής, διαιρώντας τον αριθμό του μήνα με το 3
    correct = seasons[position // 3]
    # ερώτηση πολλαπλής επιλογής στον παίκτη
    print("Σε ποια εποχή ανήκει ο μήνας", month)
    multipleChoiceUtils.multipleChoice(4, seasons, correct)

def excludedMonth(months, seasons):
    ''' Επιλέγει τυχαία μια εποχή. Στη συνέχεια βρίσκει 
    τους μήνες που της αντιστοιχούν και επιλέγει τυχαία έναν
    ακόμα παράταιρο μήνα. Ζητά από τον παίκτη να βρει ποιος είναι
    months: λίστα με τους μήνες (ξεκινάει από το Δεκέμβρη)
    seasons: λίστα με τις εποχές
    '''
    # επιλογή τυχαίας εποχής
    position = random.randint(0, len(seasons)-1)
    season = seasons[position]

    # εύρεση αρχικού και τελικού μήνα της εποχής
    monthStart = position * 3
    monthEnd = monthStart + 3
    # λίστα με τα ονόματα των μηνων της εποχής
    inseason = months[monthStart:monthEnd]
    # λίστα με τα ονόματα των υπολοίπων μηνών
    outOfSeason = months[:monthStart] + months[monthEnd:]
    # τυχαία επιλογή παράταιρου μήνα
    correct = random.choice(outOfSeason)
    # προσάρτηση του μήνα στη λίστα των απαντήσεων
    inseason.append(correct)
    # ερώτηση πολλαπλής επιλογής στον παίκτη
    print("Ποιος μήνας δεν ανήκει στην εποχή ", season, ";", sep="")
    multipleChoiceUtils.multipleChoice(4, inseason, correct)

def excludedSeason(months, seasons):
    ''' Επιλέγει μια τυχαία εποχή. Στη συνέχεια επιλέγει
    από έναν μήνα για κάθε μία από τις 3 υπόλοιπες εποχές.
    Εμφανίζει τους παραπάνω μήνες και ζητάει από τον παίκτη
    να βρει την εποχή που δεν εκπροσωπείται.
    months: λίστα με τους μήνες (ξεκινάει από το Δεκέμβρη)
    seasons: λίστα με τις εποχές
    '''
    # επιλογή τυχαίας εποχής
    position = random.randint(0, len(seasons)-1)
    season = seasons[position]
    # λίστα με 1 μήνα ανά εποχή
    monthPerSeason = []

    # λίστα με τις θέσεις των εποχών, εξαιρουμένης της εποχής επιλέχθηκε αρχικά
    seasonsNumbers = [x for x in range(0, len(seasons)) if x != position]
    # για κάθε εποχή
    for s in seasonsNumbers:
        # επίλεξε έναν τυχαίο μήνα και προσάρτησε τον στη λίστα των μηνών που θα εμφανιστούν στον παίκτη
        monthPosition = random.randint(0, 2)
        monthPerSeason.append(months[s*3 + monthPosition])

    # ερώτηση πολλαπλής επιλογής στον παίκτη
    print("Ποια εποχή δεν εκπροσωπείται στους μήνες:", end=" ")
    for m in monthPerSeason:
        print(m, end=" ")
    print()
    multipleChoiceUtils.multipleChoice(4, seasons, season)


# λίστα με τα ονόματα των μηνών
months = ["Ιανουάριος", "Φεβρουάριος", "Μάρτιος", "Απρίλιος", "Μάϊος", "Ιούνιος", "Ιούλιος", "Αύγουστος", "Σεπτέμβριος", "Οκτώβριος", "Νοέμβριος", "Δεκέμβριος"]
# λίστα με τα ονόματα των εποχών
seasons = ["Χειμώνας", "Άνοιξη", "Καλοκαίρι", "Φθινόπωρο"]

# εύρεση μήνα από το όνομα
findByName(months)
# εύρεση μήνα από τη θέση
findByPosition(months)
# εύρεση προηγούμενου μήνα
previousNextMonth(months, -1)
# εύρεση επόμενου μήνα
previousNextMonth(months, +1)
# εύρεση κοντινότερου στην αρχή του έτους
smaller(months)
# εύρεση σωστής σειράς μηνών
outOfOrder(months)

# λίστα μηνών που ξεκινούν από το Δεκέμβρη, ώστε να ταιριάζουν με τις αντίστοιχες εποχές
months = [months[-1]] + months[:-1]

# εύρεση εποχής από τον μήνα
findBySeason(months, seasons)
# εύρεση παράταιρου μήνα
excludedMonth(months, seasons)
# εύρεση παράταιρης εποχής
excludedSeason(months, seasons)
