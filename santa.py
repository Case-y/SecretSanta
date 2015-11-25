import random

def create():
	names = []
	print("Enter names.")
	print("If there are no more names, put N/A.")
	def data():

		name = input("Name?: ")

		if name == "N/A":
			print("Here is the list of participants.")
			print("")
			print(names)
			print("")
			return pairings(names, "Casey", "Ken")

		elif name in names:
			assert False, "Um... next time specify differences with same names."

		else:
			names.append(name)
			return data()

	return data()

# def pairing(names):
# 	pair = {}
# 	repeats = []
# 	last = names[:]
# 	if len(names) <= 1:
# 		assert False, "You can't do the Secret Santa. I'm sorry."
#
# 	def ship(names):
# 		length = len(names)
# 		if length == 1:
# 			for chosen_one in last:
# 				if chosen_one not in repeats:
# 					last_person = chosen_one
#
# 			pair[names[0]] = last_person
#
# 			print("Here are your secret santas and the receivers.")
# 			print("")
#
# 			check_repeats(pair)
#
# 			for person, receiver in pair.items():
# 				print (person + ": " + receiver)
#
# 			print("")
# 			return print("Enjoy Christmas!")
#
# 		assignment = random.randint(0, length - 1)
# 		binding = random.randint(0, len(last) - 1)
#
# 		if last[binding] in repeats:
# 			return ship(names)
# 		elif names[assignment] == last[binding]:
# 			return ship(names)
# 		else:
# 			pair[names[assignment]] = last[binding]
# 			name_remove = names[assignment]
# 			repeats.append(last[binding])
# 			names.remove(name_remove)
# 			return ship(names)
#
# 	return ship(names)

def pairings(names, *santa_overlords):
	"""Returns the overall pairings, and prints the pairings that each santa
	overlord should assign, so that no overlord will know their own santa."""
	length = len(names)
	assert length > 1, "You can't do the Secret Santa. I'm sorry."
	assert len(santa_overlords) == 2, "There must be 2 santa overlords, thx."
	current, left = [], [i for i in range(length)]

	# Forming pairs
	for i in range(length):
		this = random.choice(left)
		while this == i:
			if len(left) == 1:
				return pairings(names, *santa_overlords) # redo pairings
			this = random.choice(left)
		current.append(this)
		left.remove(this)

	pairs = {names[i] : names[current[i]] for i in range(length)}

	# Distributing assignments to the santa overlords
	overlord_books = [{} for lord in santa_overlords]
	who = 0
	for first in pairs:
		if pairs[first] == santa_overlords[who]:
			overlord_books[1-who][first] = pairs[first]
		else:
			overlord_books[who][first] = pairs[first]
		who = 1 - who

	# Printing everything out
	for i in range(2):
		with open("Overlord_%s.txt" %santa_overlords[i], "w") as f:
			f.write("Overlord " + santa_overlords[i] + " will assign the following:\n")
			result = "\n".join([first + " gifts to " + overlord_books[i][first] + "!" for first in overlord_books[i]])
			f.write(result)

	print("Overall pairings:\n")
	print_holiday_dict(pairs)
	print("Enjoy Christmas!")
	return pairs

def print_holiday_dict(pairings):
	"""Prints the dictionary of pairings in festive form."""
	for first in pairings:
		print(first, "gifts to", pairings[first] + "!")

def check_repeats(dictionary):
	santas = dictionary.keys()
	receivers = dictionary.values()
	for santa, receiver in zip(santas, receivers):
		if santa not in dictionary.values():
			assert False, "Probability Error... Randomization Failed"

		if receiver not in dictionary.keys():
			assert False, "Probability Error... Randomization Failed"

		if santa == receiver:
			assert False, "Probability Error... Randomization Failed"

def recursion():
	create()
	recursion()

recursion()
