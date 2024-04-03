import time

# def createBoard(board):
#     print(" %c | %c | %c " % (board[0][0], board[0][1], board[0][2]))
#     print("___|___|___")
#     print(" %c | %c | %c " % (board[1][0], board[1][1], board[1][2]))
#     print("___|___|___")
#     print(" %c | %c | %c " % (board[2][0], board[2][1], board[2][2]))
#     print("   |   |")  

def createBoard(board):
    for i in range(3):
        for j in range(3):
            if board[i][j] == "X":
                print("\x1b[31m X \x1b[0m", end="")
            elif board[i][j] == "O":
                print("\x1b[34m O \x1b[0m", end="")
            else:
                print("   ", end="")
            if j < 2:
                print("| ", end="")
        if i < 2:
            print("\n-------------")
    print(" ")        
         
dict_x_o = {
0: " ",
1: "X",
2: "O" 
}               
    
def win_draw(board, name1, name2):
      # Check rows
    for row in range(3):
        if board[row][0] == board[row][1] == board[row][2] and board[row][0] == "X":
            print(f"Player {name1} has won")
            return name1
        elif board[row][0] == board[row][1] == board[row][2] and board[row][0] == "O":
            print(f"Player {name2} has won")
            return name2
    # Check columns
    for col in range(3):
        if board[0][col] == board[1][col] == board[2][col] and board[0][col] == "X":
            print(f"Player {name1} has won")
            return name1
        if board[0][col] == board[1][col] == board[2][col] and board[0][col] == "O":
            print(f"Player {name2} has won")
            return name2   
    # Check diagonals
    if board[0][0] == board[1][1] == board[2][2] == "X" or board[0][2] == board[1][1] == board[2][0] == "X":
        print(f"Player {name1} has won")
        return name1
    elif board[0][0] == board[1][1] == board[2][2] == "0" or board[0][2] == board[1][1] == board[2][0] == "O":
        print(f"Player {name2} has won")
        return name2
    else:
        return "draw"       


def player_turn(board, row, column, player1):
    counter = 0
    if board[row][column] == dict_x_o[0]:
        if player1 == 1:
            board[row][column] = dict_x_o[1]
        else:
            board[row][column] = dict_x_o[2]
        createBoard(board)    
        counter += 1    
        return counter      
    elif board[row][column] == dict_x_o[1]:
        print("Sorry the cell is already marked with X.")
        print("Please wait 2 seconds board is loading again...")
        time.sleep(2)
    else:
        print("Sorry the cell is already marked with O.")
        print("Please wait 2 seconds board is loading again...")
        time.sleep(2)               
   
def game():
    board = [[" ", " ", " "],
        [" ", " ", " "],
        [" ", " ", " "]]   
    counter = 0
    player1 = 1
    wins_player1 = 0
    wins_player2 = 0
    draws = 0
    createBoard(board)
    name_1 = input("Please insert player 1's name: ")
    name_2 = input("Please insert player 2's name: ")
    print(f"player 1: {name_1} player 2: {name_2}")
    while True:
        if player1 == 1:
            print(f"Player {name_1} Chance")
        else:
            print(f"Player {name_2} Chance")
        i = int(input("Please insert the row number you want to point from 0 to 2: ")) 
        j = int(input("Please insert the column number you want to point from 0 to 2: ")) 
        # Check if players' selection is out of range
        while (i > 2 or i < 0) or (j > 2 or j < 0):
            print("Out of boarder. Pick another one. ")
            break 
        if player1 == 1:
            counter +=  player_turn(board, i,j, 1)
            player1 = 0
        else:
            counter +=  player_turn(board, i,j, 0)
            player1 = 1      
        winner = win_draw(board,  name_1, name_2)    
        if counter == 9 and winner == "draw":
            draws += 1
            print ("Draw!")
            break
        elif winner == name_1: 
            wins_player1 += 1
            break
        elif winner == name_2: 
            wins_player2 += 1
            break    
    return wins_player1, wins_player2, draws
   
def load_game_again():  
    wins_player1_total = 0
    wins_player2_total = 0
    draws_total = 0
    while True:
        start_time = time.time()
        wins_player1, wins_player2, draws = game()
        wins_player1_total += wins_player1
        wins_player2_total += wins_player2
        draws_total += draws
        end_time = time.time()
        game_duration = end_time - start_time 
        print(f"The game lasted {game_duration:.2f} seconds.")
        print("\nGame Stats:")
        print(f"Player 1 Wins: {wins_player1_total}")
        print(f"Player 2 Wins: {wins_player2_total}")
        print(f"Draws: {draws_total}")
        winner = input("Press 'Y' to continue to another game or 'N' to quit: ")
        if winner.upper() == 'N':
            print("Goodbye!")
            break
        elif winner.upper() == 'Y':
            continue
        else:
            print("Invalid input. Please enter 'Y' to continue or 'N' to quit.")   
                       
     
    
load_game_again()    