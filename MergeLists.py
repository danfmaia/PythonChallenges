class MergeLists:
#                                                                            -
# This function takes 2 list of numbers and returns a merged and sorted single
# list will all elements of the given lists. InsertionSort algorithm is used
# for sorting.
#
	def sortMergeLists( self, list_a, list_b ):
		if( not self.isSorted(list_a) ):
			sorted_a = self.insertionSort(list_a)
		if( not self.isSorted(list_b) ):
			sorted_b = self.insertionSort(list_b)

		temp = []
		j = 0
		for i in range(len(sorted_a)):
			while( sorted_b[j] < sorted_a[i] ):
				temp.append( sorted_b[j] )
				j += 1
			temp.append( sorted_a[i] )
		for j in range(j, len(sorted_b)):
			temp.append( sorted_b[j] )

		return temp

	def isSorted( self, list ):
		if( type(list) == list ):
			raise Exception( "Argument is not a list" )
		if( len(list) == 0 ):
			raise Exception( "List can't be empty" )
		last_i = list[0]
		for i in list:
			if( i < last_i ):
				return False
			last_i = i
		return True

	def insertionSort( self, list_in ):
		list = list_in[:]

		for i in range( 1, len(list) ):
			
			j = i - 1
			while (list[j] > list[j+1]) and (j >= 0):
				list[j], list[j+1] = list[j+1], list[j]
				j -= 1
				
		return list

def test():
	global c
	c = MergeLists()

test()
a = [-4,5,-4,0,0,3,5,-2,10]
b = [0,1,-3,13,-2,3]