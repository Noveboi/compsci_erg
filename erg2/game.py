# Έστω ένα τετράγωνο 3*3 στο οποίο τοποθετείτε “καπάκια”. Έχετε στην κατοχή σας 27 “καπάκια”, 
# 9 για κάθε μέγεθος (μικρό, μεσαίο, μεγάλο). Μια τριάδα που τερματίζει το παιχίνδι γίνεται οριζόντια, 
# κάθετα ή διαγώνια. Η τριάδα αποτελείται από καπάκια είτε του ίδιου μεγέθους είτε από το μικρό προς το 
# μεγαλύτερο. Επειδή έχετε καπάκια, ένα καπάκι μπορεί να μπει σε οποιοδήποτε τετράγωνο, αρκεί να είναι 
# ελεύθερο ή να υπάρχει εκεί μικρότερο καπάκι. Γράψτε ένα πρόγραμμα το οποίο παίζει τυχαία το παιχνίδι 
# 100 φορές και επιστρέφει το μέσο όρο των βημάτων για να λήξει το παιχνίδι.

import random
from entities import Cap, Board

def spawnCaps(): 
    caps = []
    for i in range(0,27):
        if i < 9: caps.append(Cap(1))
        elif i >= 9 and i < 18: caps.append(Cap(2))
        else: caps.append(Cap(3))
    return caps

def randomlyPlaceCaps(caps,board):
    indexes = [i for i in range(0,27)]
    vert = ['a','b','c']
    hor = ['1','2','3']
    steps = 0
    for row in vert:
        for col in hor:
            steps += 1
            key = f"{row}{col}"
            idx = random.choice(indexes)
            board.tiles[key] = caps[idx].placeOnBoard(board.tiles[key])
            indexes.remove(idx)
    return steps

def isLegalMove(tile1, tile2):#cap = cap to be moved | tile = move position
    if tile2 == None or tile1 > tile2: return True
    return False

def move(i1,i2,i3, board):
    steps = int(0)
    if isLegalMove(board.tiles[i1], board.tiles[i2]) and not board.finish():
        # print(f"{i1} -> {i2}")
        # board.show()
        board.tiles[i1], board.tiles[i2] = board.tiles[i2], board.tiles[i1]
        steps += 1
    elif isLegalMove(board.tiles[i1], board.tiles[i3]) and not board.finish():
        # print(f"{i1} -> {i3}")
        # board.show()
        board.tiles[i1], board.tiles[i3] = board.tiles[i3], board.tiles[i1]
        steps += 1
    elif isLegalMove(board.tiles[i2], board.tiles[i3]) and not board.finish():
        # print(f"{i2} -> {i3}")
        # board.show()
        board.tiles[i2], board.tiles[i3] = board.tiles[i3], board.tiles[i2]
        steps += 1
    return steps

def rowMove(board):
    vert = ['a','b','c']
    steps = int(0)
    for row in vert:
        i1 = f'{row}1'
        i2 = f'{row}2'
        i3 = f'{row}3'
        steps += move(i1,i2,i3,board)
    return steps

def colMove(board):
    hor = ['1','2','3']
    steps = int(0)
    for col in hor:
        i1 = f'a{col}'
        i2 = f'b{col}'
        i3 = f'c{col}'
        steps += move(i1,i2,i3,board)
    return steps


def game():
    caps = spawnCaps()
    board = Board()

    steps = 0
    steps += randomlyPlaceCaps(caps, board)
    # board.show()
    while not board.finish():
        steps += rowMove(board)
        steps += colMove(board)

    print(f"Complete in {steps} steps")
    return steps
if __name__ == "__main__":
    step_sum = 0
    for i in range(1,101):
        print(f"\nGame {i}:")
        step_sum += game()
    print(f"\n\nAverage steps for game over: {step_sum/i}")