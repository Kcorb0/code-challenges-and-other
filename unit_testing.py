def rgb(r, g, b):
	hexd = list(list(range(0,10))+list("ABCDEF"))
	rgb = [r, g, b]
	rgb_hex = []

	for i in rgb:
		if int(i) >= 0 and int(i)<=255:
			value = i/16
			sep = str(value).split(".")
			hex_val = str(hexd[int(value)]) + str(hexd[int(float("0."+sep[1])*16)])
			rgb_hex.append(hex_val)
		elif int(i)>255:
			rgb_hex.append('FF')
		else:
			rgb_hex.append('00')

	return "".join(rgb_hex)

print(rgb(-20,275,125))