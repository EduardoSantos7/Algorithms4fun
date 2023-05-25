class Solution:
    def minOperations(self, boxes: str) -> List[int]:
        n, ans = len(boxes), []
        left, right = 0, sum(i for i in range(n) if boxes[i] == '1')
        one_left, one_right = 0, boxes.count('1')

        for i in range(n):
            ans.append(left+right)

            if boxes[i] == '1':
                one_left += 1
                one_right -= 1

            left += one_left
            right -= one_right
        
        return ans