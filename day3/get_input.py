def get_input_1(filename="input.txt"):
	with open(filename, "r") as f:
		lines = f.read().splitlines()
		return map(lambda x: [set(x[:len(x)//2]), set(x[len(x)//2:])], lines)

def get_input_2(filename="input.txt"):
	with open(filename, "r") as f:
		lines = f.read().splitlines()
		return map(lambda i: [set(lines[i]), set(lines[i+1]), set(lines[i+2])], range(0, len(lines), 3))
