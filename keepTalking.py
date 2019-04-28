
def main():
	print("1: button")
	print("2: 6 horizontal wires")
	print("3: 123abc wires")
	print("4: led star wires")
	puzzle = input("which puzzle do you have: ")

	if int(puzzle) == 1: button()
	elif int(puzzle) == 2: horizontal6wires()
	elif int(puzzle) == 3: abc123wires()
	elif int(puzzle) == 4: ledStarWires()
	else:
		print("invalid selection")
		main()

def button():
	print("button")
	pass

def horizontal6wires():
	print("horizontal 6")
	pass

def abc123wires():
	print("abc123wires")
	pass

def ledStarWires():
	print("ledStarWires")
	pass


	# simon would be hard

main()
