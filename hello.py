def  factorial(n):
	if n==0:
	    return 1
	else:
	    return n*factorial(n-1)
number = 5
number2 = 7
result =factorial(number)
print(f"The factorial of {number} is {result}.")
print(f"Another line to make a conflict.")
