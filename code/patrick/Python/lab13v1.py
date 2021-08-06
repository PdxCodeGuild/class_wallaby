class Player:
    def __init__(self, token, name):
       self.name = name
       self.token = token

        
    
        
class Game:
    def __init__ (self):
        self.count = 0
        self.game = ['0', '1', '2', '3', '4', '5', '6', '7', '8']
        self.board = [' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ']
       
      
    def instructions(self):
        return 'Using the below example, please enter the corresponding number you wish to place an X: ' 

    
    
    def first_image(self): # shows the players the relationship between spot within the grid and corresponding number. 
        return f"""
        {self.game[0]}|{self.game[1]}|{self.game[2]} 
        {self.game[3]}|{self.game[4]}|{self.game[5]}
        {self.game[6]}|{self.game[7]}|{self.game[8]}
        """

    def __repr__(self): # This is the board that is going to be called more than once.
        
        return f"""
        {self.board[0]}|{self.board[1]}|{self.board[2]} 
        {self.board[3]}|{self.board[4]}|{self.board[5]}
        {self.board[6]}|{self.board[7]}|{self.board[8]}
        """
    def move(self, move, token):
        
        while True:
            
            if move <= 8:
                if self.board[move] == ' ':
                    self.count += 1
                    self.board[move] = token
                    print(self.count)
                    return print(self)
                elif self.board[move] == 'x' or self.board[move] == 'o':
                    print('Spot has already been chosen') 
                    return False
            else:
                print('Enter a valid number!')
                return False
                  

    

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
    name_1 = input('What is your name?: ')
    name_2 = input('What is your name?: ')

    player_1 = Player('x', name_1)
    player_2 = Player('o', name_2) 
    print(game.instructions())
    
    
    while True:
        
        game.is_full()
        print(game.first_image()) # inserted this here instead of only once becausse I always wish I had a quick reference. 
        print(f'Player on deck: {player_1.name}\nPlayers token = {player_1.token}')
        while True:
            move = int(input('Spot number 0-8?: '))
            if game.move(move, player_1.token) == False:
                continue
            else:
                break
                
        if game.calc_winner(player_1.name) == False:
            while True:
                again = input('Would you like to play again?: ').lower()
                if again == 'yes' or again == 'y':
                    game.board = [' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ']
                    game.count = 0
                    main()
                elif again == 'no' or again == 'n':
                    quit()
                else:
                    print('Please enter Yes or No')
                    continue
      
        game.is_full()
        print(game.first_image())
        print(f'Player on deck: {player_2.name}\nPlayers token = {player_2.token}')
        while True:
            move = int(input('Spot number 0-8?: '))
            if game.move(move, player_2.token) == False:
                continue
            else:
                break
        if game.calc_winner(player_1.name) == False:
            while True:
                again = input('Would you like to play again?: ').lower()
                if again == 'yes' or again == 'y':
                    game.board = [' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ']
                    game.count = 0
                    main()
                elif again == 'no' or again == 'n':
                    quit()
                else:
                    print('Please enter Yes or No')
                    continue
        
           
    
    


    
   


main()

    
    