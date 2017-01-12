""" Ερωτικά σημειώματα
    
    Μια υλοποίηση σε Python 3 του προγράμματος "Loveletters" του
    Christopher Strachey (1952), με τροποποιήσεις για την 
    ελληνική γλώσσα.

    Βασίζεται στις αντίστοιχες υλοποιήσεις σε PHP και Python 2 από 
    τον Matt Sephton (gingerbeardman) και τον Nick Montfort, που 
    είναι διαθέσιμες στις διευθύνσεις:
    https://github.com/gingerbeardman/loveletter
    http://nickm.com/memslam/love_letters.py
    
    Περιγραφή, από το σύνδεσμο: 
    https://grandtextauto.soe.ucsc.edu/2005/08/01/christopher-strachey-first-digital-artist/

    Κάθε σημείωμα αποτελείται βασικά από 5 προτάσεις. Κάθε μια από
    αυτές είναι είτε "μεγάλη", είτε "σύντομη", με την επιλογή
    να γίνεται τυχαία, με πιθανότητα 50%. 

    Κάθε "μεγάλη" πρόταση έχει τη δομή: 
    
    <άρθρο> <επίθετο> <ουσιαστικό> μου <επίρρημα> <ρήμα> <άρθρο> <επίθετο> <ουσιαστικό> σου

    Κάθε "σύντομη πρόταση" έχει τη δομή:

    (Είσαι το) <επίθετο> <ουσιαστικό> μου

    Παρατηρήσεις:
    - Δύο σύντομες προτάσεις χωρίζονται με κόμμα. Σε κάθε άλλη 
    περίπτωση, δύο προτάσεις χωρίζονται με μια τελεία. 
    - Το "Είσαι το" χρησιμοποιείται στην αρχή μιας σύντομης πρότασης
    αν η προηγούμενη πρόταση ήταν μεγάλη.
    - Τα επίθετα και τα επιρρήματα δεν συμμετέχουν υποχρεωτικά σε
    κάθε μεγάλη πρόταση, η ύπαρξη καθενός από αυτά αποφασίζεται
    τυχαία, με πιθανότητα 50%. 

    Παρατηρήσεις σχετικές με την ελληνική γλώσσα:
    - Το γένος των άρθρων και των επιθέτων είναι το ίδιο με το γένος
    των ουσιαστικών που συνοδεύουν. Γι' αυτό όλα τα διαθέσιμα επίθετα
    προσδιορίζονται σε τρεις μορφές (τα τρία γένη) και τα ουσιαστικά
    συνοδεύονται από τα άρθρα του (ώστε να είναι γνωστό το γένος).
    - Στο δεύτερο σκέλος της μεγάλης πρότασης, το επίθετο και το
    ουσιαστικό είναι στην αιτιατική.

    Το σημείωμα ξεκινά από έναν χαιρετισμό δύο λέξεων και καταλήγει με
    την υπογραφή:

    Δικός σου <επίρρημα>, 
    M.U.C.

    όπου M.U.C. σημαίνει Manchester University Computer. Ο Strachey 
    αναρτούσε κρυφά αυτά τα σημειώματα στον πίνακα ανακοινώσεων
    του πανεπιστημίου, σύμφωνα με τον σύνδεσμο:
    http://www.alpha60.de/art/love_letters/

    Ο κώδικας που ακολουθεί, όπως και ο αρχικός PHP κώδικας του Matt
    Sephton, είναι διαθέσιμος με άδεια:
    Creative Commons Attribution-Share Alike 3.0 Unported License.

    Ο κώδικας του Nick Μοntfort είναι διαθέσιμος με την εξής άδεια:

    Love Letters, copyright (c) 2014 Nick Montfort <nickm@nickm.com>
    Original by Christopher Strachey, 1952
    
    Permission to use, copy, modify, and/or distribute this software
    for any purpose with or without fee is hereby granted, provided
    that the above copyright notice and this permission notice
    appear in all copies.
"""

import random

########## χαιρετισμοί, επίθετα, ουσιαστικά, επιρρήματα και ρήματα

