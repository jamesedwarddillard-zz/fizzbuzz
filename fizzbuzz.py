"""Version 1 -- FizzBuzz

Requirements: 

1) first print fizzbuzz counting up to n
2) Then the program should print out each number from 1 to n
a) replace numbers divisible by 3 with fizz
b) replace numbers divisible by 5 with buzz
c) replace numbers divisible by 3 and 5 with FizzBuzz"""

#User entry
import sys

def divisible(a, d): #added divisible function
	if a % d == 0:
		return True
	else: 
		return False

def fizzbuzz(n = 127): #added fizzbuzz function

	try:
		n = sys.argv[1]
	except IndexError:
		n = raw_input('How high should I fizz buzz?')

	try:
		n = int(n)
	except ValueError:
		print 'Sorry, I can only fizz buzz with numbers (e.g., 7 instead of seven)'
		try:
			n = int(raw_input('Can you give me a number to fizz buzz to?'))
		except ValueError:
			n = 127 #added this because the default value wasn't coming throught... we should talk about why
			print 'Okay, 127 it is!'

	# requirement 1
	print 'FizzBuzz counting up to %s' % n

	#counting
	for i in range(n):
		i += 1
		if divisible(i, 3):
			if divisible(i, 5):
				print 'FizzBuzz',
			else:
				print 'Fizz',
		elif divisible(i, 5):
			print 'Buzz',
		else:
			print i, 

if __name__ == '__main__':
	fizzbuzz()