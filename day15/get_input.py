def get_input(filename="input.txt"):
	with open(filename, "r") as f:
		return [[int(x) for x in row.strip()] for row in f]