class Cap():
    def __init__(self, size):
        self.size = size
        self.pos = None

    def sizeCompare(self, otherCap):
        if self.size > otherCap: return "Bigger"
        elif self.size < otherCap: return "Smaller"
        return "Same"        
    
    def placeOnBoard(self, tile):
        self.pos = tile
        return self.size #so the value can be stored in the Board class as well

class Board():
#   1 2 3
# a o o o
# b o o o   <---- Board
# c o o o

    #a1,b2,c3 etc. represent tiles, they if a cap is placed on them their value becomes the size of the cap
    def __init__(self):
        self.tiles = {
            'a1': None, 'a2': None, 'a3': None,
            'b1': None, 'b2': None, 'b3': None,
            'c1': None, 'c2': None, 'c3': None
        }

    def isFull(self):
        if None not in self.tiles: return True
        return False
    
    def check(self, mode): #rcd = row, column, diagonal
        vert = ['a','b','c']
        hor = ['1','2','3']
        if mode == 'row':
            for row in vert:
                temp_row = []
                for col in hor:
                    key = f"{row}{col}"
                    temp_row.append(self.tiles[key])
                if temp_row == sorted(temp_row): 
                    return True
            return False
        elif mode == 'column':
            for col in hor:
                temp_col = []
                for row in vert:
                    key = f"{row}{col}"
                    temp_col.append(self.tiles[key])
                if temp_col == sorted(temp_col): 
                    return True
            return False
        elif mode == 'diagonal':
            for i in range(2):
                temp_diag = []
                if i == 2: 
                    hor.reverse()
                for col, row in enumerate(vert):
                    key = f"{row}{col+1}"
                    temp_diag.append(self.tiles[key])
                if temp_diag == sorted(temp_diag): 
                    return True
            return False

    def finish(self):
        if self.check('row') or self.check('column') or self.check('diagonal'): 
            return True
        return False

    def show(self):
        i = 0
        print("--Board--")
        for tile in self.tiles:
            if i % 3 == 0: print()
            print(f"{self.tiles[tile]} ", end='')
            i += 1
        print()