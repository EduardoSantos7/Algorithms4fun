class Node:
    def __init__(self, val, _next):
        self.val = val
        self.next = _next
    

class TwoSum:

    def __init__(self):
        self.results = set()
        self.elements = None
        

    def add(self, number: int) -> None:
        if self.elements == None:
            self.elements = Node(number, None)
            return
        
        # complete the sum up recording
        temp = self.elements
        while temp != None:
            self.results.add(temp.val + number)
            temp = temp.next
        
        temp = self.elements
        temp_next = self.elements.next

        while temp_next and temp_next.val < number:
            temp = temp_next
            temp_next = temp_next.next

        if temp and temp.val < number:
            new_node = Node(number, temp_next)
            temp.next = new_node
        else:
            new_node = Node(number, temp)
            self.elements = new_node


    def find(self, value: int) -> bool:
        return value in self.results
        


# Your TwoSum object will be instantiated and called as such:
# obj = TwoSum()
# obj.add(number)
# param_2 = obj.find(value)