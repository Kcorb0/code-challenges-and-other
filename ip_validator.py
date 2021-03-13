def rot13(message):
	alpha = "ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz"
	rot13 = "NOPQRSTUVWXYZABCDEFGHIJKLMnopqrstuvwxyzabcdefghijklm"
	encoded = []

	for i in message:
		try:
			encoded.append(rot13[alpha.index(i)])
		except:
			encoded.append(i)

	return "".join(encoded)

print(rot13("Test!"))