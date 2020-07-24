'''
Background:
The fizzbuzz challenge is a classic coding interview problem, where the candidate must make a program that exhibits the following behavior:
Print the integers from 1 to 100 (inclusive), but if the integer is divisible 3, print Fizz, also if the integer is divisible 5, print Buzz, and if the integer is divisible by both, print FizzBuzz
'''
for i in range(1, 101):
  string = ''
  divisible = False
  if i % 3 == 0:
    string += 'Fizz'
    divisible = True
    
  if i % 5 == 0:
    string += 'Buzz'
    divisible = True
  
  if divisible:
    print(string)
    continue
  print(i)
    
