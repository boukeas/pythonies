import random
import itertools

class Game:
    """ Τα στιγμιότυπα της κλάσης Game αντιστοιχούν σε παιχνίδια τρίλιζας.

        Η κλάση δεν έχει data members, μόνο τη μέθοδο play που υλοποιεί την
        αλληλεπίδραση μεταξύ των παικτών και του πίνακα της τρίλιζας, σ' ένα
        παιχνίδι.

        Συγκεκριμένα κατά τη διάρκεια του παιχνιδιού:

        - καλείται η Player.select για να επιλέξει ο τρέχων παίκτης τη
          θέση στην οποία επιθυμεί να τοποθετήσει το σύμβολό του
        - καλείται η Board.__setitem__ για να τοποθετηθεί το σύμβολο
          του παίκτη στην επιλεγμένη θέση του πίνακα της τρίλιζας
        - καλείται η Player.inform για να ενημερωθεί ο αντίπαλος για
          την κίνηση που πραγματοποιήθηκε
    """

    def play(self, player1, player2):
        """ Πραγματοποίηση ενός παιχνιδιού: οι παίκτες εναλλάσσονται,
            συμπληρώνοντας με τη σειρά τους από ένα τετράγωνο στον πίνακα
            της τρίλιζας, μέχρι κάποιος να κερδίσει ή να συμπληρωθούν τα
            εννέα τετράγωνα.

            player1, player2: οι παίκτες που συμμετέχουν στο παιχνίδι.
        """
        # κάθε παίκτης ενημερώνεται για τον αντίπαλό του
        players = player2.opponent, player1.opponent = player1, player2

        # δημιουργείται ο πίνακας της τρίλιζας
        board = Board()
        # επανάληψη: οι δύο παίκτες εναλλάσσονται μεταξύ τους
        #   (θα διακοπεί όταν επιστραφεί με return το αποτέλεσμα)
        for player in itertools.cycle(players):

            # ο τρέχων παίκτης επιλέγει μια θέση
            position = player.select(board)
            # η θέση συμπληρώνεται από τον παίκτη επάνω στον πίνακα
            board[position] = player
            # οι παίκτες ενημερώνονται για την κίνηση
            player.opponent.inform(board, position)

            # έλεγχος
            if board.inarow(player):
                # αν έχει γίνει τρίλιζα από τον παίκτη που έπαιξε
                print("Τρίλιζα! Κέρδισε ο", player)
                # επιστρέφεται ο νικητής
                return player
            elif not board.nb_available:
                # αν ο πίνακας συμπληρώθηκε πλήρως
                print("Ισοπαλία.")
                # επιστρέφεται None
                return None


