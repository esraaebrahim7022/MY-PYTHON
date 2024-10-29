from boardClass import Board
from menuClass  import Menu
from playerClass import Player


class Game:
    def __init__(self):
        self.board = Board()
        self.Player =[Player(),Player()]  # Fixed instantiation
        self.menu = Menu()  # Fixed instantiation
        self.current_player_index = 0 

    def start_game(self):
        choice = self.menu.choose_start_menu # Fixed typo
        if choice == "1":
            self.set_up_players()  # Fixed typo
            self.play_game()
        else:
            self.quit_game()

    def set_up_players(self):
        for number, player in enumerate(self.players, start=1):
            print(f"Player {number}, enter your details: ")
            player.choose_name()
            player.choose_symbol()
            print("-" * 20)

    def play_game(self):
        while True:
            self.play_turn()
            if self.check_win() or self.check_draw():
                choice = self.menu.choose_end_menu()
                if choice == "1":
                    self.restart_game()
                else:
                    self.quit_game()
                    break

    def check_draw(self):
        return all(not cell.isdigit() for cell in self.board.board)
            
    def check_win(self):
        win_combinations = [
            [0, 1, 2], [3, 4, 5], [6, 7, 8],
            [0, 3, 6], [1, 4, 7], [2, 5, 8],
            [0, 4, 8], [2, 4, 6]
        ]
        for combo in win_combinations:
            if self.board.board[combo[0]] == self.board.board[combo[1]] == self.board.board[combo[2]]:
                self.board.display_board()
                print(f"{self.players[self.current_player_index].name} wins!")
                return True
        return False

    def play_turn(self):
        player = self.players[self.current_player_index]
        self.board.printBoard()
        print(f"{player.name}'s turn ({player.symbol})")
        while True:
            try:
                cell_choice = int(input("Choose a number from (1-9): "))
                if 1 <= cell_choice <= 9 and self.board.update_board(cell_choice, player.symbol):
                    break
                else:
                    print("Invalid move, try again")
            except ValueError:
                print("Please enter a number between 1 and 9")

        self.switch_player()
    
    def switch_player(self):
        self.current_player_index = 1 - self.current_player_index

    def restart_game(self):
        self.board.reset_board()
        self.current_player_index = 0 
        self.play_game()

    def quit_game(self):
        print("Thank you for playing!")


game = Game()
game.start_game()

        


       
        