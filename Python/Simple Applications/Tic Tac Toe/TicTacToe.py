import random
class TicTacToe:
    def __init__(self) -> None:
        self.player = "X"
        self.next_player = self.handle_player(self.player)
        self.count = 0
   

    def handle_player(self,player):
        if player == "X":
            return "O"
        else:
            return "X"
    
    def Game(self):
      
        board = ["1","2","3","4","5","6","7","8","9"]
        while True:
            
            user_input = int(input("Choose a spot: "))
            
            if board[user_input-1]=="X" or board[user_input-1]=="O":
                print("This spot is alreay field. Choose another spot")
            
            else:
                board[user_input-1] = self.next_player
                self.player, self.next_player = self.handle_player(self.player), self.player
                print(self.next_player, "'s turn")
                self.count+=1
            formatted_board = "{} {} {}\n{} {} {}\n{} {} {}"
            print('   |   |   ')
            print(' ' + board[0] + ' | ' + board[1] + ' | ' + board[2] + ' ')
            print('   |   |   ')
            print('-----------')
            print('   |   |   ')
            print(' ' + board[3] + ' | ' + board[4] + ' | ' + board[5] + ' ')
            print('   |   |   ')
            print('-----------')
            print('   |   |   ')
            print(' ' + board[6] + ' | ' + board[7] + ' | ' + board[8] + ' ')
            print('   |   |   ')

            #print(formatted_board.format(*board))
            if board[0] == board[1] == board[2] == self.player:
                print("Player",self.player, "Win" )
                break
            elif board[3] == board[4] == board[5] == self.player:
                print("Player",self.player, "Win" )
                break
            elif board[6] == board[7] == board[8] ==self.player:
                print("Player",self.player, "Win" )
                break
            elif board[0] == board[3] == board[6]==self.player:
                print("Player",self.player, "Win" )
                break
            elif board[1] == board[4] == board[7] == self.player:
                print("Player",self.player, "Win" )
                break
            elif board[2] == board[5] == board[8] == self.player:
                print("Player",self.player, "Win" )
                break
            elif board[0] == board[4] == board[8] == self.player:
                print("Player",self.player, "Win" )
                break
            elif board[2] == board[4] == board[7] == self.player:
                print("Player",self.player, "Win" )
                break

            if self.count == 9:
                print("Its a Tie")
                break
      