class Player:
    """ Τα στιγμιότυπα των υποκλάσεων της Player αντιστοιχούν σε παίκτες.
        Κάθε παίκτης χαρακτηρίζεται από το σύμβολό του (κατά κανόνα Χ ή Ο).

        Υλοποιώντας την abstract μέθοδο select σε μια υποκλάση της Player,
        περιγράφουμε τον τρόπο με τον οποίο ένα είδος παίκτη επιλέγει κάθε
        φορά τη θέση στην οποία θα παίξει.
    """

    def __init__(self, symbol):
        self.symbol = symbol

        # Τα αντικείμενα της κλάσης Player έχουν επίσης την ιδιότητα opponent,
        # γνωρίζουν δηλαδή τον αντίπαλό τους. Η ιδιότητα αυτή δεν υφίσταται
        # κατά τη δημιουργία του αντικειμένου (κατά την __init__), αλλά
        # δημιουργείται και παίρνει τιμή δυναμικά, όταν ο παίκτης συμμετέχει
        # σ' ένα παιχνίδι (δηλαδή όταν καλείται η μέθοδος Game.play.

    def __repr__(self):
        """ Επιστρέφει την αναπαράσταση του παίκτη, δηλ. το σύμβολό του.
            (χρησιμοποιείται για την print).
        """
        return self.symbol

    def select(self, board):
        """ Με δεδομένη την τρέχουσα κατάσταση του πίνακα board, επιλέγει το
            τετράγωνο στο οποίο θα παίξει ο παίκτης κι επιστρέφει τη θέση του.

            (abstract μέθοδος, πρέπει να υλοποιηθεί στις υποκλάσεις)
        """
        raise NotImplementedError(type(self).__name__ +
                                  ".select method needs to be implemented.")

    def inform(self, board, position):
        """
            (abstract μέθοδος, πρέπει να υλοποιηθεί στις υποκλάσεις)
        """
        raise NotImplementedError(type(self).__name__ +
                                  ".inform method needs to be implemented.")

    def can_win(self, board):
        """ Ελέγχει αν ο παίκτης player μπορεί να κερδίσει και επιστρέφει τη
            θέση στην οποία χρειάζεται να παίξει για να το καταφέρει.
            Ουσιαστικά, ελέγχει αν υπάρχει κάποια τριάδα θέσεων στην οποία ο
            παίκτης έχει καταλάβει δύο από τις τρεις θέσεις, και η θέση που
            απομένει είναι διαθέσιμη.

            Η μέθοδος αυτή συμπεριλήφθηκε στην abstract κλάση Player γιατί
            θεωρήθηκε ότι οποιοσδήποτε παίκτης του παιχνιδιού, όποιον τρόπο
            κι αν χρησιμοποιεί για να επιλέξει τη θέση που θα παίξει, θα πρέπει
            να έχει τη στοιχειώδη ικανότητα να πραγματοποιεί αυτόν τον έλεγχο.

            Συνήθως ένας παίκτης θα πρέπει να καλέσει αυτή τη μέθοδο τόσο για
            τον εαυτό του, όσο και για τον αντίπαλό του:

            self.can_win(board)
            self.opponent.can_win(board)
        """
        # για κάθε μια από τις τριάδες του πίνακα που σχηματίζουν τρίλιζα
        for p1, p2, p3 in Board.triples:
            # αν ο παίκτης έχει καταλάβει τις 2 από τις 3 θέσεις
            if board.is_available(p1) and board[p2] == board[p3] == self.symbol:
                return p1
            elif board.is_available(p2) and board[p1] == board[p3] == self.symbol:
                return p2
            elif board.is_available(p3) and board[p1] == board[p2] == self.symbol:
                return p3
        # αν φτάσουμε μέχρι εδώ, ο έλεγχος απέτυχε
        return None


