""" Hangman V0.1.0 """
""" Using datamuse to get a word """
""" TODO:
	create a base of seed words to lated use 
	to fetch a random word from datamuse
"""
import random 
from datamuse import datamuse


class Game():
	"""docstring for game"""
	def __init__(self, already_guessed, counter):
		self.already_guessed = already_guessed
		self.counter = counter
		self.words_defs = self.random_word()
		self.word = self.words_defs[0]
		self.definitions = self.words_defs[1]
		self.display = self.display(self.word)
		self.username = self.intro()
		self.is_win = False

	def display(self,word):
		return "_"*len(word)
		
	def intro(self):
		print(f'\nHangman v0.3')
		username = input('Input username: ')
		print(f'{username} The game about to start\n')
		return username

	def random_word(self):
		""" fetch a random word, it use some seeds words to get a 
		random word from datamuse """

		seeds = ["january","border","image","film","promise","kids","lungs","doll","rhyme","damage","plants"]

		word_base = random.choice(seeds)
		api = datamuse.Datamuse()
		word_list = api.words(ml=word_base, md='d')
		word = word_list[0]['word']
		definitions = word_list[0]['defs']


		return word, definitions


def validate_guess(game, guess: str):
	""" validate Guess """

	if guess in game.word:
		match = [i for i, ch in enumerate(game.word) if guess == ch]
		for index in match:
			game.display = game.display[:index] + guess + game.display[index+1:]
			
		print(f'-->{game.display}\n')
		if game.display == game.word:
			game.is_win = True
			print(f"\n\n*****you win*****\n")
	else:
		print(f'Try again :( {game.counter} of 5\n\t')
		print(f'Here a definition to help: \n{random.choice(game.definitions)}')
		if game.counter >= 5:
			game.is_win = True
			print(f'the word was ** {game.word} **')
		game.counter += 1

def user_input(game):
	""" Get the user input and validate it"""
	while not game.is_win:
		guess = input("\n>Enter your Guess: ")
		guess = guess.strip().lower()

		if guess.isnumeric():
			print(f"please enter a letter\ninput was {guess}")
		elif len(guess) >= 2:
			if guess == game.word:
				game.is_win = True
				print(f"\n\n*****you win*****\n")
			else:
				print(f'Please input just one letter at the time')
		elif guess in game.already_guessed:
			print(f"you already used {guess} please select another letter")
		elif guess.isalpha():
			game.already_guessed.extend([guess])
			print(f'* Previous letters {game.already_guessed}') 
			validate_guess(game,guess)
		else:
			# TODO: Display the space
			print(f" you selected {guess}, please use just letters")    

def main():
	game = Game([],1)
	print(f"{game.display}\n")
	while game.counter <= 5 :
		user_input(game)
		if game.is_win:
			break
	print("Game Over\n")    



if __name__ == "__main__":
	main()