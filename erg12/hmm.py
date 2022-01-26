# H υπηρεσία https://www.cloudflare.com/en-gb/leagueofentropy/ προσφέρει τυχαίους αριθμούς. 
# Χρησιμοποιείστε αρχικά την διεύθυνση https://drand.cloudflare.com/public/latest για να βρείτε ποιος 
# είναι ο τελευταίος γύρος και στην συνέχεια πάρτε τις τελευταίες 100 τιμές (πεδίο randomness) μέσα από 
# το https://drand.cloudflare.com/public/{round}. Μετατρέψτε αυτές τις τιμές σε δυαδικό και εμφανίστε 
# το μήκος της μεγαλύτερης ακολουθίας με συνεχόμενα μηδενικά και το μήκος της μεγαλύτερης ακολουθίας με 
# συνεχόμενες μονάδες.

#headers in case of ssl error: UserAgent: Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:95.0) Gecko/20100101 Firefox/95.0
import requests
from json import loads
getRoundUrl = "https://drand.cloudflare.com/public/latest"

with requests.Session() as session:
    response1 = session.get(getRoundUrl)
    if response1.ok: 
        lastRoundUrl = f"https://drand.cloudflare.com/public/{loads(response1.text)['round']}"
        response2 = session.get(lastRoundUrl)
        if response2.ok:
            randomness = loads(response2.text)['randomness']
            rBin = bin(int(randomness, base=16))[2:]
            maxZeroCount = len(max(rBin.split('1')))
            maxOneCount = len(max(rBin.split('0')))
            print(f"0's: {maxZeroCount}\n1's: {maxOneCount}")
        else: print(f"oh no! i hate the internet! code: {response2.status_code}")
    else: print(f"shit hit the fan! code: {response1.status_code}")