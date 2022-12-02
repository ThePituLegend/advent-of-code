def get_input(filename="input.txt"):
	with open(filename, "r") as f:
		return map(lambda x: x.strip().split(), f.readlines())