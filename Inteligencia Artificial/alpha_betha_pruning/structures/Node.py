class Node:

    def __init__(self, n=2):
        self.n = n
        self.data = []
        self.full = False

    def isFull(self):
        return len(self.data) == self.n

    def insert(self, value):
        if len(self.data) == 0:
            self.data.append(value)
            return None
        last_node = self.data[len(self.data) - 1]

        if isinstance(last_node, Node):
            value = last_node.insert(value)
            if value is None:
                return None
        if not self.isFull() and value is not None:
            self.data.append(value)
            return None
        else:
            new_Node = Node(self.n)
            new_Node.insert(value)
            return new_Node

    def __str__(self):

        strings = ""
        for dat in self.data:
            strings = strings + ", " + str(dat)
        return "[" + strings + "]"