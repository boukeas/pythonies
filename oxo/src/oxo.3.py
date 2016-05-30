def print3x3(board, trailing = True):
    """ Εμφανίζει σε διάταξη 3x3 τα περιεχόμενα
        μιας λίστας με 9 (τουλάχιστον) στοιχεία.
        board: Λίστα που θα εμφανιστεί σε διάταξη 3χ3
    """
    print(" ", board[0], "|", board[1], "|", board[2])
    print(" ---+---+---")
    print(" ", board[3], "|", board[4], "|", board[5])
    print(" ---+---+---")
    print(" ", board[6], "|", board[7], "|", board[8])
    if trailing:
        print()
def readPosition(player, board):
    """ Διαβάζει από τον παίκτη τη θέση
        στην οποία επιθυμεί να παίξει και την
        επιστρέφει.
        player: Ο παίκτης που έχει σειρά να παίξει
        board: Μια λίστα με 9 στοιχεία (η τρίλιζα)
    """
    # εμφάνιση πίνακα τρίλιζας και πιθανών κινήσεων
    print3x3(board)
    print3x3(range(9))
    # επανάληψη: όσο το τετράγωνο δεν είναι έγκυρο
    while True:
        # επιλογή θέσης από τον παίκτη
        print(player, "διάλεξε τετράγωνο:", end=" ")
        position = int(input())
        # έλεγχος εγκυρότητας
        if position < 0 or position > 8:
            print("Επίλεξε τιμή μεταξύ 0 και 8.")
        elif board[position] != " ":
            print("To", position, "δεν είναι κενό.")
        else:
            # έγκυρη τιμή, τέλος επανάληψης
            break
    # επιστροφή επιλεγμένης θέσης
    return position
def play(player, pos, board):
    """ Πραγματοποιεί και ανακοινώνει την κίνηση
        ενός παίκτη σε συγκεκριμένη θέση
        player: Το σύμβολο του παίκτη
        pos: Η θέση στην οποία παίζει ο παίκτης
        board: Μια λίστα με 9 στοιχεία (η τρίλιζα)        
    """
    # ανακοίνωση κίνησης
    print("Ο παίκτης", player, "παίζει στο", pos)
    # συμπλήρωση επιλεγμένης θέσης
    board[pos] = player
def check(player, board):
    """ Ελέγχει αν υπάρχει 3άδα όπου ο παίκτης player
        έχει καταλάβει και τις 3 θέσεις.
        player: σύμβολο παίκτη ("Χ" ή "Ο")
        board: Μια λίστα με 9 στοιχεία (η τρίλιζα)    
    """
    # για κάθε 3άδα θέσεων στις πιθανές τρίλιζες
    # αν ο παίκτης έχει καταλάβει και τις 3 θέσεις 
    if board[0] == board[1] == board[2] == player:
        return True
    elif board[3] == board[4] == board[5] == player:
        return True
    elif board[6] == board[7] == board[8] == player:
        return True
    elif board[0] == board[3] == board[6] == player:
        return True
    elif board[1] == board[4] == board[7] == player:
        return True
    elif board[2] == board[5] == board[8] == player:
        return True
    elif board[0] == board[4] == board[8] == player:
        return True
    elif board[2] == board[4] == board[6] == player:
        return True
    else:
        # αν φτάσουμε μέχρι εδώ, ο έλεγχος απέτυχε
        return False
def next(player):
    """ Επιστρέφει το σύμβολο του παίκτη που παίζει
        μετά τον παίκτη με σύμβολο player.
        player: σύμβολο παίκτη ("Χ" ή "Ο")
    """
    if player == "X":
        return "O"
    else:
        return "X"
# η αναπαράσταση της τρίλιζας: 
# μια λίστα με 9 χαρακτήρες (" ", "Χ" ή "Ο")
# αρχικά, όλα τα τετράγωνα είναι κενά
board = 9 * [" "]
# ο παίκτης που θα παίξει πρώτος
player = "X"
# πλήθος τετραγώνων που απομένουν κενά
blank = 9
# λογική μεταβλητή που δείχνει αν έχει γίνει τρίλιζα
inarow = False
# επανάληψη: συνεχίζεται όσο υπάρχουν κενά τετράγωνα
#   και δεν έχει γίνει τρίλιζα
while blank > 0 and not inarow:
    # επιλογή θέσης από τον παίκτη
    position = readPosition(player, board)
    # συμπλήρωση επιλεγμένης θέσης
    play(player, position, board)
    # μείωση κενών τετραγώνων κατά 1
    blank -= 1
    # έλεγχος για τρίλιζα
    inarow = check(player, board)
    # εναλλαγή παίκτη
    player = next(player)
# εμφάνιση τελικού πίνακα τρίλιζας
print3x3(board)
# εμφάνιση αποτελέσματος
if inarow:
    print("Τρίλιζα! Κέρδισε ο", next(player))
else:
    print("Ισοπαλία.")
