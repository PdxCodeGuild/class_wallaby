class Player:
    def _init_(self, token):
       self.name = " "
  

    def player_name(self):
        name = input(f"Enter player #1's name: ")
        self.name = name
        
    
        
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
                if self.board[x] == ' ':
                    self.count += 1
                    self.board[x] = 'x'
                    print(self.count)
                    return print(self)
                elif self.board[x] == 'x' or self.board[x] == 'o':
                    print('Spot has already been chosen') 
                    False
            else:
                print('Enter a valid number!')
                False
                  

    def move_2(self):   
        
        True
        while True:
            False
            x = int(input('Spot number 0-8: '))
            if x <= 8:
                if self.board[x] == ' ':
                    self.count += 1
                    self.board[x] = 'o'
                    print(self.count)
                    return print(self)
                elif self.board[x] == 'x' or self.board[x] == 'o':
                    print('Spot has already been chosen') 
                    False
            else:
                print('Enter a valid number!')
                False
        
    
    # def move_2(self):
    #     x = int(input('Spot number 0-8: '))
    #     self.board[x] = 'o'
    #     return self.board
    

    def calc_winner(self, name):
        if self.board[0] !=  ' ' and self.board[1] != ' '  and self.board[2] != ' ' and {self.board[0]} == {self.board[1]} and {self.board[1]} == {self.board[2]} != [' ']:
            print(f'{name} has won')
            return False
        
        elif self.board[3] != ' ' and {self.board[4]} != ' '  and {self.board[5]} != ' ' and {self.board[3]} == {self.board[4]} and {self.board[4]} == {self.board[5]}:
            print(f'{name} has won')
            return False

        elif self.board[6] != ' ' and self.board[7] != ' '  and self.board[8] != ' ' and {self.board[6]} == {self.board[7]} and {self.board[7]} == {self.board[8]}:
            print(f'{name} has won')
            return False 
        elif self.board[0] != ' ' and self.board[3] != ' '  and self.board[6] != ' ' and {self.board[0]} == {self.board[3]} and {self.board[3]} == {self.board[6]}:
            print(f'{name} has won')
            return False 
        elif self.board[1] != ' ' and self.board[4] != ' '  and self.board[7] != ' ' and {self.board[1]} == {self.board[4]} and {self.board[4]} == {self.board[7]}:
            print(f'{name} has won')
            return False 
        elif self.board[2] != ' ' and self.board[5] != ' '  and self.board[8] != ' ' and {self.board[2]} == {self.board[5]} and {self.board[5]} == {self.board[8]}:
            print(f'{name} has won')
            return False 
        elif self.board[2] != ' ' and self.board[4] != ' '  and self.board[6] != ' 'and {self.board[2]} == {self.board[4]} and {self.board[4]} == {self.board[6]}:
            print(f'{name} has won')
            return False
        elif self.board[0] != ' ' and self.board[4] != ' '  and self.board[8] != ' ' and {self.board[0]} == {self.board[4]} and {self.board[4]} == {self.board[8]}:
            print(f'{name} has won')
            return False  
        else:
            pass
            
            
            
         
    
    def is_full(self):
        if self.count >= 10:
            print('game is a draw!')
            again = input('Would you like to play again?: ').lower()
            if again == 'yes' or again == 'y':
                self.board = [' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ']
                self.count = 0
                return True
            else:
                print('Enter a valid number!')
                return False
    
    def is_game_over():
        pass





def main():
    game = Game()    
    player_1 = Player()
    player_2 = Player()
    player_1.player_name()    
    player_2.player_name()  
    print(game.first_image())
    print(game.instructions())
    
    
    while True:
        
        game.is_full()
        print(f'Player on deck: {player_1.name}')
        game.move_1()
        if game.calc_winner(player_1.name) == False:
            again = input('Would you like to play again?: ').lower()
            if again == 'yes' or again == 'y':
                game.board = [' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ']
                game.count = 0

      
        game.is_full()
        print(f'Player on deck: {player_2.name}')
        game.move_2()
        if game.calc_winner(player_2.name) == False:
            again = input('Would you like to play again?: ').lower()
            if again == 'yes' or again == 'y':
                game.board = [' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ']
                game.count = 0
        
        
           
    
    


    
   


main()

    
    