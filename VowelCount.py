class VowelCount :
#                                                                            -
# This function takes a string and returns its vowel count (as integer).
#
	def countVowels( self, string ):
		count = 0
		for char in string:
			if( self.isVowel(char) == True ):
				count += 1
		return count

	def isVowel( self, char ):
		if( char.lower() in ['a','e','i','o','u'] ):
			return True

def test():
	global c
	c = VowelCount()

test()