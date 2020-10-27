board=[" " for i in range(9)]

def print_board():
    row1 = "| {} | {} | {} |".format(board[0],board[1],board[2])
    row2 = "| {} | {} | {} |".format(board[3],board[4],board[5])
    row3 = "| {} | {} | {} |".format(board[6],board[7],board[8])
    print()
    print(row1)
    print(row2)
    print(row3)
    print()

def player_move(icon):
    if icon=="X":
        num=1
    elif icon=="O":
        num=2
    print("Your turn player {}".format(num))
    choice=int(input("Enter your choice(1-9):").strip())
    if board[choice - 1]==" ":
        board[choice - 1]=icon       
    else:
        print("Oops! That place is already filled.")

def is_victory(icon):
    if(board[0]==icon and board[1]==icon and board[2]==icon) or \
                    (board[3]==icon and board[4]==icon and board[5]==icon) or \
                      (board[6]==icon and board[7]==icon and board[8]==icon) or \
                      (board[0]==icon and board[3]==icon and board[6]==icon) or \
                      (board[1]==icon and board[4]==icon and board[7]==icon) or \
                      (board[2]==icon and board[5]==icon and board[8]==icon) or \
                      (board[0]==icon and board[5]==icon and board[8]==icon) or \
                      (board[2]==icon and board[5]==icon and board[6]==icon):
        return True
    else:
        return False                 

def is_draw():
    if (board[0]!=" " and \
        board[1]!=" " and \
        board[2]!=" " and \
        board[3]!=" " and \
        board[4]!=" " and \
        board[5]!=" " and \
        board[6]!=" " and \
        board[7]!=" " and \
        board[8]!=" "):
        return True
    else:
        return False  
  
while True: 
    print_board()  
    player_move("X")
    print_board()
    if is_victory("X"):
        print_board()
        print("PLAYER 1 WINS!")
        break
    elif is_draw():
        print("The game is draw!")
        break
    print_board()
    player_move("O")
    if is_victory("O"):
        print_board()
        print("PLAYER 2 WINS!")
        break
    elif is_draw():
        print("The game is draw!")
        break
