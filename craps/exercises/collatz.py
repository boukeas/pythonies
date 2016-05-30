﻿print("Η εικασία του Collatz.")
print("Δώσε μου έναν ακέραιο αριθμό εκκίνησης:", end=" ")
n = int(input())

# Αποθήκευση αρχικού αριθμού για να χρησιμοποιηθεί στο τέλος
# προκειμένου να εμφανίσουμε τα κατάλληλα μηνύματα.
startValue = n

# Θα χρειαστούμε έναν μετρητή για το συνολικό αριθμό βήματων - επαναλήψεων που θα εκτελεστούν.
# Αρχικά θα του δώσουμε την τιμή 0.
steps = 0

# Θα χρησιμοποιήσουμε μια μεταβλητή για να βρούμε το σημείο πλημμυρίδας, δηλαδή τον μέγιστο αριθμό της ακολουθίας.
# Σαν αρχική τιμή θα της δώσουμε τον αρχικό αριθμό n.
maxn = n

# Η διαδικασία θα επαναλαμβάνεται όσο δεν έχουμε φτάσει στο 1.
# (Bέβαια αν καταφέρουμε να ανακαλύψουμε αριθμό που δεν ικανοποιεί την εικασία τη βάψαμε!)
while n > 1:
    print(n, end=" ")

    # αύξηση του μετρητή σε κάθε επανάληψη
    steps = steps + 1

    # έλεγχος αν ο αριθμός είναι άρτιος
    if n % 2 == 0:
        n = n // 2
    else:
        n = 3 * n + 1

    # εφόσον ο νέος αριθμός είναι μεγαλύτερος από το σημείο πλημμυρίδας, 
    # ενημέρωσε κατάλληλα την τιμή του μέγιστου
    if n > maxn:
        maxn = n

print()
print("Η εικασία του Collatz επιβεβαιώθηκε για τον αριθμό", startValue)
print("Συνολικά βήματα:", steps)
print("Σημείο πλημμυρίδας:", maxn)
