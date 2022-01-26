# Έστω ένα τετράγωνο 3*3 στο οποίο τοποθετείτε “καπάκια”. Έχετε στην κατοχή σας 27 “καπάκια”, 
# 9 για κάθε μέγεθος (μικρό, μεσαίο, μεγάλο). Μια τριάδα που τερματίζει το παιχίνδι γίνεται οριζόντια, 
# κάθετα ή διαγώνια. Η τριάδα αποτελείται από καπάκια είτε του ίδιου μεγέθους είτε από το μικρό προς το 
# μεγαλύτερο. Επειδή έχετε καπάκια, ένα καπάκι μπορεί να μπει σε οποιοδήποτε τετράγωνο, αρκεί να είναι 
# ελεύθερο ή να υπάρχει εκεί μικρότερο καπάκι. Γράψτε ένα πρόγραμμα το οποίο παίζει τυχαία το παιχνίδι 
# 100 φορές και επιστρέφει το μέσο όρο των βημάτων για να λήξει το παιχνίδι.

import random

class BottleCap():
    def __init__(self, size):
        self.size = size

def spawnBottleCaps(): 
    caps = []
    for idx in range(0,27):
        if idx < 9: caps.append('S')
        elif idx >= 9 and idx < 18: caps.append('M')
        else: caps.append('L')
    return caps

def game():
    pass

if __name__ == "__main__":
    game()

