class Composite:
#                                                                            -
# This function takes a positive integer and checks if it's a composite
# number, that is, if it's not a prime number.
# 
	def isComposite( self, x ):
		x = int(x)
		if( x < 4 ):
			return False
		for i in range( 2, x//2 + 1 ):
			if( x%i == 0 ):
				return True
		return False
#                                                                            -
# This function returns a list with all composite numbers in the given range.
# If a single argument is given, the sequence will start in 1 and end in the
# given argument.
# 
	def getCompositesBetween( self, a, b=None ):
		if( b == None ):
			if( a <= 1 ):
				raise Exception( "Single argument should be greater than 1" )
			b = a
			a = 1
		if( b <= a ):
			raise Exception( "b should be greater than a" ) 
		temp = []
		for i in range( a, b ):
			if( self.isComposite(i) ):
				temp.append(i)
		return temp

def test():
	global c
	c = Composite()

test()