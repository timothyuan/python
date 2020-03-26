import random

def display_board(board):
    print(board[1]+'|'+board[2]+'|'+board[3])
    print('- - -')
    print(board[4]+'|'+board[5]+'|'+board[6])
    print('- - -')
    print(board[7]+'|'+board[8]+'|'+board[9])

def player_input(val, board):
    prompt = 'Which square would you like to place '+val+', note: enter 0 to see numbering, -1 for current board: '
    while(True):
        try:
            x = int(input(prompt))
        except ValueError:
            print('Not an integer, try again')
            continue
        if x == -1:
            display_board(board)
        elif x == 0:
            help()
        elif x<-1 or x>9:
            print('Not in the valid range, try again')
        elif board[x] == 'X' or board[x] == 'O':
            print('There is already something there, try again')
        else:
            board[x] = val
            break

def help():
    print('Squares are numbered as the following:')
    print('1|2|3\n- - -\n4|5|6\n- - -\n7|8|9')

def win_check(val, board):
    for i in range(1,8,3):
        if board[i] == val and board[i+1] == val and board[i+2] == val:
            return True
    for i in range(1,4):
        if board[i] == val and board[i+3] == val and board[i+6] == val:
            return True
    if board[1] == val and board[5] == val and board[9] == val:
        return True
    if board[3] == val and board[5] == val and board[7] == val:
        return True
    return False

def full_check(board):
    for i in board[1:]:
        if i!='X' and i!='O':
            return False
    return True

print('Welcome to Tic Tac Toe!')
markers = ['X', 'O']
turn = random.randint(0,1)
print(markers[turn] + ' goes first')
board = ['#',' ',' ',' ',' ',' ',' ',' ',' ',' ']
while(not full_check(board)):
    player_input(markers[turn], board)
    display_board(board)
    if(win_check(markers[turn], board)):
        print(markers[turn] + ' won!')
        break
    turn = 1 - turn
else:
    print('Game over!')
