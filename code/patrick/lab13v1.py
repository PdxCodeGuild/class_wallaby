


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
        self.count += 1
        x = int(input('Spot number 0-8: '))
        self.board[x] = 'x'
        # win condition calc_winner
        print(self.count)
        print(game)
    def move_2(self):   
        self.count += 1
        x = int(input('Spot number 0-8: '))
        self.board[x] = 'o'
        print(self.count)
        print(game)
         
        
    
    # def move_2(self):
    #     x = int(input('Spot number 0-8: '))
    #     self.board[x] = 'o'
    #     return self.board
    

    def calc_winner(self):
        if self.board == ['x', 'x', 'x', ' ', ' ', ' ', 'o', 'o', 'o']:
            print('winner')
        else:
            return False
    
    def is_full(self):
        if game.count >= 10:
            print('game is a draw!')
            again = input('Would you like to play again?: ').lower()
            if again == 'yes' or again == 'y':
                game.board = [' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ']
                game.count = 0
                return True
            else:
                return False
    
    def is_game_over():
        pass

game = Game()    
player = Player()



def main():
    print(game.first_image)
    print(game.instructions())
    game_running = True
    
    while game_running:
        game.is_full()
        game.move_1()
        # if game.count > 10:
        #     print('game is a draw!')
        #     again = input('Would you like to play again?: ').lower()
        #     if again == 'yes' or again == 'y':
        #         game.board = [' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ']
        #         game.count = 1
        #         True
        #     else:
        #         break
        game.is_full()
        game.move_2()
      
        # game.calc_winner()
        
            
    
    


    
    # game.move()
    # print(game)


main()

    
    