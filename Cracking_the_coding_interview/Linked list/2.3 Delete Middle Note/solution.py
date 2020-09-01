def deleteNode(node):
    if not node or not node.next:
        return False

    next_node = node.next
    node.val = next_node.val
    node.next = next_node.val

    return True
