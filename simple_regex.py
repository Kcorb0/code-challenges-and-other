def is_prime(num):
	print(num)
	if num >= 2:
		for i in list(range(2, 100000)):
			if (num % i) == 0 and num != i:
				return False
		else:
			print(str(num) + " / " + str(i))
			return True

	else:
		return False


print(is_prime(575088361))