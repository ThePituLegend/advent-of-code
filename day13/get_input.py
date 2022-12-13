def get_input(filename="input.txt"):
	with open(filename, "r") as f:
		signal = f.read().strip().split("\n\n")
		pairs = map(lambda x: x.split("\n"), signal)

		return map(lambda x: [eval(x[0]), eval(x[1])], pairs) # God forgive me, as I have sinned