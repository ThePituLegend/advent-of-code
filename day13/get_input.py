def get_input(filename="input.txt"):
	with open(filename, "r") as f:
		dots = set()
		folds = []

		for line in f:
			if line[0] == "f": # Folds
				axis, coord = line.split(" ")[-1].strip().split("=")
				folds.append((axis, int(coord)))
			elif line != "\n":
				x, y = line.strip().split(",")
				dots.add((int(x), int(y)))
		
		return dots, folds