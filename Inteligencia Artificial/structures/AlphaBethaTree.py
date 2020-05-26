from typing import Optional

from .Node import Node

class AlphaBethaTree:

    def __init__(self, n):
        self.__n__ = n
        self.__root__ = Node(n)

    def insert(self, value):
        new_Node: Optional[Node] = self.__root__.insert(value)
        if new_Node is not None:
            n = Node(self.__n__)
            n.data.append(self.__root__)
            n.data.append(new_Node)


            self.__root__ = n

    def pruning(self):
        return self.__pruning__(self.__root__ ,-1000, 1000, 0)

    def __pruning__(self, node, alpha, betha , depth):
        if not isinstance(node, Node):
            return node
        if depth %2 == 0:
            for child in node.data:
                alpha = max(alpha, self.__pruning__(child, alpha, betha, depth+1))
                if betha<=alpha:
                    break
            return alpha
        else:
            for child in node.data:
                betha = min(betha, self.__pruning__(child, alpha, betha, depth+1))
                if betha<=alpha:
                    break
            return betha

    def __compare_alpha_betha__(self, a, b):
        if a is not None and b is not None:
            return a-b
        return 0


    def __str__(self):
        return str(self.__root__)
