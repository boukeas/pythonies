import random
# δημιουργία τυχαίου μυστικού αριθμού
secret = random.randint(1,32)
# επανάληψη:
#   δεν τερματίζεται, συνθήκη πάντα αληθής
while True:
    # εμφάνιση προτροπής και ανάγνωση αριθμού
    print("Μάντεψε τον αριθμό: 1 - 32")
    number = int(input())
    # έλεγχος αριθμού και εμφάνιση μηνύματος
    if number != secret:
        print("Λάθος.")
    else:
        print("Σωστά!")
