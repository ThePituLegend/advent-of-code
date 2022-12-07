def get_input(filename="input.txt"):
	with open(filename, "r") as f:
		return f.readline()