


class Player:
    def _init_(self, name, token):
       self.name = name
       self.token = token # X or O
        
class Game:
    def __init__ (self):
        self.count = 0
        self.game = ['0', '1', '2', '3', '4', '5', '6', '7', '8']
        self.board = [' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ']
       
      
    def instructions(self):
        return 'Using the above example, please enter the corresponding number you wish to place an X: ' 

    
    
    def first_image(self): 
        return f"""
        {self.game[0]}|{self.game[1]}|{self.game[2]} 
        {self.game[3]}|{self.game[4]}|{self.game[5]}
        {self.game[6]}|{self.game[7]}|{self.game[8]}
        """

    def __repr__(self):
        
        return f"""
        {self.board[0]}|{self.board[1]}|{self.board[2]} 
        {self.board[3]}|{self.board[4]}|{self.board[5]}
        {self.board[6]}|{self.board[7]}|{self.board[8]}
        """
    def move_1(self):
        True
        while True:
            False
            x = int(input('Spot number 0-8: '))
            if x <= 8:
                self.count += 1
                self.board[x] = 'x'
                # win condition calc_winner
                print(self.count)
                return print(game)
                
            else:
                print('Enter a valid number!')
                False
                  

    def move_2(self):   
        True
        while True:
            False
            x = int(input('Spot number 0-8: '))
            if x <= 8:
                self.count += 1
                self.board[x] = 'o'
                # win condition calc_winner
                print(self.count)
                
                return print(game)
            else:
                print('Enter a valid number!')
                False
        
    
    # def move_2(self):
    #     x = int(input('Spot number 0-8: '))
    #     self.board[x] = 'o'
    #     return self.board
    

    def calc_winner(self):
        if {self.board[0]} == {self.board[1]} == {self.board[2]} and {self.board[0]} != (' ') and {self.board[1]} != ''  and {self.board[2]} != '':
            return print(f'player1 {self.board[0]} has won')
        elif {self.board[3]} == {self.board[4]} == {self.board[5]} and {self.board[3]}  and {self.board[4]} and {self.board[5]} != '':
            return print(f'player 2{self.board[4]} has won')
        elif {self.board[6]} == {self.board[7]} == {self.board[8]} and {self.board[6]} and {self.board[7]} and {self.board[8]} != '':
            return print(f'player 3{self.board[7]} has won')
        elif {self.board[0]} == {self.board[3]} == {self.board[6]} and {self.board[0]} and {self.board[3]} and {self.board[6]} != '':
            return print(f'player4 {self.board[3]} has won')
        elif {self.board[1]} == {self.board[4]} == {self.board[7]} and {self.board[1]} and {self.board[4]} and {self.board[7]} != '':
            return print(f'player5 {self.board[7]} has won')
        elif {self.board[2]} == {self.board[5]} == {self.board[8]} and {self.board[2]} and {self.board[5]} and {self.board[8]} != '':
            return print(f'player6 {self.board[8]} has won')
        elif {self.board[0]} == {self.board[4]} == {self.board[8]} and {self.board[0]} and {self.board[4]} and {self.board[8]} != '':
            return print(f'player 7{self.board[8]} has won')
        elif {self.board[2]} == {self.board[4]} == {self.board[6]} and {self.board[2]} and {self.board[4]} and {self.board[6]} != '':
            return print(f'player 8{self.board[6]} has won')
        else: 
            pass

        # if {self.board[0]}=={self.board[1]}=={self.board[2]} == "x":
        #     print("Player X has won")
        # elif {self.board[3]}=={self.board[4]}=={self.board[5]} == 'x':
        #     print("Player X has won")
        # elif {self.board[6]}=={self.board[7]}=={self.board[8]} == 'x':
        #     print("Player X has won")
        # elif {self.board[0]}=={self.board[1]}=={self.board[2]} == 'o':
        #     print("yes1")
        # elif {self.board[3]}=={self.board[4]}=={self.board[5]} == 'o':
        #     print("yes2")
        # elif {self.board[6]}=={self.board[7]}=={self.board[8]} == 'o':
        #     print("yes3")

    # def __getitem__(self, index):
    #     return self.board[index]
    
    def is_full(self):
        if game.count >= 10:
            print('game is a draw!')
            again = input('Would you like to play again?: ').lower()
            if again == 'yes' or again == 'y':
                game.board = [' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ']
                game.count = 0
                return True
            else:
                print('Enter a valid number!')
                return False
    
    def is_game_over():
        pass

game = Game()    
player = Player()



def main():
    print(game.first_image())
    print(game.instructions())
    
    
    while True:
        
        game.is_full()
        game.move_1()
        game.calc_winner()
      
        game.is_full()
        game.move_2()
        game.calc_winner()
        
        
           
    
    


    
   


main()

    
    