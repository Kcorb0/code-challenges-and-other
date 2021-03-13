import unittest

def generate_hashtag(s):
	return "#"+"".join([i for i in s.title().split(" ")]) if len(s) <= 140 and s!= "" else False



class MyTest(unittest.TestCase):
	def test_hashtag(self):
		self.assertEqual(generate_hashtag('poggie woggie my dudies'), "#PoggieWoggieMyDudies")
		self.assertEqual(generate_hashtag('poggie woggie my dudies')[0], "#")

if __name__ == '__main__':
	unittest.main()