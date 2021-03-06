''' άσκηση από το από το http://pythonies.mysch.gr/chapters/planets.pdf

Τα μπισκότα τύχης (fortune cookies) είναι μπισκότα που στο εσωτερικό
τους περιέχουν μηνύματα με προβλέψεις γι’ αυτόν που τα ανοίγει. Υλο-
ποιήστε ένα πρόγραμμα που θα καλεί τον χρήστη να ανοίξει ένα τυχερό
μπισκότο και στη συνέχεια θα του εμφανίζει μια τυχαία πρόβλεψη.

Η παραλλαγή αυτή διαβάζει τα μηνύματα από ένα εξωτερικό αρχείο.
'''

import random
import time

messages = []

with open('messages.txt', 'r', encoding='utf-8') as messageFile:
    for line in messageFile:
        messages.append(line)
    messageFile.close()

''' εναλλακτικά:
messageFile = open('messages.txt','r',encoding='utf-8')
for line in messageFile:
    messages.append(line)
messageFile.close()
'''

while True:
    print("Σήμερα είναι η τυχερή σου μέρα.")
    time.sleep(1)
    print("Θα σου κάνω μια πρόβλεψη για το μέλλον.")
    time.sleep(1)
    print("Έτοιμος; Πάτα <Enter> και η ζωή σου μπορεί να αλλάξει για πάντα!")
    input()
    print("Λοιπόν το τυχερό σου μπισκότο λέει...")
    time.sleep(1)
    # επιλογή τυχαίου μηνύματος από τη λίστα
    print(random.choice(messages))

    # ερώτηση για επανάληψη
    print("Θέλεις κι άλλο; (N/O)")
    answer = input().upper()
    if answer != 'Ν':
        break
