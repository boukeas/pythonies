""" Ερωτικά σημειώματα
    
    Μια υλοποίηση σε Python 3 του προγράμματος "Loveletters" του
    Christopher Strachey (1952).

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
    
    My <επίθετο> <ουσιαστικό> <επίρρημα> <ρήμα> your <επίθετο> <ουσιαστικό>

    Κάθε "σύντομη πρόταση" έχει τη δομή:

    (You are) my <επίθετο> <ουσιαστικό

    Παρατηρήσεις:
    - Δύο σύντομες προτάσεις χωρίζονται με κόμμα. Σε κάθε άλλη 
    περίπτωση, δύο προτάσεις χωρίζονται με μια τελεία. 
    - Το "You are" χρησιμοποιείται στην αρχή μιας σύντομης πρότασης
    αν η προηγούμενη πρόταση ήταν μεγάλη.
    - Τα επίθετα και τα επιρρήματα δεν συμμετέχουν υποχρεωτικά σε
    κάθε μεγάλη πρόταση, η ύπαρξη καθενός από αυτά αποφασίζεται
    τυχαία, με πιθανότητα 50%. 

    Το σημείωμα ξεκινά από έναν χαιρετισμό δύο λέξεων και καταλήγει με
    την υπογραφή:

    Yours <επίρρημα>, 
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

# Οι δύο πρώτες λέξεις που σχηματίζουν τον αρχικό χαιρετισμό
salutations1 = ["Beloved", "Darling", "Dear", "Dearest", "Fanciful",
    "Honey"]
salutations2 = ["Chickpea", "Dear", "Duck", "Jewel", "Love", 
    "Moppet", "Sweetheart"]

# επίθετα
adjectives = ["affectionate", "amorous", "anxious", "avid",     
    "beautiful", "breathless", "burning", "covetous", "craving",
    "curious", "eager", "fervent", "fondest", "loveable", "lovesick", 
    "loving", "passionate", "precious", "seductive", "sweet",
    "sympathetic", "tender", "unsatisfied", "winning", "wistful"]

# ουσιαστικά
nouns = ["adoration", "affection", "ambition", "appetite", "ardour",
    "being", "burning", "charm", "craving", "desire", "devotion",
    "eagerness", "enchantment", "enthusiasm", "fancy", 
    "fellow feeling", "fervour", "fondness", "heart", "hunger",
    "infatuation", "little liking", "longing", "love", "lust",
    "passion", "rapture", "sympathy", "thirst", "wish", "yearning"]

# επιρρήματα
adverbs = ["affectionately", "ardently", "anxiously", "beautifully", 
    "burningly", "covetously", "curiously", "eagerly", "fervently",
    "fondly", "impatiently", "keenly", "lovingly", "passionately",
    "seductively", "tenderly", "wistfully"]

# ρήματα
verbs = ["adores", "attracts", "clings to", "holds dear", "hopes for",
    "hungers for", "likes", "longs for", "loves", "lusts after",
    "pants for", "pines for", "sighs for", "tempts", 
    "thirsts for", "treasures", "yearns for", "woos"]

########## συνάρτηση επιλογής τυχαίων λέξεων

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
       
########## βοηθητική συνάρτηση

def spacing(word):
    """ Επιστρέφει μια άδεια συμβολοσειρά, αν η λέξη word είναι 
        κενή, διαφορετικά επιστρέφει ένα κενό. Χρησιμοποιείται για
        να υπολογιστεί αν χρειάζεται κενό πριν από προαιρετική λέξη.
    """
    if word == "":
        return ""
    else:
        return " "

########## συναρτήσεις κατασκευής προτάσεων

def salutation(loveletter):
    """ Προσθέτει έναν χαιρετισμό στο σημείωμα loveletter

        loveletter: Μια λίστα με τα συστατικά του σημειώματος
    """
    loveletter.extend([
        select(salutations1), " ", 
        select(salutations2), 
        ",\n     "])

def longSentence(loveletter, startsWithPeriod):
    """ Προσθέτει στο σημείωμα loveletter μια "μεγάλη" πρόταση, 
        της μορφής:
        My <επίθετο> <ουσιαστικό> <επίρρημα> 
        <ρήμα> your <επίθετο> <ουσιαστικό>

        loveletter: Μια λίστα με τα συστατικά του σημειώματος
        startsWithPeriod: Αν η προηγούμενη πρόταση τελειώνει με τελεία.
    """
    # τερματισμός προηγούμενης πρότασης με τελεία
    if startsWithPeriod:
        loveletter.append(". ")

    # επιλογή πρώτου επιθέτου
    adjective1 = select(adjectives, False)
    # επιλογή πρώτου ουσιαστικού
    noun1 = select(nouns)

    # επιλογή ρήματος και επιρρήματος
    adverb = select(adverbs, False)
    verb = select(verbs)

    # επιλογή δεύτερου επιθέτου
    adjective2 = select(adjectives, False)
    # επιλογή δεύτερου ουσιαστικού
    noun2 = select(nouns)

    # προσθήκη μεγάλης πρότασης στο σημείωμα
    loveletter.extend([
        "My", 
        spacing(adjective1), adjective1, 
        " ", noun1, 
        spacing(adverb), adverb, 
        " ", verb, 
        " your",
        spacing(adjective2), adjective2, 
        " ", noun2])

def shortSentence(loveletter, startsWithPeriod):
    """ Προσθέτει στο σημείωμα loveletter μια σύντομη πρόταση, 
        της μορφής: 
        (You are) my <επίθετο> <ουσιαστικό

        loveletter: Μια λίστα με τα συστατικά του σημειώματος
        startsWithPeriod: Αν η προηγούμενη πρόταση τελειώνει με τελεία.
    """
    # σύνδεση πρότασης με την προηγούμενη
    if startsWithPeriod == None:
        # πρώτη πρόταση του σημειώματος, χωρίς στίξη
        loveletter.append("You are my")
    elif startsWithPeriod:
        # κλείσιμο προηγούμενης πρότασης με τελεία
        loveletter.append(". You are my")
    else:
        # συνέχεια προηγούμενης πρότασης με κόμμα
        loveletter.append(", my")

    # επιλογή επιθέτου
    adjective = select(adjectives)
    # επιλογή ουσιαστικού
    noun = select(nouns)

    # προσθήκη σύντομης πρότασης στο σημείωμα
    loveletter.extend([
        " ", adjective, 
        " ", noun])

def sign(loveletter):
    """ Προσθέτει στο σημείωμα loveletter μια υπογραφή.

        loveletter: Μια λίστα με τα συστατικά του σημειώματος
    """
    loveletter.extend([
        ".\n     Yours ",
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
