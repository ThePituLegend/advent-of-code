def hextobin(h): # https://stackoverflow.com/a/28913296
	return bin(int(h, 16))[2:].zfill(len(h) * 4)

def get_input(filename="input.txt"):
	with open(filename, "r") as f:
		return [hextobin(packet.strip()) for packet in f]
