class PalindromeCreator:
#                                                                            -
# This function takes a string and checks if it's a palindrome, or tries to
# make a palindrome removing 1 or 2 characters from it. The palindrome created
# must have at least 3 characters. If it's possible to make a palindrome
# removing 1 or 2 characters, the function will return a string with those
# characters.
# 
# A palindrome is a sequence of characters that reads the same backward as
# forward.
#
	def main( self, str ):
		if len(str) < 3 :
			return 'not possible'
		temp = self.isPalindrome( str )
		if temp == True :
			return 'palindrome'

		if len(str) < 4 :
			return 'not possible'
		temp = self.removing_1( str )
		if temp != False :
			return temp
		
		if len(str) < 5 :
			return 'not possible'
		temp = self.removing_2( str )
		if temp != False :
			return temp
		else:
			return 'not possible'

	def removing_1( self, str ):
		for i in range(len(str)) :
			newStr = str[0:i] + str[i+1:len(str)]
			#print( newStr )
			if self.isPalindrome( newStr ) == True :
				return str[i]
		return False

	def removing_2( self, str ):
		for i in range(len(str)) :
			newStr = str[0:i] + str[i+1:len(str)]
			char2 = self.removing_1( newStr )
			if char2 != False :
				return str[i] + char2
		return False

	def isPalindrome( self, str ):
		for i in range(len(str)//2) :
			if str[i] != str[-i-1] :
				return False
		return True

def test():
	global c
	c = PalindromeCreator()

test()