# οι δύο  λέξεις που σχηματίζουν τον αρχικό χαιρετισμό
salutations1 = ["Αγαπημένο", "Γλυκό", "Αγαπητό", "Πολύτιμό", 
    "Μελένιο", "Φανταστικό"]
salutations2 = ["μπιζελάκι", "παπάκι", "κόσμημα", 
    "αγαπάκι", "ροδακινάκι", "αρκουδάκι"]

# επίθετα: η λίστα περιέχει και τα τρία γένη κάθε επιθέτου, για να
#   είναι εφικτός ο συνδυασμός με το ουσιαστικό που συνοδεύει
adjectives = [
    ("τρυφερός", "τρυφερή", "τρυφερό"),
    ("όμορφος", "όμορφη", "όμορφο"),
    ("καυτός", "καυτή", "καυτό"),
    ("παθιασμένος", "παθιασμένη", "παθιασμένο"),
    ("φλεγόμενος", "φλεγόμενη", "φλεγόμενο"),
    ("παράξενος", "παράξενη", "παράξενο"),
    ("πολύτιμος", "πολύτιμη", "πολύτιμο"),
    ("ενθουσιασμένος", "ενθουσιασμένη", "ενθουσιασμένο"),
    ("αγαπησιάρικος", "αγαπησιάρικη", "αγαπησιάρικο"),
    ("ακόρεστος", "ακόρεστη", "ακόρεστο"),
    ("ανικανοποίητος", "ανικανοποίητη", "ανικανοποίητο"),
    ("παρορμητικός", "παρορμητική", "παρορμητικό")]

# ουσιαστικά: η λίστα περιέχει και το άρθρο κάθε ουσιαστικού,
#   στην ονομαστική, για να φαίνεται το γένος του
nouns = ["η λατρεία", "η τρυφερότητα", "η φιλοδοξία", "η όρεξη", 
    "η ζέση", "το είναι", "η φωτιά", "η γοητεία", "ο πόθος", 
    "η επιθυμία", "η αφοσίωση", "η ανυπομονησία", "η μαγεία", 
    "ο ενθουσιασμός", "το γούστο", "η συμπάθεια", "η καρδιά", 
    "η πείνα", "η εμμονή", "το πάθος", "η έκρηξη", "η συμπάθεια", 
    "η δίψα", "η ευχή"]

# επιρρήματα
adverbs = ["τρυφερά", "με ενθουσιασμό", "ανυπόμονα", "όμορφα", 
    "φλεγόμενα", "παθιασμένα", "θερμά", "γλυκά", "με αγάπη", 
    "παθιάρικα", "αποπλανητικά", "απερίσκεπτα"]

# ρήματα
verbs = ["λατρεύει", "ελκύει", "εξυψώνει", "ελπίζει για",
    "αποζητάει", "λατρεύει", "πονάει για", "παθιάζεται για",
    "λαχανιάζει για", "αναστενάζει για", "βάζει σε πειρασμό", 
    "διψάει για", "πολιορκεί"]

########## συναρτήσεις που αποτυπώνουν γραμματικούς κανόνες

def finalni(word, nextWord):
    """ Επιστρέφει αυτούσια τη λέξη word όταν η λέξη nextWord
        αρχίζει από φωνήεν, τα γράμματα κ, π, τ, ξ και ψ ή τους
        δίφθογγους γκ, μπ, ντ, τζ, τσ. Σε κάθε άλλη περίπτωση
        επιστρέφει τη λέξη word χωρίς το τελευταίο της γράμμα.
        Χρησιμοποιείται για την πιθανή αφαίρεση του τελικού 'ν'.
    """
    if nextWord[0] in "αεηιουωκπτξψ":
        return word
    elif nextWord[0:2] in ("γκ", "μπ", "ντ", "τζ", "τσ"):
        return word
    else:
        return word[:-1]

