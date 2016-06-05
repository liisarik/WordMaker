def tryCombinationsRecursive(index, combination, letters, words, maxLetters):
	foundWords = []
	for i in range(len(letters)):
		letter = letters[i]
		combination += letter.lower()
		if combination in words:
			foundWords.append(combination)
		if index < maxLetters:
			remainingLetters = letters[:i] + letters[i+1:]
			subWords = tryCombinationsRecursive(index + 1, combination, remainingLetters, words, maxLetters)
			for word in subWords:
				if not word in foundWords:
					foundWords.append(word)
		combination = combination[:-1]
	return foundWords

def loadWords():
	with open("words.txt", "r") as file:
		lines = [line.rstrip("\n").lower() for line in file]
		return lines

def findWords(letters):
	words = loadWords()
	found = tryCombinationsRecursive(1, "", letters, words, len(letters))
	return found

letters = input("Insert letters: ")
words = findWords(letters)
words.sort(key=len, reverse=True)
for word in words:
	print(word)