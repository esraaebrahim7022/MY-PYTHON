class Player :
    def __init__(self):
        self.name = ""
        self.symbol = ""

    #choose name function:
    def choose_name(self):
     while True:
        name = input('enter your name(letters only): ')
        if name.isalpha():#فانكشن بترجعلي ب ترو لو ال داخل حروف بس
            self.name = name
            break
            print('please enter a valid name')
            
#-----------------------------------------------------

#choose sympol function:
    def choose_sympol(self):
     while True:
        symbol = input(f'{self.name}, choose your symbol: ')
        if symbol.isalpha() and len(symbol)==1:#بتاكد انه دخل حرف واحد
            self.symbol = symbol.upper()
            break
            print('please enter a valid symbol!! ')