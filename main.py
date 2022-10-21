import string

with open('./words.txt', 'r') as f:
	answers = f.read().split()


letters = {
	"firstLet": list(string.ascii_lowercase),
	"secondLet": list(string.ascii_lowercase),
	"thirdLet": list(string.ascii_lowercase),
	"fourthLet": list(string.ascii_lowercase),
	"fifthLet": list(string.ascii_lowercase)
}

print(letters[list(letters.keys())[0]])
possibleGuesses = answers
print(possibleGuesses)
newPossibleGuesses = []
isInWord = []
guess = input("Guess a five letter word\n\n|")
passnum = 0

while True:
	passnum += 1
	if len(possibleGuesses) == 1:
		break
	if passnum > 1:
		print(possibleGuesses)
		guess = input("Type a word in the list\n\n|")
	print("\nType G for green, B for black and Y for yellow")
	for letter in range(len(list(guess))):
		letOneInfo = input(f"{list(guess)[letter]} = ").upper()
		if letOneInfo == "G":
			isInWord.append(list(guess)[letter])
			letters[list(letters.keys())[letter]] = [list(guess)[letter]]
			
		elif letOneInfo == "Y":
			isInWord.append(list(guess)[letter])
			letters[list(letters.keys())[letter]].remove(list(guess)[letter])
		else:
			for x in range(5):
				if list(guess)[letter] in letters[list(letters.keys())[x]] and not(list(guess)[letter] in isInWord):
					letters[list(letters.keys())[x]].remove(list(guess)[letter])
	newPossibleGuesses = []
	for guesses in possibleGuesses:
		flagged = False
		if guesses[0] in letters["firstLet"]:
			if guesses[1] in letters["secondLet"]:
				if guesses[2] in letters["thirdLet"]:
					if guesses[3] in letters["fourthLet"]:
						if guesses[4] in letters["fifthLet"]:
							for definiteLets in isInWord:
								if definiteLets in guesses: continue
								else:
									flagged = True
									break
							if flagged: continue
							print("Added word")
							newPossibleGuesses.append(guesses)
	possibleGuesses = newPossibleGuesses


input(f"Word is {possibleGuesses[0]}")
