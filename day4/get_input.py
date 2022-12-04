def gen_set(rng):
	start, end = map(int, rng.split("-"))
	return set(range(start, end + 1))

def get_input(filename="input.txt"):
	with open(filename, "r") as f:
		lines = f.read().splitlines()
		return map(lambda x: [gen_set(y) for y in x.split(",")], lines)