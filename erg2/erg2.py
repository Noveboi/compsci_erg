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
        self.pos = None

    def sizeCompare(self, otherCap):
        if self.size > otherCap: return "Bigger"
        elif self.size < otherCap: return "Smaller"
        return "Same"

class Board():
#   1 2 3
# A o o o
# B o o o   <---- Board
# C o o o
    #a1,b2,c3 etc. represent tiles, they if a cap is placed on them their value becomes the size of the cap
    def __init__(self):
        self.a1 = None
        self.a2 = None
        self.a3 = None
        self.b1 = None
        self.b2 = None
        self.b3 = None
        self.c1 = None
        self.c2 = None
        self.c3 = None
        self.rowA = [self.a1,self.a2,self.a3]
        self.rowB = [self.b1,self.b2,self.b3]
        self.rowC = [self.c1,self.c2,self.c3]
        self.col1 = [self.a1,self.b1,self.c1]
        self.col2 = [self.a2,self.b2,self.c2]
        self.col3 = [self.a3,self.b3,self.c3]
        self.diagRl = [self.a3, self.b2,self.c1]
        self.diagLr = [self.a1, self.b2,self.c3]
        self.rows = [self.rowA, self.rowB, self.rowC]
        self.cols = [self.col1, self.col2, self.col3]
        self.diags = [self.diagLr, self.diagRl]
    
    def moveIsValid(self, beforeTile, afterTile):
        if afterTile == None or afterTile > beforeTile: return True
        return False
    
    def check(self, rcds): #rcd = row, column, diagonal
        for rcd in rcds:
            if rcd == rcd.sort(): return True
        return False
    
    def finish(self):
        if self.check(self.rows) or self.check(self.cols) or self.check(self.diags): return True
        return False

def spawnBottleCaps(): 
    caps = []
    for idx in range(0,27):
        if idx < 9: caps.append(BottleCap(1))
        elif idx >= 9 and idx < 18: caps.append(BottleCap(2))
        else: caps.append(BottleCap(3))
    return caps

def game():
    pass

if __name__ == "__main__":
    game()
    caps = spawnBottleCaps()
    idx1 = random.randint(0,27)
    idx2 = random.randint(0,27)
    

