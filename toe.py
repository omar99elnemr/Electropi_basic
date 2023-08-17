def print_board(board):
    for row in board:
        for square in row:
            print(square or"-","|", end=" ")
        print()
            

def get_move(board,current_player):
    while True:
        print_board(board)
        print(f"\nit's player {current_player}'s turn:")
        row=int(input("Enter row number from 1:3 => "))-1
        column=int(input("Enter column number from 1:3 => "))-1
        try:      
            if board[row][column]=="":
                  board[row][column]=current_player
                  break
            else:
                  print("invalid input!")
        except IndexError:
              print("invalid input!",IndexError)
          
          
def check_win(board, current_player):
    for i in range(2):
        # Check rows
        if board[i][0] == board[i][1] == board[i][2] == current_player:
            return True
        
        # Check columns
        if board[0][i] == board[1][i] == board[2][i] == current_player:
            return True
          
    #Check diagonals
    if board[0][0] == board[1][1] == board[2][2] == current_player:
        return True

    if board[0][2] == board[1][1] == board[2][0] == current_player:
        return True

    return False
          
          
def check_tie(board):
    for row in board:
        for square in row:
          if square=="":
              return False
    return True
    

def start_game():
     board=[["","",""],
           ["","",""],
           ["","",""]]
     players=['X','O']
     current_player=players[0]

     while True:
        get_move(board, current_player)

        if check_win(board, current_player):
            print("====================")
            print(f"Player {current_player} wins!")
            print("====================")
            print_board(board)
            break


        if check_tie(board):
            print("==============")
            print("It's a tie!")
            print("=============")
            print_board(board)
            break

    #Switch players
        if current_player == players[0]:
            current_player = players[1]
        else:
            current_player = players[0]

start_game()