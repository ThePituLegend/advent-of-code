def get_input(filename="input.txt"):
	with open(filename, "r") as f:
		return map(lambda elf: map(int, elf.split("\n")), f.read().split("\n\n"))
