﻿# Ας ξεκινήσουμε εξηγώντας στον χρήστη τι κάνει το πρόγραμμά μας
print("Πόσο θα ζυγίζαμε αν κατοικούσαμε σε κάποιο άλλο ουράνιο σώμα;")
print("Ανακάλυψέ το για τη Σελήνη, τον Ήλιο και τον πλανήτη Αφροδίτη.")

# ερώτηση για το βάρος και μετατροπή του από αλφαριθμητικό σε ακέραιο αριθμό
print("Πόσα κιλά είσαι;", end=" ")
weight = int(input())

# υπολογισμός βάρους στα άλλα ουράνια σώματα, μετατροπή σε ακέραιο και
# αποθήκευση των αποτελεσμάτων σε κατάλληλες μεταβλητές
moon = int(weight/6)
sun = int(weight * 27.07)
venus = int(weight * 0.9)

# εμφάνιση των αποτελεσμάτων στην οθόνη
print("Το βάρος σου στη Γη είναι", weight, "κιλά.")
print("Το βάρος σου στη Σελήνη είναι", moon, "κιλά.")
print("Το βάρος σου στον Ήλιο είναι", sun, "κιλά.")
print("Το βάρος σου στην Αφροδίτη είναι", venus, "κιλά.")
