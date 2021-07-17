class Player:
    def _init_(self, name, token):
       self.name = name
       self.token = token # X or O
        
class Game:
    def __init__ (self, move, image_1):
        self.image_1 = image_1
        self.move = move
        self.__repr__ = repr
        
        
    
    def __repr__(self):
        tic_image = self.image_1
        return tic_image
    
    def image_1(self):
        # image_13 = {
        #     0:" |", 1:" ", 2:" ",
        #     3:" |", 4:" ", 5:" ",
        #     6:" |", 7:" ", 8:" ",
        # }
        #return dict.keys(tic_image)
        board = '''f(
        {1}|
        
        )'''
        return board
    
    def move(x, y, player):
        pass
    

    def clac_winner():
        pass
    
    def is_full():
        pass
    
    def is_game_over():
        pass

game = Game(None, None)    
player = Player()


print(game.image_1)




    
    