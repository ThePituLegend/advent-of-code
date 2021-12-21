def get_input(filename="input.txt"):
	with open(filename, "r") as f:
		min_x, max_x, min_y, max_y = (int(n) for axis in f.readline()[13:].split(",") for n in axis.strip()[2:].split(".."))
		return {"x": min_x, "y": min_y}, {"x": max_x, "y": max_y}