def get_input(filename="input.txt"):
    with open(filename, "r") as f:
        lines = [[list(map(int, points.split(","))) for points in line.split(" -> ")] for line in f.read().splitlines()]
        corner = (max([point[0] for points in lines for point in points]), max([point[1] for points in lines for point in points]))

        return lines, corner