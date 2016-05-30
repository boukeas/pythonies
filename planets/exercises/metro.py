stations = [
    "ΠΕΙΡΑΙΑΣ", 	
    "ΦΑΛΗΡΟ",  	
    "ΜΟΣΧΑΤΟ",  	
    "ΚΑΛΛΙΘΕΑ",  	
    "ΤΑΥΡΟΣ",  	
    "ΠΕΤΡΑΛΩΝΑ",  	
    "ΘΗΣΕΙΟ",  	
    "ΜΟΝΑΣΤΗΡΑΚΙ",  	
    "ΟΜΟΝΟΙΑ",  	
    "ΒΙΚΤΩΡΙΑ",  	
    "ΑΤΤΙΚΗ",  	
    "ΑΓΙΟΣ ΝΙΚΟΛΑΟΣ", 
    "ΚΑΤΩ ΠΑΤΗΣΙΑ",  	
    "ΑΓΙΟΣ ΕΛΕΥΘΕΡΙΟΣ",  	
    "ΑΝΩ ΠΑΤΗΣΙΑ",  	
    "ΠΕΡΙΣΣΟΣ",  	
    "ΠΕΥΚΑΚΙΑ",  	
    "ΝΕΑ ΙΩΝΙΑ",  	
    "ΗΡΑΚΛΕΙΟ",  	
    "ΕΙΡΗΝΗ",  	
    "ΝΕΡΑΤΖΙΩΤΙΣΣΑ", 
    "ΜΑΡΟΥΣΙ",  	
    "Κ.Α.Τ.",  	
    "ΚΗΦΙΣΙΑ"]

def inputWord(words, prompt, errorprompt):
    """ διαβάζει μια λέξη από το χρήστη και την επιστρέφει, 
        εξασφαλίζοντας ότι αυτή βρίσκεται στη λίστα επιτρεπτών λέξεων
        words: η λίστα επιτρεπτών λέξεων
        prompt: η προτροπή που εμφανίζεται στο χρήστη
        errorprompt: το μήνυμα σε περίπτωση λάθους
    """
    print(prompt)
    word = input().upper()
    while word not in words:
        print(errorprompt)
        print(prompt)
        word = input().upper()
    return word

while True:
    # σταθμοί αναχώρησης και τερματισμού
    departure = inputWord(stations, "Δώστε σταθμό αφετηρίας", "Ανύπαρκτος σταθμός")
    destination = inputWord(stations, "Δώστε σταθμό προορισμού", "Ανύπαρκτος σταθμός")
    # θέσεις (δείκτες) των σταθμών αυτών
    depIndex = stations.index(departure)
    dstIndex = stations.index(destination)
    # υπολογισμός κατεύθυνσης και ενδιάμεσων σταθμών
    if depIndex < dstIndex:
        terminal = stations[-1]
        route = stations[depIndex+1:dstIndex]
    else:
        terminal = stations[0]
        route = stations[depIndex-1:dstIndex:-1]
    # εμφάνιση πληροφοριών  
    print("\nΕνδιάμεσοι σταθμοί από", departure, "προς", destination, "με κατεύθυνση", terminal)
    for station in route:
        print(station)
    # συνέχεια
    print("Επιθυμείτε πληροφορίες για κάποια άλλη διαδρομή;")
    if input().upper() in ["Ο", "ΟΧΙ", "N", "No"]:
        break
print("Καλές διαδρομές.")

