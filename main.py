from word_grid import *
import argparse
from colored import fg
import timeit

parser = argparse.ArgumentParser(description="Generates a word search puzzle")

parser.add_argument("-c", "--cheated", action="store_true", help = "Hightlight words")
parser.add_argument("-f", "--file", type=str, default="words.txt", help = "Path to a custom words file. One word per line.")
parser.add_argument("-s", "--size", type=int, default=20, help = "Sets a custom grid size (Default: 20)")

args = parser.parse_args()


def main(cheated=False, words_file=None, size=10):
	words = []
	file1 = open('E:\Python\ANALGOTRY\words.txt','r')
	lines = file1.readlines()
	file1.close()

	for _ in range(10):
		words.append(lines[random.randint(0, len(lines)-1)].strip())

	grid = WordGrid(size)
	
	print("┌────────────────────┐")
	print("│ Word Search Puzzle │")
	print("└────────────────────┘")
		
	count = 0
	isNext =True
	answers=[]

	grid.cheated = False
	grid.generate_with_words(words)
	print(words)
	print()
	print('If u wanna try this game, you can follow the words above!')
	print('It is only 10 answer in this game!')
	user = input('START (Y/N) : ')
	if user == 'y':
		while isNext :
			answer = input("Your Answer : ")
			if ((answer in words) and (answer not in answers)):
				print("Your Answer Is True !!!")
				answers.append(answer)
			elif answer =="check":
				print(answers)
			elif answer =="end":
				print('You stop the game')
				isNext = False
			else:
				print("Your Answer Is False !!!")
			
		
			if(len(words) == len(answers)):
				isNext = False
				print("Your Game Is Complete!")
		print()
	elif user == 'n':
		pass
	
if __name__ == "__main__":
	main(cheated=args.cheated, words_file=args.file, size=args.size)
