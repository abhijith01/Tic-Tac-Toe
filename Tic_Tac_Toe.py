board=["-","-","-",
       "-","-","-",
       "-","-","-"]
print('------------ TIC TAC TOE----------------')
player1=input("enter your name (player1):")
player2=input("enter your name (player2):")
print("do you want to start the game ??[Y/N]")
response=input()
if response== "Y" or response=="y":
    response=True
else:
    response=False


def display_board():
    print(board[0]+"|"+board[1]+"|"+board[2])
    print(board[3]+"|"+board[4]+"|"+board[5])
    print(board[6]+"|"+board[7]+"|"+board[8])
def win_tie():
     row1=(board[0]==board[1]==board[2] and board[0]!="-")
     row2=(board[3]==board[4]==board[5] and board[4]!="-")
     row3 = (board[6] == board[7] == board[8] and board[6] != "-")
     col1 = (board[0] == board[3] == board[6] and board[0] != "-")
     col2 = (board[1] == board[4] == board[7] and board[4] != "-")
     col3 = (board[2] == board[5] == board[8] and board[5] != "-")
     dig1=(board[0] == board[4] == board[8] and board[0] != "-")
     dig2=(board[2] == board[4] == board[6] and board[2] != "-")
     if row1 :
         print(board[0]+"won the game")
         return True
     elif row2 :
         print(board[3]+"won the game")
         return True
     elif row3 :
         print(board[6]+"  won the game")
         return True
     elif col1:
         print(board[0]+"  won the game")
         return True
     elif col2:
         print(board[1]+"  won the game")
         return True
     elif col3:
         print(board[2]+"  won the game")
         return True
     elif dig1:
         print(board[0]+"  won the game")
         return True
     elif dig2:
         print(board[2]+"  won the game ")
         return True
     else:
         return  False
def playgame():
    display_board()
    current_player = "X"
    while game_is_on() and response:
        print(flip_player(current_player)+" turn")
        pos = input("enter the postion 1-9:")
        pos=int(pos)-1
        if board[pos]=='-' and board[pos]!='X' and board[pos]!="O":
            board[pos]=flip_player(current_player)
        else:
            print("plz enter valid postion ")
            current_player=flip_player(current_player)
        current_player = flip_player(current_player)
        display_board()
def game_is_on():
    flag=0
    f=False
    for i in range(0,9):
        if board[i]=="-" and not win_tie():
            return True
        else:
            flag=1
    if flag==1:
        print("game is draw")

def flip_player(current_player):
    if current_player=="X":
        current_player="O"
    else:
        current_player="X"
    return current_player
playgame()
