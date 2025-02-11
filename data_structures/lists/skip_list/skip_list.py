import random

class SkipListNode:
    def __init__(self, value, level):
        self.value = value
        self.forward = [None] * (level + 1)  # List of forward pointers


class SkipList:
    MAX_LEVEL = 16  # Max height of the skip list
    PROBABILITY = 0.5  # Probability for level generation

    def __init__(self):
        self.head = SkipListNode(None, self.MAX_LEVEL)
        self.level = 0  # Current max level of the skip list

    def insert(self, value):
        update = [None] * (self.MAX_LEVEL + 1)
        current = self.head

        # Find the place to insert
        for i in range(self.level, -1, -1):
            while current.forward[i] and current.forward[i].value < value:
                current = current.forward[i]
            update[i] = current  # Store the last node at this level before insertion

        # Generate a level for the new node
        new_level = self._random_level()
        if new_level > self.level:
            for i in range(self.level + 1, new_level + 1):
                update[i] = self.head  # Update header pointers
            self.level = new_level  # Update the highest level

        # Insert the node
        new_node = SkipListNode(value, new_level)
        for i in range(new_level + 1):
            new_node.forward[i] = update[i].forward[i]
            update[i].forward[i] = new_node

    def search(self, value):
        current = self.head
        for i in range(self.level, -1, -1):
            while current.forward[i] and current.forward[i].value < value:
                current = current.forward[i]

        # Move to next node and check if it matches the value
        current = current.forward[0]
        return current and current.value == value

    def delete(self, value):
        update = [None] * (self.MAX_LEVEL + 1)
        current = self.head

        # Locate the node to delete
        for i in range(self.level, -1, -1):
            while current.forward[i] and current.forward[i].value < value:
                current = current.forward[i]
            update[i] = current

        target = current.forward[0]  # Candidate for deletion

        if target and target.value == value:
            for i in range(len(target.forward)):
                update[i].forward[i] = target.forward[i]

            # Reduce level if needed
            while self.level > 0 and self.head.forward[self.level] is None:
                self.level -= 1

    def _random_level(self):
        level = 0
        while random.random() < self.PROBABILITY and level < self.MAX_LEVEL:
            level += 1
        return level

    def display(self):
        print("\nSkip List:")
        for i in range(self.level + 1):
            node = self.head.forward[i]
            print(f"Level {i}: ", end=" ")
            while node:
                print(node.value, end=" -> ")
                node = node.forward[i]
            print("None")

if __name__ == "__main__":
    skip_list = SkipList()

    # Insert values
    skip_list.insert(3)
    skip_list.insert(6)
    skip_list.insert(7)
    skip_list.insert(9)
    skip_list.insert(12)
    skip_list.insert(19)
    skip_list.insert(17)
    skip_list.insert(26)
    skip_list.insert(21)
    skip_list.insert(25)

    # Display
    skip_list.display()

    # Search for values
    print("\nSearch 19:", skip_list.search(19))  # True
    print("Search 15:", skip_list.search(15))  # False

    # Delete a value
    skip_list.delete(19)
    print("\nAfter deleting 19:")
    skip_list.display()

    skip_list.delete(21)
    print("\nAfter deleting 21:")
    skip_list.display()
