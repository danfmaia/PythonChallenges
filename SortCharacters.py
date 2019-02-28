class SortCharacters :
#                                                                            -
# This function takes a string and returns a string with the same characters
# in ascending order concerning their ASCII codes.
#
	def sortCharacters( self, string ):
		charList = []
		for char in string:
			charList.append( char )

		list = []
		for char in charList:
			list.append( [ord(char), char] )

		sortedList = []
		sortedList.append( list[0] )
		for i in range( 1, len(list) ):
			sortedList.append( list[i] )
			for j in range( len(sortedList)-1, 0, -1 ):
				if( sortedList[j-1][0] > sortedList[j][0] ):
					sortedList[j-1], sortedList[j] = sortedList[j], sortedList[j-1]
		
		sortedString = []
		for pair in sortedList:
			sortedString.append( pair[1] )
		sortedString = ''.join(sortedString)

		return sortedString


def test():
	global c
	c = SortCharacters()

test()