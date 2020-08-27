def return_kth_last_one(head, k):
    if not head:
        return

    p1 = head
    p2 = head
    i = 0

    while p2.next and i < k:
        i += 1
        p2 = p2.next

    while p2:
        p2 = p2.next
        p1 = p1.next

    return p1
