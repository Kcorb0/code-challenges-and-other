
for rows in range(0, 30):
	for cols in range(0, 30-rows):
		print(" ", end="")
	for i in range(0, rows*2+1):
		print("/", end="")
	print("\\")
