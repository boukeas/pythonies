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
# είσοδος ημερομηνίας από το χρήστη
print("Έτος: ", end="")
year = int(input())
print("Mήνας: ", end="")
month = int(input())
# επανάληψη, όσο η τιμή είναι εκτός ορίων
while month < 1 or month > 12:
    # μήνυμα λάθους
    print("Δώστε τιμή από 1 μέχρι 12")
    print("Mήνας: ", end="")
    month = int(input())
print("Ημέρα: ", end="")
day = int(input())
# κλήση υποπρογράμματος για υπολογισμό ημέρας
weekday = computeWeekday(day, month, year)
# εμφάνιση ημέρας της εβδομάδας (0:Κυριακή - 6:Σάββατο)
print("Ημέρα της εβδομάδας:", weekday)
