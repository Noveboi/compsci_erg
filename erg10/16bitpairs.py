# Σας δίνεται αρχείο κειμένου με μόνο ASCII χαρακτήρες. Αρχικά απεικονίστε κάθε χαρακτήρα σε δυαδικό 
# μήκους 7. Από αυτούς κρατάτε μόνο τα πρώτα δύο και τα τελευταία δύο bits. Χωρίστε την ακολουθία σας 
# σε αριθμούς των 16 bits και εμφανίστε τα ακόλουθα στατιστικά: 
# α) Τι ποσοστό είναι ζυγοί; 
# β) Τι ποσοστό διαιρείται ακριβώς με το 3; 
# γ) Τι ποσοστό διαιρείται ακριβώς με το 5; 
# δ) Τι ποσοστό διαιρείται ακριβώς με το 7;
with open('Tale of two cities (ASCII)', 'r') as f:
    text = f.read()

chars = list(text)
fourBits = []
sixteenBits = []
for char in chars:
    binary = bin(ord(char))[2:]
    fBits = binary[0:2]
    lBits = binary[-2 : len(binary)]
    if len(fourBits) < 3:
        fourBits.append(''.join([fBits,lBits]))
    elif len(fourBits) == 3:
        fourBits.append(''.join([fBits, lBits]))
        sixteenBits.append(''.join(map(str, fourBits)), 2)
        fourBits.clear()

def divByN(nums):
    by2 = 0
    by3 = 0
    by5 = 0
    by7 = 0
    for num in nums:
        num = int(num)
        if num % 2 == 0: by2 += 1
        if num % 3 == 0: by3 += 1
        if num % 5 == 0: by5 += 1
        if num % 7 == 0: by7 += 1
    return [
        f"div by 2: {by2/len(nums) * 100}%", 
        f"div by 3: {by3/len(nums) * 100}%", 
        f"div by 5: {by5/len(nums) * 100}%", 
        f"div by 7: {by7/len(nums) * 100}%"]

for results in divByN(sixteenBits):
    print(results)
