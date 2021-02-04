class Node:
    def __init__(self, value, _next=None):
        self.value = value
        self.next = _next


class SimpleLinkedList:
    def __init__(self, length):
        self.head = None

        for i in range(length):
            self.insert(i)

    def insert(self, value):
        """ Insert at the end  """

        if not self.head:
            self.head = Node(value)
            return

        temp = self.head

        while temp.next:
            temp = temp.next

        temp.next = Node(value)

    @staticmethod
    def intersectAt(l1, l2, index_l1, index_l2):
        temp1 = l1.head
        counter = 0
        while temp1.next and counter < index_l1:
            temp1 = temp1.next
            counter += 1

        temp2 = l2.head
        counter = 0
        while temp2.next and counter < index_l2:
            temp2 = temp2.next
            counter += 1

        temp2.next = temp1

    @staticmethod
    def print_list(_list):
        temp = _list.head
        while temp:
            print(temp.value, end='-')
            temp = temp.next
        print()


l1 = SimpleLinkedList(10)
l2 = SimpleLinkedList(6)

SimpleLinkedList.print_list(l1)
SimpleLinkedList.print_list(l2)

SimpleLinkedList.intersectAt(l1, l2, 6, 3)

SimpleLinkedList.print_list(l1)
SimpleLinkedList.print_list(l2)


def detect_intersection(l1, l2):

    if not l1 or not l2:
        return False

    temp = l1.head
    len_l1 = 1
    while temp.next:
        temp = temp.next
        len_l1 += 1

    temp = l2.head
    len_l2 = 1
    while temp.next:
        temp = temp.next
        len_l2 += 1

    moved_node, start_node = (
        l1.head, l2.head) if len_l1 > len_l2 else (l2.head, l1.head)

    for _ in range(abs(len_l1 - len_l2)):
        moved_node = moved_node.next

    while moved_node != start_node and moved_node.next and start_node.next:
        moved_node = moved_node.next
        start_node = start_node.next

    return start_node if moved_node == start_node else False


res = detect_intersection(l1, l2)

print(res if not res else res.value)
