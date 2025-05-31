# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def nodesBetweenCriticalPoints(self, head: Optional[ListNode]) -> List[int]:
        # Iterate the list to find the most critical nodes
        prev, current, critical_nodes, counter = None, head, [], 0
        while current != None:
            counter += 1
            # if both prev and next are not null evaluate if this is a critical node
            if prev and current.next:
                if current.val < prev.val and current.val < current.next.val:
                    critical_nodes.append(counter)
                elif current.val > prev.val and current.val > current.next.val:
                    critical_nodes.append(counter)
            prev = current
            current = current.next
        # Compute the max and min distances
        if len(critical_nodes) < 2:
            return [-1,-1]
        critical_nodes.sort()
        _min = inf
        for i in range(1, len(critical_nodes)):
            _min = min(_min, critical_nodes[i] - critical_nodes[i-1])
        return [_min, critical_nodes[-1] - critical_nodes[0]]