class Board:
    """ Ένα στιγμιότυπο της κλάσης Board αντιστοιχεί στον πίνακα της τρίλιζας.

        Η κλάση περιέχει ορισμούς για τις μεθόδους __getitem__ και __setitem__,
        με τις οποίες παρέχει πρόσβαση στις θέσεις του πίνακα, χρησιμοποιώντας
        τις αγκύλες και το μοναδικό αναγνωριστικό κάθε θέσης.

        Επίσης, η κλάση παρέχει μεθόδους που αφορούν στις διαθέσιμες θέσεις του
        πίνακα και τον έλεγχο αν έχει γίνει τρίλιζα.
    """

    # Η πλειάδα positions καθορίζει τον τρόπο με τον οποίο μπορούμε
    # ν' αναφερθούμε σε κάθε θέση του πίνακα της τρίλιζας.
    # (η πλειάδα ανήκει στην κλάση, όχι στ' αντικείμενά της)
    positions = ("7", "8", "9",         # πρώτη γραμμή
                 "4", "5", "6",         # δεύτερη γραμμή
                 "1", "2", "3")         # τρίτη γραμμή

    # Η πλειάδα triples περιέχει τις 3άδες των θέσεων του πίνακα που
    # σχηματίζουν τρίλιζες.
    # (η πλειάδα ανήκει στην κλάση, όχι στ' αντικείμενά της)
    triples = ((positions[0], positions[1], positions[2]),  # 1η γραμμή
               (positions[3], positions[4], positions[5]),  # 2η γραμμή
               (positions[6], positions[7], positions[8]),  # 3η γραμμή
               (positions[0], positions[3], positions[6]),  # 1η στήλη
               (positions[1], positions[4], positions[7]),  # 2η στήλη
               (positions[2], positions[5], positions[8]),  # 3η στήλη
               (positions[0], positions[4], positions[8]),  # κ. διαγώνιος
               (positions[2], positions[4], positions[6]))  # δ. διαγώνιος

    def __init__(self):
        # η εσωτερική αναπαράσταση της τρίλιζας είναι ένα dict, στο οποίο
        # κάθε θέση αντιστοιχίζεται με το περιεχόμενό της
        self._squares = dict()
        self.nb_available = 9

    def __getitem__(self, position):
        """ Επιστρέφει το περιεχόμενο της θέσης position.
            (επιτρέπει την πρόσβαση στις θέσεις του πίνακα με τα [])
        """
        return self._squares.get(position, " ")

    def __setitem__(self, position, player):
        """ Συμπληρώνει τη θέση position με το σύμβολο του παίκτη player.
            (επιτρέπει την τροποποίηση των θέσεων του πίνακα με τα [])
        """
        self.nb_available -= 1
        self._squares[position] = player.symbol

    def __repr__(self):
        """ Επιστρέφει την αναπαράσταση της τρίλιζας
            (χρησιμοποιείται για την print).
        """
        return three_by_three(list(self[position]
                                   for position in Board.positions))

    def is_available(self, position):
        """ Ελέγχει αν η θέση position είναι κενή.
        """
        return self[position] == " "

    def available_positions(self):
        """ Επιστρέφει τις κενές θέσεις του πίνακα.
            (ουσιαστικά επιστρέφει έναν generator)
        """
        return (position for position in Board.positions
                if self.is_available(position))

    def inarow(self, player):
        """ Ελέγχει αν ο παίκτης player έχει κάνει τρίλιζα, δηλ. αν υπάρχει
            οποιαδήποτε τριάδα στην οποία ο παίκτης player έχει καταλάβει
            και τις τρεις θέσεις.
        """
        return any(self[p1] == self[p2] == self[p3] == player.symbol
                   for p1, p2, p3 in Board.triples)


"""
Υποκλάσεις της Player που υλοποιούν τη συμπεριφορά διαφορετικών παικτών.
"""

class Random(Player):
    """ Ένας παίκτης που επιλέγει κινήσεις τυχαία, εκτός κι αν μπορεί να κάνει
        τρίλιζα ή να εμποδίσει τρίλιζα του αντιπάλου.
    """

    def __init__(self, symbol):
        super().__init__(symbol)

    def select(self, board):
        """ Επιλέγει μια θέση στην οποία μπορεί να κάνει τρίλιζα, ή μια θέση
            στην οποια εμποδίζει τρίλιζα του αντιπάλου, ή μια τυχαία θέση σε
            διαφορετική περίπτωση.
        """
        # έλεγχος αν ο παίκτης μπορεί να κάνει τρίλιζα
        position = self.can_win(board)
        if position is not None:
            return position
        # έλεγχος αν ο αντίπαλος μπορεί να κάνει τρίλιζα
        position = self.opponent.can_win(board)
        if position is not None:
            return position
        # επιλογή μιας τυχαίας θέσης
        return random.choice(list(board.available_positions()))

    def inform(self, board, position):
        pass


class Human(Player):
    """ Ένας παίκτης που ζητάει από το χρήστη να επιλέξει κίνηση.
    """

    def __init__(self, symbol):
        super().__init__(symbol)

    def select(self, board):
        """ Επιστρέφει τη θέση που επιλέγει ο χρήστης, εξασφαλίζοντας
            με κατάλληλους ελέγχους ότι είναι έγκυρη.
        """
        while True:
            # εμφανίζονται στο χρήστη οι θέσεις στις οποίες μπορεί να παίξει
            # σε μορφή πίνακα τρίλιζας (για να φαίνεται η αντιστοιχία)
            print(three_by_three(list(position if board.is_available(position)
                                      else " " for position in Board.positions)), end="\n\n")
            # ο χρήστης επιλέγει θέση
            print(self.symbol, "διάλεξε τετράγωνο:", end=" ")
            position = input()
            # ελέγχεται αν η θέση είναι έγκυρη και διαθέσιμη
            if position not in Board.positions:
                print("Οι έγκυρες τιμές είναι:", ", ".join(sorted(board.available_positions())))
            elif not board.is_available(position):
                print("To", position, "δεν είναι κενό.")
            else:
                return position

    def inform(self, board, position):
        print("Ο παίκτης", self.opponent, "έπαιξε στη θέση", position, end=".\n\n")
        print(board, end="\n\n")


