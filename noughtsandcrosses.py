#Md Mostak Laheri

import random
import os.path
import json
random.seed()



def draw_board(board):
    for i, row in enumerate(board):
        print(" | ".join(row))
        if i < 2:
            print("---------")

def welcome(board):
    print()
    print("Hello, It's Md Mostak Laheri, Id no: 2511809")
    print()
    print('Welcome to the "Unbeatable Noughts and Crosses" game.')
    print("The board layout is shown below:")
    print()
    draw_board([["1", "2", "3"], ["4", "5", "6"], ["7", "8", "9"]])
    print()
    print("When prompted, enter the number corresponding to the square you want.")

def initialise_board(board):
    for i in range(3):
        board[i] = [' ' for _ in range(3)]
    return board

def map_input_to_cell(choice):
    mapping = {
        1: (0, 0), 2: (0, 1), 3: (0, 2),
        4: (1, 0), 5: (1, 1), 6: (1, 2),
        7: (2, 0), 8: (2, 1), 9: (2, 2)
    }
    return mapping.get(choice, None)

def get_player_move(board):
   while True:
        try:
            move = int(input("Enter a number between (1-9) to choose your cell: "))

            cell = map_input_to_cell(move)
            if cell is None:
                print("Invalid input. Please enter a number between 1 and 9.")
                continue

            row, col = cell
            if board[row][col] == ' ':
                return row, col
            else:
                print("Cell already taken. Try again.")
        except ValueError:
            print("Invalid input. Please enter a number between 1 and 9.")
  
def choose_computer_move(board):
    for row in range(3):
        for col in range(3):
            if board[row][col] == ' ':
                board[row][col] = 'O'
                if check_for_win(board, 'O'):
                    board[row][col] = ' '
                    return row, col
                board[row][col] = ' '
    for row in range(3):
        for col in range(3):
            if board[row][col] == ' ':
                board[row][col] = 'X'
                if check_for_win(board, 'X'):
                    board[row][col] = ' '
                    return row, col
                board[row][col] = ' '

    empty_cells  = [(row, col) for row in range(3) for col in range(3) if board[row][col] == ' ']
    return random.choice(empty_cells)


def check_for_win(board, mark):
    for i in range(3):
        if all([board[i][j] == mark for j in range(3)]):
           return True
        if all([board[j][i] == mark for j in range(3)]):
            return True
        if (board[0][0] == mark and board[1][1] == mark and board[2][2] == mark) or \
           (board[0][2] == mark and board[1][1] == mark and board[2][0] == mark):
            return True
        
    return False

def check_for_draw(board):
  return all(board[row][col] != ' ' for row in range(3) for col in range(3))

        
def play_game(board):
    initialise_board(board)
    draw_board(board)

    while True:
        row, col = get_player_move(board)
        board[row][col] = 'X'
        draw_board(board)

        if check_for_win(board, 'X'):
            print("You Win!")
            return 1
        
        if check_for_draw(board):
            print("It's a draw!, play again for Win")
            return 0

        row, col = choose_computer_move(board)
        board[row][col] = '0'
        draw_board(board)

        if check_for_win(board, '0'):
            print("You lose! Computer wins.")
            return -1
        if check_for_draw(board):
            print("It's a draw ")
            return 0
                    
                
def menu():
    print("1. Start Game")
    print("2. Save score")
    print("3. Load and Display scores")
    print("q. End the program")

    choice = input("Enter your choice (1, 2, 3, or q): ").strip()

    if choice in ['1', '2', '3', 'q']:
        return choice
    else:
        print("Invalid choice. Please enter '1', '2', '3', or 'q'.")
        

def load_scores():
    """
    Load the leaderboard scores from 'leaderboard.txt'.

    Returns:
        dict: A dictionary with player names as keys and scores as values.
              Returns an empty dictionary if the file does not exist.
    """
    try:
        if not os.path.exists('leaderboard.txt'):
            print("No leaderboard file found. Returning an empty leaderboard.")
            return {}

        with open('leaderboard.txt', 'r') as file:
            leaders = json.load(file)
            print("Leaderboard successfully loaded.")
            return leaders

    except (json.JSONDecodeError, IOError) as e:
        print(f"Error loading leaderboard: {e}")
        return {}
    
def save_score(score):
    """
    Save the score to the leaderboard.
    """
    name = input("Enter your name: ").strip()
    leaders = load_scores() 

    if name in leaders:
        leaders[name] += score  
    else:
        leaders[name] = score  

    try:
        with open('leaderboard.txt', 'w') as file:
            json.dump(leaders, file)
        print("Score saved successfully.")
    except IOError as e:
        print(f"Error saving score: {e}")

def display_leaderboard(leaders):
    sorted_leaders = sorted(leaders.items(), key=lambda x: x[1], reverse=True)

    print("Leaderboard:")
    for rank, (player_name, score) in enumerate(sorted_leaders, start=1):
        print(f"{rank}. {player_name}: {score}")


if __name__ == "__main__":
    board = [[' ' for _ in range(3)] for _ in range(3)]
    welcome(board)

if __name__ == "__main__":
    while True:
        choice = menu()
        if choice == '1':
            score = play_game(board)
            if score == 1:
                print("Congratulations, You won successfully.")
            elif score == -1:
                print("It was a logical effort.")
            else:
                print("Thank you for playing; lots of fun.")
        elif choice == '2':
            try:
                save_score(score)  
                print("Score saved successfully.")
            except Exception as e:
                print(f"Error saving score: {e}")
        elif choice == '3':
            leaders = load_scores()
            display_leaderboard(leaders)
        elif choice == 'q':
            print("It was fun, thanks for playing.")
           
            try:
                leaders = load_scores()
                display_leaderboard(leaders)
            except:
                print("No leaderboard available.")
            break
        else:
            print("Invalid choice. Please try again.")
