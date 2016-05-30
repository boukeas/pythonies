def computeWeekday(day, month, year):
    """ Υπολογίζει με την μέθοδο του Gauss 
    την ημέρα της εβδομάδας στην οποία αντιστοιχεί
    μια συγκεκριμένη ημερομηνία.
    day, month, year: ορίζει την ημερομηνία 
    """
    # προσαρμογή μήνα και έτους 2 μήνες προς τα πίσω
    if month > 2:
        month = month - 2
    else:
        month = month + 10
        year = year - 1
    # όρος για δίσεκτα έτη
    leap = 5*(year%4) + 4*(year%100) + 6*(year%400)
    # υπολογισμός κι επιστροφή ημέρας της εβδομάδας
    return (day + leap + int(2.6 * month - 0.2)) % 7
def readInt(prompt,lower,upper):
    """ Εμφανίζει μια προτροπή και μετά διαβάζει 
    από το χρήστη κι επιστρέφει έναν ακέραιο αριθμό,
    εξασφαλίζοντας ότι βρίσκεται εντός ορίων.
    prompt: η προτροπή που εμφανίζεται στο χρήστη
    lower, upper: τα όρια
    """
    # εμφάνιση προτροπής και ανάγνωση τιμής
    print(prompt, end="")
    num = int(input())
    # επανάληψη, όσο η τιμή είναι εκτός ορίων
    while num < lower or num > upper:
        # μήνυμα λάθους
        print("Δώστε τιμή από",lower,"μέχρι",upper)
        # εμφάνιση προτροπής και ανάγνωση τιμής
        print(prompt, end="")
        num = int(input())
    # η έγκυρη τιμή επιστρέφεται
    return num
def isLeap(year):
    """ Επιστρέφει την τιμή True αν το έτος year
    είναι δίσεκτο, αλλιώς επιστρέφει False.
    """
    return ((year % 4 == 0 and year % 100 > 0) or
           year % 400 == 0)
def daysOfMonth(m,y):
    """ Επιστρέφει το πλήθος των ημερών ενός μήνα.
    m: ο αριθμός του μήνα (1-12)
    y: ο αριθμός του έτους (απαραίτητο όταν m=2)
    """
    if m == 2:      
        # Φεβρουάριος
        if isLeap(y):
            return 29
        else:
            return 28
    elif m <= 7:    
        # Ιανουάριος - Ιούλιος (πλην Φεβρουαρίου)
        if m % 2 == 1:
            return 31
        else:
            return 30
    else:           
        # Αύγουστος - Δεκέμβριος
        if m % 2 == 1:
            return 30
        else:
            return 31
# είσοδος ημερομηνίας από το χρήστη
year = readInt("Έτος: ", 1923, 2999)
month = readInt("Mήνας: ", 1, 12)
day = readInt("Ημέρα: ", 1, daysOfMonth(month,year))
# πλειάδα με τα ονόματα των ημερών
dayNames = ('Κυρ','Δευ','Τρι','Τετ','Πεμ','Παρ','Σαβ')
# κλήση υποπρογράμματος για υπολογισμό ημέρας
weekday = computeWeekday(day, month, year)
# εμφάνιση ημέρας της εβδομάδας (0:Κυριακή - 6:Σάββατο)
print("Ημέρα της εβδομάδας:", dayNames[weekday])
