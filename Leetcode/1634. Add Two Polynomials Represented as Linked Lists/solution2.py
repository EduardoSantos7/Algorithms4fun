class Solution:

    def addPoly(self, poly1, poly2):
        p1 = poly1
        p2 = poly2
        # initial dummy node
        sum = PolyNode()
        # maintain pointer to last node
        current = sum

        # Maintain two pointers
        while p1 != None and p2 != None:
            if p1.power == p2.power:
                if p1.coefficient + p2.coefficient != 0:
                    current.next = PolyNode(
                        p1.coefficient + p2.coefficient, p1.power
                    )
                    current = current.next
                p1 = p1.next
                p2 = p2.next
            elif p1.power > p2.power:
                current.next = p1
                p1 = p1.next
                current = current.next
            else:
                current.next = p2
                p2 = p2.next
                current = current.next

        if p1 == None:
            current.next = p2
        else:
            current.next = p1
        return sum.next