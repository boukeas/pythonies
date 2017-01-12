## Mastermind
    
Μια αντικειμενοστραφής υλοποίηση σε Python 3 του δημοφιλούς παιχνιδιού [Mastermind](https://en.wikipedia.org/wiki/Mastermind_(board_game)).

### Βασικές Οντότητες

#### Το παιχνίδι (κλάση `MastermindGame`)

Σε κάθε παιχνίδι Mastermind, συμμετέχουν δύο παίκτες, ο Codemaker και ο Codebreaker. Ο Codemaker σχηματίζει στην αρχή του παιχνιδιού μια μυστική κωδική λέξη (με τα επιμέρους στοιχεία της λέξεις να αντλούνται από ένα δεδομένο σύνολο). Ο Codebreaker διαθέτει ένα πλήθος προσπαθειών για να καταφέρει να μαντέψει την μυστική κωδική λέξη. Σε κάθε προσπάθεια προτείνει μια πιθανή κωδική λέξη και ο Codemaker την αξιολογεί.

Ένα αντικείμενο της κλάσης `MastermindGame` αντιστοιχεί σε ένα παιχνίδι με συγκεκριμένο σύνολο στοιχείων από το οποίο σχηματίζονται οι κωδικές λέξεις (αριθμοί, γράμματα, χρώματα, κλπ), συγκεκριμένο μέγεθος των κωδικών λέξεων (π.χ. τέσσερα στοιχεία) και συγκεκριμένο πλήθος προσπαθειών για τον Codebreaker. Η μέθοδος `play` της κλάσης `MastermindGame` υλοποιεί τη διαδικασία του παιχνιδιού.

#### Οι παίκτες (βασική κλάση `CodePlayer` και υποκλάσεις `Codemaker` και `Codebreaker`)

Ο ρόλος του `Codemaker` είναι να επιλέγει την μυστική κωδική λέξη στην αρχή του παιχνιδιού, να παρέχει στον `Codebreaker` ανατροφοδότηση για τις κωδικές λέξεις που επιλέγει και να αποκαλύπτει την μυστική κωδική λέξη στο τέλος του παιχνιδιού.

Η κλάση `Codemaker` παρέχει abstract μεθόδους γι' αυτές τις λειτουργίες που θα πρέπει να υλοποιηθούν από τις υποκλάσεις της.

Ο ρόλος του `Codebreaker` είναι να επιλέγει σε κάθε προσπάθεια μια πιθανή κωδική λέξη, να δέχεται την ανατροφοδότηση του `Codemaker` γι' αυτές τις επιλογές του και να ενημερώνεται για την μυστική κωδική λέξη στο τέλος του παιχνιδιού.

Η κλάση `Codebreaker` παρέχει abstract μεθόδους γι' αυτές τις λειτουργίες που θα πρέπει να υλοποιηθούν από τις υποκλάσεις της.

#### Μια στρατηγική για τον `Codebreaker` (βασική κλάση `Strategy`)

Οι κινήσεις ενός `Codebreaker` υπαγορεύονται από μια στρατηγική. Μια στρατηγική παρέχει μια πρόταση ως προς την κωδική λέξη που πρέπει να επιλέξει σε κάθε βήμα ο `Codebreaker` και επηρρεάζεται από τις ανατροφοδοτήσεις που λαμβάνει ο `Codebreaker` για τις κωδικές λέξεις που επιλέγει.

Η κλάση `Strategy` παρέχει abstract μεθόδους γι' αυτές τις λειτουργίες που θα πρέπει να υλοποιηθούν από τις υποκλάσεις της.

#### Οι κωδικές λέξεις (κλάση `Code`, υποκλάση της `tuple`)

Κάθε κωδική λέξη είναι μια πλειάδα, με μέγεθος και στοιχεία που αντλούνται από τα δεδομένα του παιχνιδιού.

#### Ο αποτιμητής (κλάση `Evaluator`)

Βασικό στοιχείο του παιχνιδιού είναι η δυνατότητα σύγκρισης δύο κωδικών λέξεων ώστε να εκτιμηθεί σε πόσες θέσεις συμπίπτουν και πόσα επιπλέον κοινά στοιχεία έχουν σε διαφορετικές θέσεις. Αυτή η λειτουργία είναι απαραίτητη σε πολλές οντότητες του παιχνιδιού και για διαφορετικούς λόγους, γι' αυτό και απομονώθηκε σε αυτή την ξεχωριστή κλάση.

Η μέθοδος αποτίμησης είναι στατική (static method) κι έτσι δεν χρειάζεται να δημιουργηθούν αντικείμενα αυτής της κλάσης για να χρησιμοποιηθεί η μέθοδος.

### Παράγωγες Οντότητες

#### Αυτοματοποιημένος codemaker (κλάση `MachineMaker`, υποκλάση της `Codemaker`)

Η βασική λειτουργία ενός μηχανικού codemaker είναι να επιλέγει με τυχαίο τρόπο, στην αρχή του παιχνιδιού, την μυστική κωδική λέξη. Για τις  αποτιμήσεις των πιθανών κωδικών λέξεων του `Codebreaker` χρησιμοποιεί τον `Evaluator`.

#### Αυτοματοποιημένος codebreaker (κλάση `MachineBreaker`, υποκλάση της `Codebreaker`)

Η βασική λειτουργία ενός μηχανικού codemaker είναι η επιλογή μιας πιθανής κωδικής λέξης σε κάθε προσπάθεια, η οποία ουσιαστικά υπαγορεύεται από την στρατηγική την οποία δέχεται σαν παράμετρο (γι' αυτό και η κλάση είναι απλούστατη).

#### Ο Χρήστης ως Παίκτης (κλάση `HumanPlayer`, υποκλάση της `CodePlayer`)

Η κλάση αυτή δεν σχετίζεται με το ρόλο του χρήστη ως codebreaker ή codemaker, απλά παρέχει μια μέθοδο που επιτρέπει την είσοδο κωδικών λέξεων από το χρήστη. Αυτή είναι μια απαραίτητη λειτουργία όταν ένας από τους δύο παίκτες είναι ο χρήστης, όποιος κι αν είναι ο ρόλος του.

#### Ο Χρήστης ως codemaker (κλάση `HumanMaker`, υποκλάση των `HumanPlayer` και `Codemaker`)

Η βασική λειτουργία των αντικειμένων αυτής της κλάσης είναι να αλληλεπιδρούν με τον χρήστη στο ρόλο του codemaker, δηλαδή να εισάγουν από το χρήστη την αποτίμηση των πιθανών κωδικών λέξεων που δοκιμάζει ο codebreaker σε κάθε προσπάθεια.

#### Ο Χρήστης ως codebreaker (κλάση `HumanBreaker`, υποκλάση των `HumanPlayer` και `Codebreaker`)

Η βασική λειτουργία των αντικειμένων αυτής της κλάσης είναι να αλληλεπιδρούν με τον χρήστη στο ρόλο του codebreaker, δηλαδή να εισάγουν από το χρήστη την πιθανή κωδική λέξη που επιθυμεί να δοκιμάσει σε κάθε προσπάθεια.

#### Ο Χρήστης ως codebreaker με στρατηγική (κλάση `HumanAugmentedBreaker`, υποκλάση της `HumanBreaker`)

Τα αντικείμενα αυτής της κλάσης δέχονται ως επιπλέον παράμετρο μια στρατηγική, την οποία μπορεί να χρησιμοποιήσει ο χρήστης για να δεχθεί *υποδείξεις* (χωρίς βέβαια να είναι υποχρεωμένος να τις ακολουθήσει, σε αντίθεση μ' έναν απλό μηχανικό codebreaker).

### Στρατηγικές

* Τυχαία επιλογή κωδικής λέξης (κλάση `RandomStrategy`, υποκλάση της `Strategy`)
* Διατήρηση συνόλου συμβατών κωδικών λέξεων (κλάση `PossibleStrategy`, υποκλάση της `Strategy`)
* Τυχαία επιλογή από το σύνολο συμβατών κωδικών λέξεων (κλάση `PossibleSetRandomStrategy`, υποκλάση της `PossibleSetStrategy`)
* Αλγόριθμος του Knuth ή 5-guess algorithm (κλάση `KnuthStrategy`, υποκλάση της `PossibleSetStrategy`)

### Άδεια Χρήσης

[3-clause BSD License](https://opensource.org/licenses/BSD-3-Clause)

Copyright 2017 George Boukeas (boukeas@gmail.com)

Redistribution and use in source and binary forms, with or without modification, are permitted provided that the following conditions are met:

1. Redistributions of source code must retain the above copyright notice, this list of conditions and the following disclaimer.

2. Redistributions in binary form must reproduce the above copyright notice, this list of conditions and the following disclaimer in the documentation and/or other materials provided with the distribution.

3. Neither the name of the copyright holder nor the names of its contributors may be used to endorse or promote products derived from this software without specific prior written permission.

THIS SOFTWARE IS PROVIDED BY THE COPYRIGHT HOLDERS AND CONTRIBUTORS "AS IS" AND ANY EXPRESS OR IMPLIED WARRANTIES, INCLUDING, BUT NOT LIMITED TO, THE IMPLIED WARRANTIES OF MERCHANTABILITY AND FITNESS FOR A PARTICULAR PURPOSE ARE DISCLAIMED. IN NO EVENT SHALL THE COPYRIGHT HOLDER OR CONTRIBUTORS BE LIABLE FOR ANY DIRECT, INDIRECT, INCIDENTAL, SPECIAL, EXEMPLARY, OR CONSEQUENTIAL DAMAGES (INCLUDING, BUT NOT LIMITED TO, PROCUREMENT OF SUBSTITUTE GOODS OR SERVICES; LOSS OF USE, DATA, OR PROFITS; OR BUSINESS INTERRUPTION) HOWEVER CAUSED AND ON ANY THEORY OF LIABILITY, WHETHER IN CONTRACT, STRICT LIABILITY, OR TORT (INCLUDING NEGLIGENCE OR OTHERWISE) ARISING IN ANY WAY OUT OF THE USE OF THIS SOFTWARE, EVEN IF ADVISED OF THE POSSIBILITY OF SUCH DAMAGE.
