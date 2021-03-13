def generate_hashtag(s):
	return "#"+"".join([i for i in s.title().split(" ")]) if len(s) <= 140 and s!= "" else False


print(generate_hashtag('poggie woggie my dudies'))