class Paper(Player):
    """ Ένας παίκτης που παίζει (απαραιτήτως) πρώτος με τα Χ και επιλέγει τις
        κινήσεις του σύμφωνα με τις οδηγίες του Έξυπνου Χαρτιού.

        Links:
            http://pythonies.mysch.gr/ipaper.pdf
            http://pythonies.mysch.gr/ipaper-ext.pdf
    """

    def __init__(self):
        super().__init__("X")

    @staticmethod
    def first_available(board):
        """ Επιστρέφει τη πρώτη κενή θέση του πίνακα board.
        """
        for position in Board.positions:
            if board.is_available(position):
                return position

    def select(self, board):
        """ Επιστρέφει την επόμενη κίνηση του Έξυπνου Χαρτιού.
        """
        nb_moves = (9 - board.nb_available) // 2
        if nb_moves == 0:
            # κίνηση 1η: πάνω αριστερά γωνία (θέση 0)
            return Board.positions[0]
        elif nb_moves == 1:
            # κίνηση 2η: κάτω δεξιά γωνία (θέση 8), αν
            # είναι διαθέσιμη, αλλιώς πάνω δεξιά (θέση 2)
            if board.is_available(Board.positions[8]):
                return Board.positions[8]
            else:
                return Board.positions[2]
        elif nb_moves < 4:
            # έλεγχος αν ο παίκτης μπορεί να κάνει τρίλιζα
            position = self.can_win(board)
            if position is not None:
                return position
            # έλεγχος αν ο αντίπαλος μπορεί να κάνει τρίλιζα
            position = self.opponent.can_win(board)
            if position is not None:
                return position
            # αλλιώς παίξε σε οποιαδήποτε γωνία
            for corner in (Board.positions[p] for p in (0, 2, 6, 8)):
                if board.is_available(corner):
                    return corner
        else:
            # κίνηση 5η: παίξε στο διαθέσιμο τετράγωνο
            return Paper.first_available(board)

    def inform(self, board, position):
        pass


"""
Βοηθητική συνάρτηση για την εμφάνιση του πίνακα της τρίλιζας.
"""

def three_by_three(iterable):
    """ Δέχεται σαν παράμετρο ένα iterable που έχει (τουλάχιστον) 9 στοιχεία
        και επιστρέφει ένα string στο οποίο τα στοιχεία είναι διατεταγμένα σε
        έναν πίνακα 3x3.

        Υποθέτει ότι τα στοιχεία έχουν μήκος 1. Αν αυτό δεν ισχύει, ο πίνακας
        δεν εμφανίζεται σωστά.
    """
    return (" " + " | ".join(iterable[0:3]) + "\n" +
            "-" * 3 + "+" + "-" * 3 + "+" + "-" * 3 + "\n" +
            " " + " | ".join(iterable[3:6]) + "\n" +
            "-" * 3 + "+" + "-" * 3 + "+" + "-" * 3 + "\n" +
            " " + " | ".join(iterable[6:9]))


"""
Το κύριο πρόγραμμα (αν δεν έχει γίνει import σαν βιβλιοθήκη): 
Δημιουργούνται δύο παίκτες και μετά ξεκινάει το παιχνίδι μεταξύ τους.
"""

if __name__ == "__main__":

    # ο παίκτης με τα Χ: το έξυπνο χαρτί
    player1 = Paper()
    # ο παίκτης με τα Ο: ένας άνθρωπος
    # τα τετράγωνα τα βλέπει αριθμημένα όπως στο αριθμητικό πληκτρολόγιο
    player2 = Human("O")

    # παίζεται ένα παιχνίδια ανάμεσα στους δύο παίκτες
    Game().play(player1, player2)
