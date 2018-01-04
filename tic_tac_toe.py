import csv
import random
import os
import sys

# colors
W  = '\033[0m'  # white (normal)
R  = '\033[31m' # red
G  = '\033[32m' # green
O  = '\033[33m' # orange
B  = '\033[34m' # blue
P  = '\033[35m' # purple

class CrossOrCircle:
    def __init__(self, number):
        self.circle = False
        self.cross = False
        self.number = number

    def print_circle(self):
        self.circle = True
        self.cross = False

    def print_cross(self):
        self.circle = False
        self.cross = True

    def __str__(self):
        if self.circle:
            return "{}".format(G +'0')
        elif self.cross:
            return "{}".format(B +'X')
        else:
            return "{}".format(R+self.number)

class Board:
    def __init__(self):
        self.board = []
    
    def add_board_from_file(self, file='tictac.csv'):
        with open(file, 'r') as f:
            reader = csv.reader(f)
            self.board = [sign for row in reader for line in row for sign in line]
        for sign in self.board:
            if sign.isdigit():
                self.board[self.board.index(sign)] = CrossOrCircle(sign)

    def change_value(self, player_choose):
        for sign in self.board:
            if isinstance(sign, CrossOrCircle) and not sign.circle and not sign.cross:
                if player_choose == sign.number:
                    return sign

    def ai_for_computer(self):
        list_for_crossed = [100]
        for sign in self.board:
            if isinstance(sign, CrossOrCircle) and sign.cross:
                list_for_crossed.append(int(sign.number))
                list_for_crossed.sort()
        list_for_circled = [100]
        for sign in self.board:
            if isinstance(sign, CrossOrCircle) and sign.circle:
                list_for_circled.append(int(sign.number))
                list_for_circled.sort()
        list_to_choose = []
        for sign in self.board:
            if isinstance(sign, CrossOrCircle) and not sign.cross and not sign.circle:
                list_to_choose.append(sign.number)
                list_to_choose.sort()

        #computer won
        if 1 in list_for_circled and 2 in list_for_circled and 3 in list_for_circled:
            print(O+'COMPUTER IS SMARTER THAN YOU!\nYOU ARE LOSER!')
            sys.exit()
        if 4 in list_for_circled and 5 in list_for_circled and 6 in list_for_circled:
            print(O+'COMPUTER IS SMARTER THAN YOU!\nYOU ARE LOSER!')
            sys.exit()
        if 7 in list_for_circled and 8 in list_for_circled and 9 in list_for_circled:
            print(O+'COMPUTER IS SMARTER THAN YOU!\nYOU ARE LOSER!')
            sys.exit()
        if 1 in list_for_circled and 4 in list_for_circled and 7 in list_for_circled:
            print(O+'COMPUTER IS SMARTER THAN YOU!\nYOU ARE LOSER!')
            sys.exit()
        if 2 in list_for_circled and 5 in list_for_circled and 8 in list_for_circled:
            print(O+'COMPUTER IS SMARTER THAN YOU!\nYOU ARE LOSER!')
            sys.exit()
        if 3 in list_for_circled and 6 in list_for_circled and 9 in list_for_circled:
            print(O+'COMPUTER IS SMARTER THAN YOU!\nYOU ARE LOSER!')
            sys.exit()
        if 1 in list_for_circled and 5 in list_for_circled and 9 in list_for_circled:
            print(O+'COMPUTER IS SMARTER THAN YOU!\nYOU ARE LOSER!')
            sys.exit()
        if 3 in list_for_circled and 5 in list_for_circled and 7 in list_for_circled:
            print(O+'COMPUTER IS SMARTER THAN YOU!\nYOU ARE LOSER!')
            sys.exit()
        #user won
        if 1 in list_for_crossed and 2 in list_for_crossed and 3 in list_for_crossed:
            print(O+'YOU ARE SO SMART!\nYOU WON!')
            sys.exit()
        if 4 in list_for_crossed and 5 in list_for_crossed and 6 in list_for_crossed:
            print(O+'YOU ARE SO SMART!\nYOU WON!')
            sys.exit()
        if 7 in list_for_crossed and 8 in list_for_crossed and 9 in list_for_crossed:
            print(O+'YOU ARE SO SMART!\nYOU WON!')
            sys.exit()
        if 1 in list_for_crossed and 4 in list_for_crossed and 7 in list_for_crossed:
            print(O+'YOU ARE SO SMART!\nYOU WON!')
            sys.exit()
        if 2 in list_for_crossed and 5 in list_for_crossed and 8 in list_for_crossed:
            print(O+'YOU ARE SO SMART!\nYOU WON!')
            sys.exit()
        if 3 in list_for_crossed and 6 in list_for_crossed and 9 in list_for_crossed:
            print(O+'YOU ARE SO SMART!\nYOU WON!')
            sys.exit()
        if 1 in list_for_crossed and 5 in list_for_crossed and 9 in list_for_crossed:
            print(O+'YOU ARE SO SMART!\nYOU WON!')
            sys.exit()
        if 3 in list_for_crossed and 5 in list_for_crossed and 7 in list_for_crossed:
            print(O+'YOU ARE SO SMART!\nYOU WON!')
            sys.exit()
        
        #computer to win
        if 1 in list_for_circled and 2 in list_for_circled and str(3) in list_to_choose:
            return self.change_value(str(3))
        if 1 in list_for_circled and 3 in list_for_circled and str(2) in list_to_choose:
            return self.change_value(str(2))
        if 2 in list_for_circled and 3 in list_for_circled and str(1) in list_to_choose:
            return self.change_value(str(1))
        if 4 in list_for_circled and 5 in list_for_circled and str(6) in list_to_choose:
            return self.change_value(str(6))
        if 4 in list_for_circled and 6 in list_for_circled and str(5) in list_to_choose:
            return self.change_value(str(5))
        if 5 in list_for_circled and 6 in list_for_circled and str(4) in list_to_choose:
            return self.change_value(str(4))
        if 7 in list_for_circled and 8 in list_for_circled and str(9) in list_to_choose:
            return self.change_value(str(9))
        if 7 in list_for_circled and 9 in list_for_circled and str(8) in list_to_choose:
            return self.change_value(str(8))
        if 8 in list_for_circled and 9 in list_for_circled and str(7) in list_to_choose:
            return self.change_value(str(7))
        
        if 1 in list_for_circled and 4 in list_for_circled and str(7) in list_to_choose:
            return self.change_value(str(7))
        if 1 in list_for_circled and 7 in list_for_circled and str(4) in list_to_choose:
            return self.change_value(str(4))
        if 4 in list_for_circled and 7 in list_for_circled and str(1) in list_to_choose:
            return self.change_value(str(1))
        if 2 in list_for_circled and 5 in list_for_circled and str(8) in list_to_choose:
            return self.change_value(str(8))
        if 2 in list_for_circled and 8 in list_for_circled and str(5) in list_to_choose:
            return self.change_value(str(5))
        if 5 in list_for_circled and 8 in list_for_circled and str(2) in list_to_choose:
            return self.change_value(str(2))
        if 3 in list_for_circled and 6 in list_for_circled and str(9) in list_to_choose:
            return self.change_value(str(9))
        if 3 in list_for_circled and 9 in list_for_circled and str(6) in list_to_choose:
            return self.change_value(str(6))
        if 6 in list_for_circled and 9 in list_for_circled and str(3) in list_to_choose:
            return self.change_value(str(3))
        
        if 1 in list_for_circled and 5 in list_for_circled and str(9) in list_to_choose:
            return self.change_value(str(9))
        if 1 in list_for_circled and 9 in list_for_circled and str(5) in list_to_choose:
            return self.change_value(str(5))
        if 5 in list_for_circled and 9 in list_for_circled and str(1) in list_to_choose:
            return self.change_value(str(1))
        if 3 in list_for_circled and 5 in list_for_circled and str(7) in list_to_choose:
            return self.change_value(str(7))
        if 3 in list_for_circled and 7 in list_for_circled and str(5) in list_to_choose:
            return self.change_value(str(5))
        if 5 in list_for_circled and 7 in list_for_circled and str(3) in list_to_choose:
            return self.change_value(str(3))


        #computer to block
        if 1 in list_for_crossed and 2 in list_for_crossed and str(3) in list_to_choose:
            return self.change_value(str(3))
        if 1 in list_for_crossed and 3 in list_for_crossed and str(2) in list_to_choose:
            return self.change_value(str(2))
        if 2 in list_for_crossed and 3 in list_for_crossed and str(1) in list_to_choose:
            return self.change_value(str(1))
        if 4 in list_for_crossed and 5 in list_for_crossed and str(6) in list_to_choose:
            return self.change_value(str(6))
        if 4 in list_for_crossed and 6 in list_for_crossed and str(5) in list_to_choose:
            return self.change_value(str(5))
        if 5 in list_for_crossed and 6 in list_for_crossed and str(4) in list_to_choose:
            return self.change_value(str(4))
        if 7 in list_for_crossed and 8 in list_for_crossed and str(9) in list_to_choose:
            return self.change_value(str(9))
        if 7 in list_for_crossed and 9 in list_for_crossed and str(8) in list_to_choose:
            return self.change_value(str(8))
        if 8 in list_for_crossed and 9 in list_for_crossed and str(7) in list_to_choose:
            return self.change_value(str(7))

        if 1 in list_for_crossed and 4 in list_for_crossed and str(7) in list_to_choose:
            return self.change_value(str(7))
        if 1 in list_for_crossed and 7 in list_for_crossed and str(4) in list_to_choose:
            return self.change_value(str(4))
        if 4 in list_for_crossed and 7 in list_for_crossed and str(1) in list_to_choose:
            return self.change_value(str(1))
        if 2 in list_for_crossed and 5 in list_for_crossed and str(8) in list_to_choose:
            return self.change_value(str(8))
        if 2 in list_for_crossed and 8 in list_for_crossed and str(5) in list_to_choose:
            return self.change_value(str(5))
        if 5 in list_for_crossed and 8 in list_for_crossed and str(2) in list_to_choose:
            return self.change_value(str(2))
        if 3 in list_for_crossed and 6 in list_for_crossed and str(9) in list_to_choose:
            return self.change_value(str(9))
        if 3 in list_for_crossed and 9 in list_for_crossed and str(6) in list_to_choose:
            return self.change_value(str(6))
        if 6 in list_for_crossed and 9 in list_for_crossed and str(3) in list_to_choose:
            return self.change_value(str(3))
        
        if 1 in list_for_crossed and 5 in list_for_crossed and str(9) in list_to_choose:
            return self.change_value(str(9))
        if 1 in list_for_crossed and 9 in list_for_crossed and str(5) in list_to_choose:
            return self.change_value(str(5))
        if 5 in list_for_crossed and 9 in list_for_crossed and str(1) in list_to_choose:
            return self.change_value(str(1))
        if 3 in list_for_crossed and 5 in list_for_crossed and str(7) in list_to_choose:
            return self.change_value(str(7))
        if 3 in list_for_crossed and 7 in list_for_crossed and str(5) in list_to_choose:
            return self.change_value(str(5))
        if 5 in list_for_crossed and 7 in list_for_crossed and str(3) in list_to_choose:
            return self.change_value(str(3))
        else:
            x = random.choice(list_to_choose)
            return self.change_value(str(x))

    def __str__(self):
        board = ''
        for n, sign in enumerate(self.board, 1):
            if n == 10 or n == 20 or n == 30 or n == 40 or n == 50 or n == 60:
                board += R+str(sign) + '\n'
            else:
                board += R+str(sign)
        return board
            

def random_start(board):
    randomm = random.choice([1,0])
    if randomm == 0:
        for i in range(4):
            try:
                os.system('clear')
                print(board)
                user = input(O+"choose number: ")
                board.change_value(user).print_cross()
                os.system('clear')
                print(board)
                board.ai_for_computer().print_circle()
                os.system('clear')            
                print(board)
                if i == 3:
                    user = input(O+"choose number: ")
                    board.change_value(user).print_cross()
                    os.system('clear')            
                    print(board)
            except AttributeError:
                user = input(O+"Last chance: : ")
                board.change_value(user).print_cross()
                os.system('clear')            
                print(board)
    elif randomm == 1:
        for i in range(4):
            try:
                board.ai_for_computer().print_circle()
                os.system('clear')            
                print(board)
                user = input(O+"choose number: ")
                board.change_value(user).print_cross()
                os.system('clear')            
                print(board)
                if i == 3:
                    board.ai_for_computer().print_circle()
                    os.system('clear')            
                    print(board)
            except AttributeError:
                user = input(O+"Last chance: ")
                board.change_value(user).print_cross()
                os.system('clear')            
                print(board)
def main():
    board = Board()
    board.add_board_from_file()
    random_start(board)


if __name__ == "__main__":
    main()