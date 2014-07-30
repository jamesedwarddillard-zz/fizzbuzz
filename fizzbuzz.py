"""Version 1 -- FizzBuzz

Requirements: 

1) first print fizzbuzz counting up to n
2) Then the program should print out each number from 1 to n
a) replace numbers divisible by 3 with fizz
b) replace numbers divisible by 5 with buzz
c) replace numbers divisible by 3 and 5 with FizzBuzz"""

import sys

def divisible(number, diviser): #divisible determines whether or not a number is divisible by another
	return number % diviser == 0

def fizzbuzz(n = 127): #fizzbuzz counts replacing numbers divisible by 3 w/ 'fizz', numbers divisible by 5 w/ 'buzz' and numbers divisible by both w/ 'fizzbuzz'
	print 'FizzBuzz counting up to %s' % n 
	#count up to n replacing 3s and 5s
	for i in range(1, n+1): 
		if divisible(i, 3):
			if divisible(i, 5):
				print 'FizzBuzz',
			else:
				print 'Fizz',
		elif divisible(i, 5):
			print 'Buzz',
		else:
			print i, 

#getting fizz buzz to run in the command line
if __name__ == '__main__':
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
			n = 127
			print 'Okay, 127 it is!'

	fizzbuzz(n)

