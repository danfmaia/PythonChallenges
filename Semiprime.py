class Semiprime:
#                                                                            -
# This function checks if the given natural number is semiprime, that is, if
# it's a natural number that is a product of exactly two (not necessarily
# distinct) primes.
# 
	def isSemiprime( self, x ):
		x = int(x)
		if( x < 2 ):
			return False
		primesBetween = self.getPrimesBetween( 2, x//2 + 1 )
		for i in primesBetween:
			if( x%i == 0 ):
				y = x/i
				if( self.isPrime(y) ):
					return True
		return False
#                                                                            -
# This function returns a list of all semiprimes in a given range of natural
# numbers. (b is exclusive, following Python's practice)
#
	def getSemiprimesBetween( self, a, b=None ):
		if( b == None ):
			if( a <= 2 ):
				raise Exception( "Single argument should be greater 2" )
			b = a
			a = 2
		if( b <= a ):
			raise Exception( "b should be greater than a" ) 
		temp = []
		for i in range( a, b ):
			if( self.isSemiprime(i) ):
				temp.append(i)
		return temp

	def isPrime( self, x ):
		if( x < 2 ):
			return False
		for i in range( 2, x//2 + 1 ):
			if( x%i == 0 ):
				return False
		return True

	# (b is exclusive, following Python's practice.)
	def getPrimesBetween( self, a, b ):
		temp = []
		for i in range( a, b ):
			if( self.isPrime(i) ):
				temp.append(i)
		return temp

def test():
	global c
	c = Semiprime()

test()