def objective(article, noun):
    """ Επιστρέφει το άρθρο article και το ουσιαστικό noun, αφού
        τα μετατρέψει στην αιτιατική.
    """
    # έλεγχος γένους, με βάση το άρθρο 
    if article == "ο":
        # αρσενικό: αφαίρεση του τελικού 'ς'
        return "τον", noun[:-1]
    elif article == "η":
        # έλεγχος για αφαίρεση του τελικού 'ς' (π.χ. κιβωτός)
        if noun[-1] == "ς":
            noun = noun[:-1]
        # θηλυκό: ενδεχομενη αφαίρεση του τελικού 'ν'
        return finalni("την", noun), noun
    else:
        # ουδέτερο: καμία αλλαγή στην αιτιατική
        return "το", noun

########## συναρτήσεις επιλογής τυχαίων λέξεων

def select(alist, required = True):
    """ Επιλέγει τυχαία και επιστρέφει μια λέξη από μια λίστα 
        πιθανών λέξεων.
        
        alist: η λίστα από την οποία γίνεται η επιλογή
        required: αν είναι False, ενδέχεται να μην επιλεχθεί λέξη, 
            με πιθανότητα 50%
    """
    if required or random.randint(0,1):
        return random.choice(alist)
    else:
        return ""

def selectMatching(alist, article, required = True):
    """ Επιλέγει τυχαία και επιστρέφει μια λέξη από μια λίστα πιθανών
        λέξεων, έτσι ώστε αυτή να είναι συγκεκριμένου γένους.
        
        H λίστα πρέπει να περιέχει τριάδες από λέξεις, που 
        αντιστοιχούν στα τρία γένη, ώστε η συνάρτηση να επιστρέφει
        το γένος που ταιριάζει με το άρθρο που δίνεται ως παράμετρος.
        
        alist: η λίστα από την οποία γίνεται η επιλογή
        article: προσδιορισμός γένους με ένα από τα "ο", "η", "το"
        required: αν είναι False, ενδέχεται να μην επιλεχθεί λέξη, 
            με πιθανότητα 50%
    """
    if required or random.randint(0,1):
        # δείκτης που αντιστοιχεί σε ένα από τα τρία γένη,
        # ανάλογα με το άρθρο
        genre = {"ο": 0, "η": 1, "το": 2}[article]
        # τυχαία επιλογή μιας λέξης (τριάδα)
        word = random.choice(alist)
        # επιστροφή της λέξης, στο κατάλληλο γένος
        return word[genre]
    else:
        return ""

########## βοηθητικές συναρτήσεις

def spacing(word):
    """ Επιστρέφει μια άδεια συμβολοσειρά, αν η λέξη word είναι 
        κενή, διαφορετικά επιστρέφει ένα κενό. Χρησιμοποιείται για
        να υπολογιστεί αν χρειάζεται κενό πριν προαιρετική λέξη.
    """
    if word == "":
        return ""
    else:
        return " "

def capitalize(word):
    """ Επιστρέφει τη λέξη word με το πρώτο γράμμα κεφαλαίο. """
    return word[0].upper() + word[1:]

def extractArticle(fullnoun):
    """ Διασπά μια συμβολοσειρά που περιέχει ένα άρθρο και ένα 
        ουσιαστικό (στην ονομαστική) στα δύο συστατικά της.

        fullnoun: η συμβολοσειρά που θα διασπαστεί.
    """
    # η θέση του κενού (θεωρείται ότι έπεται του άρθρου)
    space = fullnoun.index(" ")
    # επιστρέφεται το άρθρο και η υπόλοιπη συμβολοσειρά
    return fullnoun[:space], fullnoun[space+1:]

########## συναρτήσεις κατασκευής προτάσεων

def salutation(loveletter):
    """ Προσθέτει έναν χαιρετισμό στο σημείωμα loveletter

        loveletter: Μια λίστα με τα συστατικά του σημειώματος
    """
    loveletter.extend([
        select(salutations1),
        " μου ",
        select(salutations2), 
        ",\n     "])

