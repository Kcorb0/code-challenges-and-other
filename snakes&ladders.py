# Dice rules
# Rule 1: if both dice rolls are the same player gets another go
# Rule 2:


class SnakesLadders:

	def __init__(self):
		self.players = [0, 0]
		self.turn = 0
		self.ladders = {2:38, 7:14, 8:31, 15:26, 21:42, 28:84, 36:44, 51:67, 71:91, 78:98, 87:94}
		self.snakes = {16:6, 46:25, 49:11, 62:19, 64:60, 74:53, 89:68, 92:88, 95:75, 99:80}

	def play(self, die1, die2):
		total = die1+die2
		turn = self.turn
		player_score = self.players[turn]
		player_position = player_score + total

		if 100 in self.players:
			return 'Game over!'
		else:
			if player_position == 100:
				print(player_position)
				self.players[turn] = 100
				return f'Player {turn+1} Wins!'

			elif player_position > 100:
				player_position = 100 - (player_position - 100)

			for key, val in self.ladders.items():
				if player_position == key:
					player_position = val

			for key, val in self.snakes.items():
				if player_position == key:
					player_position = val

			self.players[turn] = player_position

			if die1==die2:
				self.turn = self.turn
			elif self.turn == 0:
				self.turn = 1
			else:
				self.turn = 0

			return f'Player {turn+1} is on square {player_position}'

game = SnakesLadders()

print(game.play(20, 20))
print(game.play(20, 20))
print(game.play(10, 10))
print(game.play(10, 10))
print(game.play(10, 10))
print(game.play(10, 10))



