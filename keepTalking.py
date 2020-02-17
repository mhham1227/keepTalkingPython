
def main():
	print("1: button")
	print("2: 6 horizontal wires")
	print("3: 123abc wires")
	print("4: led star wires")
	puzzle = int(input("which puzzle do you have: "))

	if int(puzzle) == 1: button()
	elif int(puzzle) == 2: horizontal6wires()
	elif int(puzzle) == 3: abc123wires()
	elif int(puzzle) == 4: ledStarWires()
	else:
		print("invalid selection")
		main()


def button():
	color = str(input("which color is the button: ")).lower()
	text = str(input("what is the text on the button: ")).lower()
	batteries = int(input("how many batteries are there: "))


	if color == "blue" and text == "abort":
		HoldButton()

	elif (batteries > 1 and text == "detonate"): 
		print("press and immediately release")

	elif color == "white":
		CARlabel = str(input("is there a lit indicator with a CAR label: ")).lower()
		if CARlabel == "y":
			HoldButton()
		else:
			HoldButton()

	elif batteries > 2:
		FRKlabel = str(input("is there a lit indicator with a FRK label: ")).lower()
		if FRKlabel == "y":
			print("press and immediately release")
		else:
			HoldButton()

	elif color == "red" and text == "hold":
		print("press and immediately release")

	else:
		HoldButton()


def HoldButton():
	print("------------PRESS AND HOLD THE BUTTON-----------------")
	color = str(input("which color is the strip: ")).lower()
	if color == "blue": print("release with a 4 in any position")
	elif color == "yellow":print("release with a 5 in any position")
	else:print("release with a 1 in any position") 
	#this also handles a white strip bc it's a 1 either way


def horizontal6wires(): #horizontal 6 
	print("horizontal 6")
	pass

def abc123wires(): 
	# color = str(input("what color is the wire: ")).lower()
	# letter = str(input("which letter is the wire going to: ")).lower()
	black = ["abc","ac","b","ac","b","bc","ab","c","c"]
	blue = ["b", "ac","b","a","b","bc","c","ac","a"]
	red = ["c","b","a","ac","b","ac","abc","ab","b"]
	blackCount = 0
	blueCount = 0
	redCount = 0
	while 1==1:
		color = str(input("what color is the wire: ")).lower()
		letter = str(input("which letter is the wire going to: ")).lower()
		# print(color)
		# print(letter)
		if color == "black":
			if str(letter) in black[blackCount]:
				print("cut")
			else:
				print("do not cut")
			blackCount += 1

		elif color == "blue":
			if str(letter) in blue[blueCount]:
				print("cut")
			else:
				print("do not cut")
			blueCount += 1

		elif color == "red":
			if str(letter) in red[redCount]:
				print("cut")
			else:
				print("do not cut")
			redCount += 1
		else:
			print("what the is going on ")


def ledStarWires():
	print("ledStarWires") # michael
	pass


	# simon would be hard

main()
