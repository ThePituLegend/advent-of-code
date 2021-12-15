def get_input(filename="input.txt"):
	with open(filename, "r") as f:
		polymer = f.readline().strip()
		f.readline() # Skip white line

		rules = {}
		for line in f:
			pair, insert = line.strip().split(" -> ")
			rules[pair] = insert
		
		return polymer, rules