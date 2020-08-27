def delete_duplicates(self, head):

    temp = head
    if not temp:
        return

    prev = None
    mem = set()

    while temp is not None:
        if temp.val in mem:
            prev.next = temp.next
        else:
            mem.add(temp.val)
            prev = temp

        temp = temp.next
