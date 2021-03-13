# Perdiodic Table Tester (PTT)
import random as rn

names = 
symbols =
atomic_weight = None


def pick_element():
	n = rn.randint(1, 12)
	name = periodic_dic[n][0]
	symbol = periodic_dic[n][1]
	atomic_w = periodic_dic[n][2]

	return f"name: {name}\n" f"symbol: {symbol}\n" f"atomic_weight: {atomic_w}\n"


print(pick_element())