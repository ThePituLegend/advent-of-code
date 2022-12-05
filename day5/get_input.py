def extract_move(move):
	move = move.split()
	return (int(move[1]), int(move[3])-1, int(move[5])-1)

def get_input(filename="input.txt"):
	with open(filename, "r") as f:
		crates, moves = f.read().split("\n\n")
		crates = [x.split() for x in crates.splitlines()]
		moves = map(extract_move, moves.splitlines())
		return crates, moves