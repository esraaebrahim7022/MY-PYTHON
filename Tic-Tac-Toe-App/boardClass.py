class Board :
    def __init__(self):
        self.board =[str(i)for i in range(1,10)]# list comprehension 

    def printBoard(self):
        for i in range(0, 9, 3):
            print( " | " .join (self.board[i:i+3]))
            if i < 6:
                print ("---" * 10)

##############################################33

def update_board(self,choise,sympol):
     if self.is_valid_move(choise):
            self.board[choise-1] = sympol
            return True
     else:
            return False
     

def is_valid_move(self, choice):  # الاختيار بتاعي ينفع ومتاح ولا لا
        return self.board[choice-1].isdigit()#فانكشن بترجعلي ترو لو كه ارقام

def reset_board(self): #بعيد انشاء البورد
        self.board = [str(i) for i in range(1, 10)]



             

