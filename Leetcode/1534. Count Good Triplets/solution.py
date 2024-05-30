class FenwickTree:
    def __init__(self, size: int):
        self.partial = [0] * (size + 1)
        self.length = size + 1
    
    def getCum(self, end: int, start: int) -> int:
        return self.getSum(end) - self.getSum(start - 1)
    
    def getSum(self, index0: int) -> int:
        start1 = index0 + 1
        ans = 0
        while start1 > 0:
            ans += self.partial[start1]
            start1 &= (start1 - 1)
        return ans
    
    def addSum(self, i0:int, val: int):
        start1 = i0 + 1
        while True:
            self.partial[start1] += val
            start1 += start1 & (-start1)
            if start1 >= self.length:
                return

class Solution:
    def countGoodTriplets(self, arr: List[int], a: int, b: int, c: int) -> int:
        pre = [0] * 1001
        post = FenwickTree(1001)
        pre[arr[0]] += 1
        vi = 2
        while vi < 0 + len(arr):
            post.addSum(arr[vi], 1)
            vi += 1

        i = 1
        ans = 0
        while i < 0 + len(arr) - 1:
            middle = arr[i]
            aupper = min(1000, middle + a)
            alower = max(0, middle - a)
            bupper = min(1000, middle + b)
            blower = max(0, middle - b)
            traversea = alower
            while traversea <= aupper:
                if pre[traversea]:
                    intersectlower = max(blower, traversea - c)
                    intersecupper = min(bupper, traversea + c)
                    if intersecupper >= intersectlower:
                        if not intersectlower:
                            ans += pre[traversea] * post.getSum(intersecupper)
                        else:
                            ans += pre[traversea] * post.getCum(intersecupper, intersectlower)
                traversea += 1
            pre[middle] += 1
            vaftermiddle = arr[i + 1]
            post.addSum(vaftermiddle, -1)
            i += 1
        return ans
        