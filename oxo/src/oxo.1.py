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
    # εμφάνιση πίνακα τρίλιζας και πιθανών κινήσεων
    print3x3(board)
    print3x3(range(9))
    # επιλογή θέσης από τον παίκτη
    print(player, "διάλεξε τετράγωνο:", end=" ")
    position = int(input())
    # ανακοίνωση κίνησης
    print("Ο παίκτης", player, "παίζει στο", position)
    # συμπλήρωση επιλεγμένης θέσης
    board[position] = player
    # μείωση κενών τετραγώνων κατά 1
    blank -= 1
    # έλεγχος για τρίλιζα:
    # για κάθε 3άδα θέσεων στις πιθανές τρίλιζες
    # ελέγχεται αν ο παίκτης έχει καταλάβει 3 θέσεις 
    if board[0] == board[1] == board[2] == player:
        inarow = True
    elif board[3] == board[4] == board[5] == player:
        inarow = True
    elif board[6] == board[7] == board[8] == player:
        inarow = True
    elif board[0] == board[3] == board[6] == player:
        inarow = True
    elif board[1] == board[4] == board[7] == player:
        inarow = True
    elif board[2] == board[5] == board[8] == player:
        inarow = True
    elif board[0] == board[4] == board[8] == player:
        inarow = True
    elif board[2] == board[4] == board[6] == player:
        inarow = True
    # εναλλαγή παίκτη
    if player == "X":
        player = "O"
    else:
        player = "X"
# εμφάνιση τελικού πίνακα τρίλιζας
print3x3(board)
# εμφάνιση αποτελέσματος
if inarow:
    print("Τρίλιζα!")
else:
    print("Ισοπαλία.")
