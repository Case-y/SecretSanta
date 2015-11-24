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
			return pairing(names)

		elif name in names:
			assert False, "Um... next time specify differences with same names."

		else:
			names.append(name)
			return data()

	return data()

def pairing(names):
	pair = {}
	repeats = []
	last = names[:]
	if len(names) <= 1:
		assert False, "You can't do the Secret Santa. I'm sorry."

	def ship(names):
		length = len(names)
		if length == 1:
			for chosen_one in last:
				if chosen_one not in repeats:
					last_person = chosen_one

			pair[names[0]] = last_person

			print("Here are your secret santas and the receivers.")
			print("")
			
			check_repeats(pair)

			for person, receiver in pair.items():
				print (person + ": " + receiver)

			print("")
			return print("Enjoy Christmas!")

		assignment = random.randint(0, length - 1)
		binding = random.randint(0, len(last) - 1)

		if last[binding] in repeats:
			return ship(names)
		elif names[assignment] == last[binding]:
			return ship(names)
		else:
			pair[names[assignment]] = last[binding]
			name_remove = names[assignment]
			repeats.append(last[binding])
			names.remove(name_remove)
			return ship(names)

	return ship(names)


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




















