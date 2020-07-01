# Do not edit the class below except
# for the depthFirstSearch method.
# Feel free to add new properties
# and methods to the class.


class Node:
    def __init__(self, name):
        self.children = []
        self.name = name

    def addChild(self, name):
        self.children.append(Node(name))
        return self

    def depthFirstSearch(self, array):
        stack = [self]

        while stack:
            node = stack.pop()
            if node:
                array.append(node.name)
                stack.extend(node.children[::-1])
        return array
