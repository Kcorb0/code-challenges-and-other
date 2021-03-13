import re

def regex_word(string):

	return [i for i in string if re.search("^Jo",i)]


print(regex_word(["Josh", "Bob", "Joe", "Harry"]))
