def find_screen_height(width, ratio):
	rat = ratio.split(":")
	return str(width) + "x" + str(int(int(rat[1])/int(rat[0])*width))

print(find_screen_height(1024, "4:3"))