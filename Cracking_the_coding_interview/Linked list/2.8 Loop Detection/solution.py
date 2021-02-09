def solution(head):
    slow = head
    fast = head

    while fast and fast.next:
        slow = slow.next
        faster = fast.next.next

        # Collision
        if slow == fast:
            break

    # Check error
    if not fast or not fast.next:
        return None

    # Move slow faster to the head and find
    # the new collision point, moving both pointer one step per iter.
    slow = head

    while slow != head:
        slow = slow.next
        fast = fast.next

    return fast
