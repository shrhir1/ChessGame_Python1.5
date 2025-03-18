# assignment: programming assignment 4
# author: shreya hiremath
# date: August 12, 2022
# file: chess.py is a program write a program that shows the valid moves of chess pieces.
# input: strings and integers (position)
# output: possible positions of chess piece 



class Board:
    def __init__(self):
        self.board = {}

        self.empty()

    def empty(self):
        for col in 'abcdefgh':
            for row in '12345678':
                self.board[col + row] = ' '

    def set(self, pos, label):
        if pos in self.board.keys():
            self.board[pos] = label

    def draw(self):
        print('   a   b   c   d   e   f   g   h')
        print(' +---+---+---+---+---+---+---+---+')
        print('8| {} | {} | {} | {} | {} | {} | {} | {} |8'.format(self.board['a8'], self.board['b8'],
                                                                           self.board['c8'], self.board['d8'],
                                                                           self.board['e8'], self.board['f8'],
                                                                           self.board['g8'], self.board['h8']))
        print(' +---+---+---+---+---+---+---+---+')
        print('7| {} | {} | {} | {} | {} | {} | {} | {} |7'.format(self.board['a7'], self.board['b7'],
                                                                           self.board['c7'], self.board['d7'],
                                                                           self.board['e7'], self.board['f7'],
                                                                           self.board['g7'], self.board['h7']))
        print(' +---+---+---+---+---+---+---+---+')
        print('6| {} | {} | {} | {} | {} | {} | {} | {} |6'.format(self.board['a6'], self.board['b6'],
                                                                           self.board['c6'], self.board['d6'],
                                                                           self.board['e6'], self.board['f6'],
                                                                           self.board['g6'], self.board['h6']))
        print(' +---+---+---+---+---+---+---+---+')
        print('5| {} | {} | {} | {} | {} | {} | {} | {} |5'.format(self.board['a5'], self.board['b5'],
                                                                           self.board['c5'], self.board['d5'],
                                                                           self.board['e5'], self.board['f5'],
                                                                           self.board['g5'], self.board['h5']))
        print(' +---+---+---+---+---+---+---+---+')
        print('4| {} | {} | {} | {} | {} | {} | {} | {} |4'.format(self.board['a4'], self.board['b4'],
                                                                           self.board['c4'], self.board['d4'],
                                                                           self.board['e4'], self.board['f4'],
                                                                           self.board['g4'], self.board['h4']))
        print(' +---+---+---+---+---+---+---+---+')
        print('3| {} | {} | {} | {} | {} | {} | {} | {} |3'.format(self.board['a3'], self.board['b3'],
                                                                           self.board['c3'], self.board['d3'],
                                                                           self.board['e3'], self.board['f3'],
                                                                           self.board['g3'], self.board['h3']))
        print(' +---+---+---+---+---+---+---+---+')
        print('2| {} | {} | {} | {} | {} | {} | {} | {} |2'.format(self.board['a2'], self.board['b2'],
                                                                           self.board['c2'], self.board['d2'],
                                                                           self.board['e2'], self.board['f2'],
                                                                           self.board['g2'], self.board['h2']))
        print(' +---+---+---+---+---+---+---+---+')
        print('1| {} | {} | {} | {} | {} | {} | {} | {} |1'.format(self.board['a1'], self.board['b1'],
                                                                           self.board['c1'], self.board['d1'],
                                                                           self.board['e1'], self.board['f1'],
                                                                           self.board['g1'], self.board['h1']))
        print(' +---+---+---+---+---+---+---+---+')
        print('   a   b   c   d   e   f   g   h')




class Chess_Piece:
    def __init__(self, name, board, pos, color='white'):
        self.position = self.get_index(pos)
        self.color = color
        board.set(pos, self.get_name())
        self.name = name

    def get_index(self, pos):
        return ('abcdefgh'.index(pos[0]), '12345678'.index(pos[1]))

    def get_rank(self, index):
        if index >= 0 and index < 8:
            return '12345678'[index]

    def get_file(self, index):
        if index >= 0 and index < 8:
            return 'abcdefgh'[index]

    def get_name(self):
        return self.name

    def moves(self, board):
        pass


