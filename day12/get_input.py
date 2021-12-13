from collections import defaultdict

def get_input(filename="input.txt"):
	with open(filename, "r") as f:
		graph = defaultdict(list)

		for edge in f:
			v, n = edge.strip().split("-") # Vertex & Neighbour
			
			if v != "end":
				graph[v].append(n)
			
			if v != "start" and n != "end":
				graph[n].append(v)

		return graph