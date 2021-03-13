def fib(n):
	"""Print a fibonacci sequence up to n"""
	
	sequence = []
	a, b = 0, 1

	while a < n:
		sequence.append(str(a))
		a, b = b, a+b

	return "-".join(sequence)

print(fib(10000000))
