import numpy as np

def get_input(filename="input.txt"):
	with open(filename, "r") as f:
		# Read the input file, consisting of a 2d array of integers without any spaces, and get a numpy array
		return np.array([list(map(int, line.strip())) for line in f.readlines()])
