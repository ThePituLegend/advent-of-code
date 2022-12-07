class Node():
    def __init__(self, name, parent, size=0):
        self.name: str = name
        self.parent: Node = parent
        self.children: list[Node] = []
        self.size: int = size

    def __str__(self):
        return f"{self.name} ({self.size})"

    def __repr__(self):
        return self.__str__()

    def __lt__(self, other):
        return self.size < other.size

    def __le__(self, other: int):
        return self.size <= other

    def __ge__(self, other: int):
        return self.size >= other

    def __add__(self, other: int):
        return self.size + other

    def __radd__(self, other: int):
        return self.size + other

class Tree():
    def __init__(self):
        self.root: Node = Node("/", None)
        self.pwd: Node = self.root
        self.dirs: list[Node] = []

    def add_node(self, name, size=0):
        if size == 0: # It's a directory (size 0)
            node = Node(name, self.pwd)
            self.pwd.children.append(node)
            self.dirs.append(node)

            self.pwd = node

        else: # It's a file
            node = Node(name, self.pwd, size)
            self.pwd.children.append(node)

    def go_up(self):
        self.pwd = self.pwd.parent

    def update_sizes(self):
        for child in self.root.children:
            self.root.size += self.update_size_childrens(child)

    def update_size_childrens(self, node):
        for child in node.children:
            node.size += self.update_size_childrens(child)

        return node.size