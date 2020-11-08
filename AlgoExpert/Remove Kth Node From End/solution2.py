# This is an input class. Do not edit.
class LinkedList:
    def __init__(self, value):
        self.value = value
        self.next = None


def removeKthNodeFromEnd(head, k):
    first, second = head, head

	count = 1
	
	while count <= k:
		second = second.next
		count += 1
	
	if not second:
		head.value = head.next.value
		head.next = head.next.next
		return

	while second.next:
		second = second.next
		first = first.next
		
	
	first.next = first.next.next
