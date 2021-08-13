class Board:
	def __init__(self):
		self.board = ['X', 'O', 'X', 'O', 'X', 'O', 'X', 'O', 'X']
	
    def say_somethin(self):
		print('tic tac toe is fun')
	
	def __repr__(self):
		b = self.board
		return f"""
			{b[0]}|{b[1]}|{b[2]}
			{b[3]}|{b[4]}|{b[5]}
			{b[6]}|{b[7]}|{b[8]}
		"""
	
	def __getitem__(self, index):
		return self.board[index]
	
	def __lte__(self, _value):
			return False


game = Board()
print(game.__repr__())
from typing import ClassVar


#name = input(f'Enter your name: ')

#class Player:
    
    #def __init__(self,name,token):
     
        #self.name = name
        #self.token = token
    
#player_info = Player(input('Whats your name ?:'),('X' or 'O'))
#print(player_info)



#player = Player()
#name = player.name
#print(f'{name} {token}' )
