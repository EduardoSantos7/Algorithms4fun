# This is an input class. Do not edit.
class LinkedList:
    def __init__(self, value):
        self.value = value
        self.next = None


def removeKthNodeFromEnd(head, k):
    temp = head
	count = 0
	
	while temp:
		count += 1
		temp = temp.next

	temp = head
	target_moves = count - k - 1
	
	# Delete the head node
	if target_moves < 0:
		head.value = head.next.value
		head.next = head.next.next
		return
	
	while target_moves:
		temp = temp.next
		target_moves -= 1
	
	# Avoid an error when no elements is deleted
	if temp.next:
		temp.next = temp.next.next
