''' άσκηση από το http://pythonies.mysch.gr/chapters/nim.pdf
'''

def next1(p, q):
    """ Επιστρέφει τον αριθμό του παίκτη
    που παίζει μετά τον παίκτη p.
    p: αριθμός παίκτη (>= 1)
    q: πλήθος παικτών που συμμετέχουν
    """
    if p < q:
        return p + 1
    else:
        return 1

def next2(p, q):
    """ Επιστρέφει τον αριθμό του παίκτη
    που παίζει μετά τον παίκτη p.
    p: αριθμός παίκτη (>= 1)
    q: πλήθος παικτών που συμμετέχουν
    """
    return (p % q) + 1

print("Δοκιμή για τη γενικευμένη συνάρτηση next.")
print("Δώσε αριθμό παικτών:")
nbPlayers = int(input())

for player in range(1,nbPlayers+1):
    print("Μετά τον παίκτη", player, "παίζει ο", next2(player,nbPlayers))

