

class ScientificNotation :
#
# Takes a number string and converts it to scientific notation.
#
	def toNotation ( self, number ) :

		def removeFinalZeros( number ) :
			i = -1
			while number[i] == ('0') :
				i -= 1
			i += 1
			temp = number[:i]
			return temp

		if not isinstance( number, str ) :
			raise Exception( "Value is not a string" )

		# Checks if the entered string corresponds to an integer
		try:
			float( number )
		except:
			raise Exception( "String does not correspond to an integer" )

		#Removes minus sign if it has it, and records that
		if number[0] == '-' :
			negative = True
			number = number[1:]
		else :
			negative = False

		#Removes starting zeros if the number has any 
		i = 0
		while number[i] == '0' :
			i += 1
			if i == len(number) :
				return '0'
		number = number[i:]

		# Finds dot position if it has a dot, or returns -1
		position = number.find('.')

		# Treats numbers starting with dot character
		if position == 0 :
			if number == '.' :
				return '0'
			i = 1
			while number[i] == '0' :
				i += 1
				if i == len(number) :
					return '0'

			if len( number[i+1:] ) > 0 :
				temp = number[i] + '.' + number[i+1:]
			else :
				temp = number[i]

			power = i
			temp = temp + " * 10^-" + str(power)

		# Treats numbers starting with numeral character
		if position != 0 :
			if position == -1 :
				position = len(number)
				temp = number
			else :
				print 'passou'
				temp = removeFinalZeros( number )
				temp = temp.replace( '.', '' )
			
			if len( temp[1:] ) > 0 :
				temp = temp[0] + '.' + temp[1:]
			else :
				temp = temp[0]

			power = position - 1
			if power > 0 :
				temp = temp + " * 10^" + str(power)

		# Gives back the minus sign if number was negative
		if negative == True :
			temp = '-' + temp

		return temp


def test():
	global o
	o = ScientificNotation()

test()