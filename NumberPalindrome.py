class NumberPalindrome:
#                                                                            -                                                                       
# This function takes a list of single digit numbers and checks if it's
# possible to create a palindrome from them. A palindrome is a sequence of
# characters that reads the same backward as forward.

	def isPalindromeable( self, list ):
		assert list is list, "Argument is not a list: %r" % list

		if (len(list) % 2) == 0 :
			for i in range(10) :
				if (list.count(i) % 2) == 1 :
					return False
		else:
			oddCount = 0
			for i in range(10) :
				if (list.count(i) % 2) == 1 :
					oddCount += 1
				if oddCount > 1 :
					return False

		return True

def test():
	global c
	c = NumberPalindrome()

test()