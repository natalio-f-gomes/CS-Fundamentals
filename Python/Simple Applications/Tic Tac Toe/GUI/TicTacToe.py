from tkinter import *
class TicTacToe:
    def __init__(self):
        app = Tk()
        app.title("Tic Tac Toe")
        app.geometry("380x500")
        app.maxsize(380,500)
        app.minsize(380,500)

        self.current_player = "X"
        self.array = ["_","_","_","_","_","_","_","_","_"]
        self.attempts = 0
        self.winning = False

        self.row_1_col_1 = Button(app, width=10, height=7, command=lambda index=0: self.TicTacToe(index))
        self.row_1_col_1.grid(row=0, column=0)

        self.row_1_col_2 = Button(app,width=10, height=7, command=lambda index=1: self.TicTacToe(index))
        self.row_1_col_2.grid(row=0, column=1)

        self.row_1_col_3 = Button(app,width=10, height=7, command=lambda index=2: self.TicTacToe(index))
        self.row_1_col_3.grid(row=0, column=2)


        self.row_2_col_1 = Button(app, width=10, height=7,command=lambda index=3: self.TicTacToe(index))
        self.row_2_col_1.grid(row=1, column=0)

        self.row_2_col_2 = Button(app,width=10, height=7,command=lambda index=4: self.TicTacToe(index))
        self.row_2_col_2.grid(row=1, column=1)

        self.row_2_col_3 = Button(app,width=10, height=7,command=lambda index=5: self.TicTacToe(index))
        self.row_2_col_3.grid(row=1, column=2)

        self.row_3_col_1 = Button(app, width=10, height=7,command=lambda index=6: self.TicTacToe(index))
        self.row_3_col_1.grid(row=2, column=0)

        self.row_3_col_2 = Button(app,width=10, height=7,command=lambda index=7: self.TicTacToe(index))
        self.row_3_col_2.grid(row=2, column=1)

        self.row_3_col_3 = Button(app,width=10, height=7,command=lambda index=8: self.TicTacToe(index))
        self.row_3_col_3.grid(row=2, column=2)

        self.win_label = Label(app, width=10, text="")
        self.win_label.grid(row=3,column=1)

        self.restart_btn= Button(app,command=lambda index=-1: self.TicTacToe(index), text="Restart")
        self.restart_btn.grid(row=4, column=1)


        app.mainloop()

    def TicTacToe(self,btn_value):
        
        if btn_value == -1:  # restart button clicked
            self.current_player = "X"
            self.attempts = 0
            self.winning = False
            self.array = ["_","_","_","_","_","_","_","_","_"]
            self.win_label.config(text="")
            self.row_1_col_1.config(text="")
            self.row_1_col_2.config(text="")
            self.row_1_col_3.config(text="")
            self.row_2_col_1.config(text="")
            self.row_2_col_2.config(text="")
            self.row_2_col_3.config(text="")
            self.row_3_col_1.config(text="")
            self.row_3_col_2.config(text="")
            self.row_3_col_3.config(text="")

            return

        self.attempts += 1
        if self.attempts == 9:
            self.win_label.config(text="It's a Tie")

        if self.current_player == "X":
            self.current_player = "O"
        else:
            self.current_player = "X"

        if btn_value == 0:
            self.row_1_col_1.config(text=self.current_player)
        elif btn_value == 1:
            self.row_1_col_2.config(text=self.current_player)
        elif btn_value == 2:
            self.row_1_col_3.config(text=self.current_player)
        elif btn_value == 3:
            self.row_2_col_1.config(text=self.current_player)
        elif btn_value == 4:
            self.row_2_col_2.config(text=self.current_player)
        elif btn_value == 5:
            self.row_2_col_3.config(text=self.current_player)
        elif btn_value == 6:
            self.row_3_col_1.config(text=self.current_player)
        elif btn_value == 7:
            self.row_3_col_2.config(text=self.current_player)
        elif btn_value == 8:
            self.row_3_col_3.config(text=self.current_player)

        self.array[btn_value] = self.current_player
        print(self.array)

        if (self.array[0]==self.array[1]==self.array[2]==self.current_player
            or self.array[3]==self.array[4]==self.array[5]==self.current_player
            or self.array[6]==self.array[7]==self.array[8]==self.current_player 
            or self.array[0]==self.array[3]==self.array[6]==self.current_player 
            or self.array[1]==self.array[4]==self.array[7]==self.current_player 
            or self.array[2]==self.array[5]==self.array[8]==self.current_player 
            or self.array[0]==self.array[4]==self.array[8]==self.current_player 
            or self.array[2]==self.array[4]==self.array[6]==self.current_player):
            self.win_label.config(text=self.current_player + " Wins")
            self.winning = True
            return


if __name__ == "__main__":
    app = TicTacToe()
    
