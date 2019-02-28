import re

class LargestWord:
#                                                                            -
# This function takes a string and returns a string with the largest word in 
# case of a single word or returns a list of largest words in case of a tie.
#
	def getLargestWords( self, string ):
		wordList = self.getWordList( string )
		largestLength = self.getLargestLength( wordList )
		largestWords = []
		for word in wordList:
			if( len(word) == largestLength ):
				largestWords.append( word )
		if( len(largestWords) == 1 ):
			return largestWords[0]
		else:
			return largestWords

	def getWordList( self, string ):
		wordList = re.sub( "[^\w]", " ", string ).split()
		return wordList

	def getLargestLength( self, wordList ):
		largestLength = 0
		for word in wordList:
			length = len(word)
			if( length > largestLength ):
				largestLength = length
		return largestLength

def test():
	global c
	c = LargestWord()

test()