def longSentence(loveletter, startsWithPeriod):
    """ Προσθέτει στο σημείωμα loveletter μια "μεγάλη" πρόταση, 
        της μορφής:
        <άρθρο> <επίθετο> <ουσιαστικό> μου 
        <επίρρημα> <ρήμα> 
        <άρθρο> <επίθετο> <ουσιαστικό> σου

        loveletter: Μια λίστα με τα συστατικά του σημειώματος
        startsWithPeriod: Αν η προηγούμενη πρόταση τελειώνει με τελεία.
    """
    # τερματισμός προηγούμενης πρότασης με τελεία
    if startsWithPeriod:
        loveletter.append(". ")

    # επιλογή πρώτου ουσιαστικού (με άρθρο)
    fullnoun = select(nouns)
    article1, noun1 = extractArticle(fullnoun)
    # επιλογή πρώτου επιθέτου
    adjective1 = selectMatching(adjectives, article1, False)

    # επιλογή ρήματος και επιρρήματος
    adverb = select(adverbs, False)
    verb = select(verbs)

    # επιλογή δεύτερου ουσιαστικού (με άρθρο)
    fullnoun = select(nouns)
    article2, noun2 = extractArticle(fullnoun)
    # επιλογή δεύτερου επιθέτου
    adjective2 = selectMatching(adjectives, article2, False)
    # μετατροπή στην αιτιατική
    if adjective2 == "":
        article2, noun2 = objective(article2, noun2)
    else:
        __, noun2 = objective(article2, noun2)
        article2, adjective2 = objective(article2, adjective2)

    # προσθήκη μεγάλης πρότασης στο σημείωμα
    loveletter.extend([
        capitalize(article1), 
        spacing(adjective1), adjective1, 
        " ", noun1, " μου", 
        spacing(adverb), adverb, 
        " ", verb, 
        " ", article2, 
        spacing(adjective2), adjective2, 
        " ", noun2, " σου"])

def shortSentence(loveletter, startsWithPeriod):
    """ Προσθέτει στο σημείωμα loveletter μια σύντομη πρόταση, 
        της μορφής: 
        (Είσαι το) <επίθετο> <ουσιαστικό> μου

        loveletter: Μια λίστα με τα συστατικά του σημειώματος
        startsWithPeriod: Αν η προηγούμενη πρόταση τελειώνει με τελεία.
    """
    # σύνδεση πρότασης με την προηγούμενη
    if startsWithPeriod == None:
        # πρώτη πρόταση του σημειώματος, χωρίς στίξη
        loveletter.append("Είσαι ")
    elif startsWithPeriod:
        # κλείσιμο προηγούμενης πρότασης με τελεία
        loveletter.append(". Είσαι ")
    else:
        # συνέχεια προηγούμενης πρότασης με κόμμα
        loveletter.append(", ")

    # επιλογή ουσιαστικού (με άρθρο)
    fullnoun = select(nouns)
    article, noun = extractArticle(fullnoun)
    # επιλογή επιθέτου
    adjective = selectMatching(adjectives, article)

    # προσθήκη σύντομης πρότασης στο σημείωμα
    loveletter.extend([
        article, 
        " ", adjective, 
        " ", noun, " μου"])

def sign(loveletter):
    """ Προσθέτει στο σημείωμα loveletter μια υπογραφή.

        loveletter: Μια λίστα με τα συστατικά του σημειώματος
    """
    loveletter.extend([
        ".\n     Δικός σου ",
        select(adverbs),
        ",\n     M.U.C.\n"])


########## κύριο πρόγραμμα

# το σημείωμα, αρχικά κενό
loveletter = []

# χαιρετισμός
salutation(loveletter)

# αν η προηγούμενη πρόταση ήταν μεγάλη 
previousWasLong = None

# για κάθε μία από τις 5 προτάσεις
for sentence in range(5):
    # τυχαία επιλογή ανάμεσα σε μεγάλη ή σύντομη πρόταση    
    if random.randint(0,1):
        longSentence(loveletter, sentence > 0)
        previousWasLong = True
    else:
        # σύντομη πρόταση
        shortSentence(loveletter, previousWasLong)
        previousWasLong = False

# υπογραφή
sign(loveletter)

# δημιουργία σημειώματος από τη λίστα loveletter
# και εμφάνισή του
print("".join(loveletter), end = "")