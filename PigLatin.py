class PigLatin :
#                                                                            -
# This function takes a letter string and returns that string converted to Pig
# Latin.

# If the word starts with a consonant (excluding y) or consonant
# cluster, they will be transfered to the end with -ay appended next.
# 
# If the word starts with a vowel (including y), no letter is transfered and
# -yay is appended to the end.
#
	def english_to_pigLatin( self, string_in ) :
		string = list(string_in.lower())

		if self.isConsonant( string[0] ) :
			cluster = []
			while self.isConsonant( string[0] ) :
				cluster.append( string[0] )
				string.pop(0)
		else :
			cluster = ['y']

		# print "cluster:", cluster
		# print "string", string

		temp = string + cluster + ['a', 'y']
		temp = "".join( temp )
		return temp


	def isConsonant( self, char ) :
		if char in ('a', 'e', 'i', 'o', 'u', 'y') :
			return False
		return True

def test() :
	global c
	c = PigLatin()

test()