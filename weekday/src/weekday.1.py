# είσοδος ημερομηνίας από το χρήστη
print("Έτος: ", end="")
year = int(input())
print("Mήνας: ", end="")
month = int(input())
print("Ημέρα: ", end="")
day = int(input())
# υπολογισμός ημέρας με την μέθοδο του Gauss
# προσαρμογή μήνα και έτους 2 μήνες προς τα πίσω
if month > 2:
    month = month - 2
else:
    month = month + 10
    year = year - 1
# όρος για δίσεκτα έτη
leap = 5*(year%4) + 4*(year%100) + 6*(year%400)
# υπολογισμός ημέρας της εβδομάδας
weekday = (day + leap + int(2.6 * month - 0.2)) % 7
# εμφάνιση ημέρας της εβδομάδας (0:Κυριακή - 6:Σάββατο)
print("Ημέρα της εβδομάδας:", weekday)
