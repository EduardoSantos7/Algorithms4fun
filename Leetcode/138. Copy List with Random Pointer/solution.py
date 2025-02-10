"""
# Definition for a Node.
class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random
"""

class Solution:
    def copyRandomList(self, head: 'Optional[Node]') -> 'Optional[Node]':
        # enumerate the nodes
        i = 0
        enum = {}
        temp = head
        while temp:
            enum[temp] = i
            i += 1
            temp = temp.next
        # create an array where every node represents a value and the random node index
        array = []
        temp = head
        while temp:
            array.append([temp.val, enum[temp.random] if temp.random else None])
            temp = temp.next
        # create a new list based on above array
        temp_array = [None] * len(array)
        for i, node_data in enumerate(array):
            new_node = Node(node_data[0])
            temp_array[i] = new_node

        for i, node in enumerate(temp_array):
            node.next = temp_array[i+1] if i < len(temp_array) - 1 else None
            node.random = temp_array[array[i][1]] if array[i][1] is not None else None

        return temp_array[0] if temp_array else head