class Rook(Chess_Piece):

    def get_name(self):
        return 'R'

    def moves(self, board):
        x, y = self.position

        total = [(x, i) for i in range(8)] + [(i, y) for i in range(8)]

        total = [(i, j) for (i, j) in total if (i, j) != (x, y)]


        for p in total:
            file = self.get_file(p[0])
            rank = self.get_rank(p[1])

            key = file + rank
            board.board[key] = "x"



class King(Chess_Piece):

    def get_name(self):
        return 'K'

    def moves(self, board):
        x, y = self.position

        a = [x - 1, x, x + 1]
        b = [y - 1, y, y + 1]

        total = [(x, y) for x in a for y in b]
        total.remove((x, y))

        for p in total:
            file = self.get_file(p[0])
            rank = self.get_rank(p[1])
            if(file is not None):
                if (rank is not None):
                    key = file + rank
                    board.board[key] = "x"


class Knight (Chess_Piece):
    
    def get_name(self):
        return 'N'
        
    def moves(self, board):
        
        x, y = self.position

        total = [(x+2,y-1),(x+2,y+1),(x-2,y-1), (x-2,y+1), (x+1,y-2),(x-1,y-2),(x-1,y+2), (x+1,y+2)]

        domain = [0,1,2,3,4,5,6,7]

        total = [(i,j) for (i,j) in total if i in domain and j in domain]
        
    
        for p in total:
            file = self.get_file(p[0])
            rank = self.get_rank(p[1])
            
            key = file + rank
            board.board[key] = "x"



class Bishop(Chess_Piece):

    def get_name(self):
        return 'B'

    def moves(self, board):
        x, y = self.position


        total = []
        for i in range(1,8):
            a = [x-i, x, x+i]
            b = [y-i, y, y+i]
            total = total + [(i, j) for i in a for j in b] #if (i j !=(x,y)]
            
        #print(total)

        new  = [(i, j) for (i, j) in total] #if i!=j]
        new = [(i, j) for (i, j) in new if i != x]
        new = [(i, j) for (i, j) in new if j != y]


        for p in new:
            file = self.get_file(p[0])
            rank = self.get_rank(p[1])
            if(file is not None):
                if (rank is not None):
                    key = file + rank
                    board.board[key] = "x"
                    
        board.board[self.position] = self.get_name()


class Queen(Chess_Piece):
    
    def get_name(self):
        return 'Q'
        
    def moves(self, board):
        
        Rook.moves(self,board)
        Bishop.moves(self,board)





if __name__ == '__main__':
    print('Welcome to the Chess Game!')
    board = Board()
    board.draw()
    # your code goes here
    board.empty()
    # print(board.board)

    while True:
        answer = input('Enter a chess piece and its position or type X to exit:\n')
        if len(answer) != 3:
            if answer.upper() == 'X':
                print("Goodbye!")
                break
            else:
                continue
        elif answer[0].upper() in 'KQNBR' and answer[1] in 'abcdefgh' and answer[2] in '12345678':

        
            if answer[0].upper() == 'R':
                rook = Rook('R', board, answer[1:])
                rook.moves(board)
                
            if answer[0].upper() == 'K':
                king = King('K', board, answer[1:])
                king.moves(board)

            if answer[0].upper() == 'N':
                knight = Knight('N', board, answer[1:])
                knight.moves(board)

            if answer[0].upper() == 'B':
                bishop = Bishop('B', board, answer[1:])
                bishop.moves(board)

            if answer[0].upper() == 'Q':
                queen = Queen('Q', board, answer[1:])
                queen.moves(board)

        else:
            continue
                
        board.draw()
        board.empty()
