from math import sqrt
from alphabet import *
import random
import os

HORIZONTAL 	= 0
VERTICAL	= 1

class WordGrid:
	def __init__(self, width) -> None:
		self.grid = []
		self.width = width
		self.area = width**2
		self.cheated = False

		for col in range(self.area):
			self.grid.append(get_random_letter())

		self.available_spots = []

		for spot in range(self.area):
			self.available_spots.append(True)

	def generate_with_words(self, words):
		if self.can_generate(words):
			for word in words:
				finded_place_to_enter_word = False
				attempt = 0
				while not finded_place_to_enter_word and attempt <= 100:

					random_direction = random.choice([HORIZONTAL, VERTICAL])

					random_x = random.randint(0, self.width-1)
					random_y = random.randint(0, self.width-1)


					if random_x + len(word) > self.width and random_direction == HORIZONTAL:
						random_x -= (random_x + len(word)) - self.width
					if random_y + len(word) > self.width and random_direction == VERTICAL:
						random_y -= (random_y + len(word)) - self.width
					
					
					if self.is_placeable(word, random_x, random_y, random_direction):
						self.place_word(word, random_x, random_y, random_direction)
						finded_place_to_enter_word = True
					
					attempt += 1
					
			if attempt >= 100:
				i = input("Error: Could not place some words (out of space), print the puzzle anyway? [y/n] ")
				if i.casefold() == 'y':
					self.print()
				else:
					exit()
			else:
				self.print()

	def place_word(self, word, x, y, direction):
		for l in range(len(word)):
			if direction == HORIZONTAL:
				self.grid[x+l + y * self.width] = "\033[32m" + word[l] + "\033[0m" if self.cheated else word[l]
				self.available_spots[x+l + y * self.width] = False 
			elif direction == VERTICAL:
				self.grid[x + (y+l) * self.width] = "\033[32m" + word[l] + "\033[0m" if self.cheated else word[l]
				self.available_spots[x + (y+l) * self.width] = False 
			
	def is_placeable(self, word, x, y, direction):
		for l in range(len(word)):

			letter = "\033[32m" + word[l] + "\033[0m" if self.cheated else word[l]

			if direction == HORIZONTAL:
				if self.grid[x+l + y * self.width] == letter:
					self.available_spots[x+l + y * self.width] = True
			else:
				if self.grid[x + (y+l) * self.width] == letter:
					self.available_spots[x + (y+l) * self.width] = True
			spot_available = self.available_spots[x+l + y * self.width] if direction == HORIZONTAL else self.available_spots[x + (y+l) * self.width]

			if spot_available:
				continue
			else:
				return False
		return True

	def can_generate(self, words):
		letter_count = 0
		for word in words:
			for letter in word:
				letter_count += 1
				if letter_count > self.area:
					print("\nToo many words for a little grid!")
					return False
			if len(word) > self.width:
				print(f"\nYou entered a word too big for the grid size! (Grid size: {self.width})")
				return False
		return True

	def print(self):

		print("\033[96m┌" + ("─"*(2*(self.width)+1)) + "┐\033[0m" ) 
		for y in range(self.width):
			print("\033[96m│\033[0m", end=" ")
			for x in range(self.width):
				print(self.grid[x + y * self.width], end=" ")
			print("\033[96m│\033[0m")
		print("\033[96m└" + ("─"*(2*(self.width)+1)) + "┘\033[0m" )
