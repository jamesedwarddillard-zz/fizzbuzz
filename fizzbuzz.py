"""Version 1 -- FizzBuzz

Requirements: 

1) first print fizzbuzz counting up to n
2) Then the program should print out each number from 1 to n
a) replace numbers divisible by 3 with fizz
b) replace numbers divisible by 5 with buzz
c) replace numbers divisible by 3 and 5 with FizzBuzz"""

def fizzbuzz(n):
	print 'FizzBuzz counting up to %s' % str(n)

	for i in range(n):

		i += 1

		if i % 3 == 0:

			if i % 5 == 0:

				print 'Fizz Buzz'

			else:

				print 'Fizz'

		elif i % 5 == 0:

			print 'Buzz'

		else:

			print i 

fizzbuzz(100)