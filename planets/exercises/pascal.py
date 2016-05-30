n = int(input("Πόσες φορές n θα στρίψουμε το νόμισμα; "))

# η πρώτη γραμμή
line = [1]
# για κάθε γραμμή, μέχρι τη n-οστή
for i in range(n):
    # πρώτο στοιχείο της νέας γραμμής
    newline = [1]
    # κάθε ενδιάμεσο στοιχείο της νέας γραμμής είναι...
    for index in range(1,len(line)):
        # το άθροισμα των δύο στοιχείων "από πάνω" του
        newline.append(line[index-1] + line[index])
    # τελευταίο στοιχείο της νέας γραμμής
    newline.append(1)
    line = newline
    # όλο το περιεχόμενο της for μπορεί να γραφτεί με μία μόνο γραμμή:
    # line = [1] + [line[index-1] + line[index] for index in range(1,len(line))] + [1]

# άθροισμα της n-οστής γραμμής
sum = 2 ** n    
# εμφάνιση πιθανοτήτων
print("Όταν στρίβεις ένα νόμισμα", n, "φορές, η πιθανότητα να φέρεις κορώνα:")
for times in range(0,n+1):
    print(times, "φορές:", line[times] / sum)

    
