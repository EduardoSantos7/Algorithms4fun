class KthLargest:
    nums : List[int] = None
    k : int = None

    def __init__(self, k: int, nums: List[int]):
        nums.sort()
        self.k = k
        self.nums = nums

    def add(self, val: int) -> int:
        self.nums.append(val)
        self.nums.sort()
        return self.nums[-self.k]