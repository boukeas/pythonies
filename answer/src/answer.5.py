import time
# είσοδος ονόματος
print("Πώς σε λένε;")
name = input()
# ανάκτηση τοπικής ώρας συστήματος
hour = time.localtime().tm_hour
# εμφάνιση χαιρετισμού ανάλογα με την ώρα
if hour < 14:
    print("Καλημέρα", name)
else:
    print("Καλησπέρα", name)
# καθυστέρηση
wait = 7500000 * 365 * 24 * 60 * 60
time.sleep(wait)
# ορισμός και εμφάνιση της Απάντησης
answer = 42
print("Η Απάντηση είναι...", answer)
