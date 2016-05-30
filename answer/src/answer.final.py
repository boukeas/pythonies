import time

# είσοδος ονόματος
print("Πώς σε λένε;", end=" ")
name = input()
# ανάκτηση τοπικής ώρας συστήματος
hour = time.localtime().tm_hour
# εμφάνιση χαιρετισμού ανάλογα με την ώρα
if hour < 14:
    print("Καλημέρα", name)
else:
    print("Καλησπέρα", name)

# καθυστέρηση
wait = 3
time.sleep(wait)
# ορισμός και εμφάνιση της Απάντησης
answer = 42
print("Η Απάντηση είναι...", answer)
