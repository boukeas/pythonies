import random

def newdeck():
    """ Κατασκευάζει κι επιστρέφει μια λίστα με τα χαρτιά της τράπουλας
        Η λίστα περιέχει μόνο αριθμούς από το 1 μέχρι και το 13
    """
    return 4 * [card for card in range(1,14)]

def face(card):
    """ Επιστρέφει την ένδειξη του χαρτιού card, δηλαδή Α, J, Q ή K 
        αν πρόκειται για άσο ή φιγούρα, διαφορετικά την αριθμητική του αξία.
    """
    if card == 1:
        return "A"
    elif card == 11:
        return "J"
    elif card == 12:
        return "Q"
    elif card == 13:
        return "K"
    else:
        return card

def printcards(cards):
    """ Εμφανίζει τις ενδείξεις των χαρτιών της λίστας cards.
    """
    for card in cards:
        print(face(card), end=" ")
    print()

def value(card):
    """ Επιστρέφει την αριθμητική αξία του χαρτιού card.
    """
    if card > 10:
        return 10
    else:
        return card

def deal(deck, cards, nbcards = 1):
    """ Μοιράζει χαρτιά από την τράπουλα στον παίκτη
        deck: η λίστα με τα χαρτιά της τράπουλας
        cards: τα χαρτιά του παίκτη
        nbcards: το πλήθος των χαρτιών που μοιράζονται
    """
    for card in range(nbcards):
        cards.append(deck.pop())

def maxvalue(value, nbaces):
    """ υπολογίζει κι επιστρέφει την μέγιστη αξία των χαρτιών του παίκτη
        value: το άθροισμα των χαρτιών του παίκτη
        nbaces: το πλήθος των άσων που έχει ο παίκτης
    """
    if nbaces > 0 and value + 10 <= 21:
        # υπάρχει άσος και μπορεί να μετρήσει για 11 χωρίς να "καεί" ο παίκτης
        return value + 10
    else:
        return value

# δημιουργία και ανακάτεμα τράπουλας
deck = newdeck()
random.shuffle(deck)

# η μάνα παίρνει δύο χαρτιά
dealer = []
deal(deck, dealer, 2)
# αξία χαρτιών και πλήθος άσων μάνας
dealervalue = value(dealer[0]) + value(dealer[1])
dealeraces = dealer.count(1)

print("Το ανοιχτό χαρτί της μάνας είναι:", face(dealer[1]))

# ο παίκτης παίρνει δύο χαρτιά
player = []
deal(deck, player, 2)
# αξία χαρτιών και πλήθος άσων παίκτη
playervalue = value(player[0]) + value(player[1])
playeraces = player.count(1)

print("Τα χαρτιά σου είναι:", end = " ")
printcards(player)

# όσο η μέγιστη αξία των χαρτιών του παίκτη είναι μικρότερη από 21
decisionvalue = maxvalue(playervalue, playeraces)
while decisionvalue < 21:
    print("Θέλεις κι άλλο χαρτί;", end = " ")
    answer = input().lower()
    if answer == "ν":
        # μοιράζεται άλλο ένα χαρτί
        deal(deck, player)
        newcard = player[-1]
        print("Τράβηξες", face(newcard))
        # υπολογίζεται η νέα μέγιστη αξία
        playervalue += value(newcard)
        if newcard == 1:
            playeraces += 1
        decisionvalue = maxvalue(playervalue, playeraces)
        # εμφάνιση χαρτιών
        print("Τα χαρτιά σου είναι:", end = " ")
        printcards(player)
    else:
        break

# αποτέλεσμα για παίκτη
playervalue = decisionvalue
if playervalue > 21:
    print("Κάηκες! Η αξία των χαρτιών σου είναι", playervalue)
    exit()
elif playervalue == 21:
    print("Blackjack!")
else:
    print("Η αξία των χαρτιών σου είναι", playervalue)

print("Τα χαρτιά της μάνας είναι:", end = " ")
printcards(dealer)

# όσο η μέγιστη αξία των χαρτιών της μάνας είναι μικρότερη από 21
decisionvalue = maxvalue(dealervalue, dealeraces)
while decisionvalue < 21:
    if decisionvalue < playervalue:
        # η μάνα τραβάει όσο υπολείπεται του παίκτη
        deal(deck, dealer)
        newcard = dealer[-1]
        print("Η μάνα τράβηξε", face(newcard))
        # υπολογίζεται η νέα μέγιστη αξία
        dealervalue += value(newcard)
        if newcard == 1:
            dealeraces += 1
        decisionvalue = maxvalue(dealervalue, dealeraces)
        # εμφάνιση χαρτιών
        print("Τα χαρτιά της μάνας είναι:", end = " ")
        printcards(dealer)
    else:
        break

# αποτέλεσμα παιχνιδιού
dealervalue = decisionvalue
if dealervalue > 21:
    print("Η μάνα κάηκε! Η αξία των χαρτιών της είναι", dealervalue)
    exit()
elif dealervalue == 21:
    print("Η μάνα έκανε Blackjack!")
else:
    print("Η μάνα σε κέρδισε με", dealervalue, "εναντίον του δικού σου", playervalue)

