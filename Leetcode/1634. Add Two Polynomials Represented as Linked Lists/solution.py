# Definition for polynomial singly-linked list.
# class PolyNode:
#     def __init__(self, x=0, y=0, next=None):
#         self.coefficient = x
#         self.power = y
#         self.next = next

class Solution:
    def addPoly(self, poly1: 'PolyNode', poly2: 'PolyNode') -> 'PolyNode':
        coefficients_by_power = {}

        while poly1:
            if poly1.power in coefficients_by_power:
                coefficients_by_power[poly1.power].append(poly1.coefficient)
            else:
                coefficients_by_power[poly1.power] = [poly1.coefficient]
            poly1 = poly1.next
        
        while poly2:
            if poly2.power in coefficients_by_power:
                coefficients_by_power[poly2.power].append(poly2.coefficient)
            else:
                coefficients_by_power[poly2.power] = [poly2.coefficient]
            poly2 = poly2.next
        
        curr = None
        for power in sorted(coefficients_by_power):
            _sum = sum(coefficients_by_power[power])
            if _sum != 0:
                node = PolyNode(_sum, power, curr)
                curr = node
        
        return curr