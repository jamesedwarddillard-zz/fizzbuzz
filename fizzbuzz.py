"""Version 1 -- FizzBuzz

Requirements: 

1) first print fizzbuzz counting up to n
2) Then the program should print out each number from 1 to n
a) replace numbers divisible by 3 with fizz
b) replace numbers divisible by 5 with buzz
c) replace numbers divisible by 3 and 5 with FizzBuzz"""

#User entry
import sys

def divisible(n, d): #added divisible function
	if n % d == 0:
		return True
	else: 
		return False

try:
	n = sys.argv[1]
except IndexError:
	n = raw_input('How high should I fizz buzz?')

try:
	n = int(n)
except ValueError:
	print 'Sorry, I can only fizz buzz with numbers (e.g., 7 instead of seven)'
	n = int(raw_input('Can you give me a number to fizz buzz to?'))

# requirement 1
print 'FizzBuzz counting up to %s' % n

#counting
for i in range(n):
	i += 1
	if i % 3 == 0:
		if i % 5 == 0:
			print 'FizzBuzz',
		else:
			print 'Fizz',
	elif i % 5 == 0:
		print 'Buzz',
	else:
		print i, 
