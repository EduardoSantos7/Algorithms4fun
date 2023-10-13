def __init__(self, k: int, nums: List[int]):
    # self.nums is a ""heap"" 
    self.nums = nums[:k]
    # self.nums = [4,5,8]
    self.k = k
    # self.k = 3
    heapify(self.nums) # O(N) where N is # of elements in heap
    # self.nums = [4,5,8]

    # [k= 3, len(nums) = 4 ] // This is the rest of the list O(M-N)
    for i in range(k,len(nums)):
        # if any number is bigger than the smallest element in the list,
        # then we simply push it into the list, and pop the smallest
        # pushpop is quicker than pushing the element and popping
        if nums[i] > self.nums[0]: 
            heappushpop(self.nums,nums[i]) #log(N)
    # we only need to track the k largest elements at a time, and can overlook anything smaller in nums
    

def add(self, val: int) -> int:
    # if the length of the heap (self.nums) is less than self.k(the size) than we push into nums the current value because we aren't keeping track of k numbers in our heap yet
    if len(self.nums) < self.k:
        heappush(self.nums,val) # O(log(N))
        # if the val is larger than the smallest number, we pop the smallest number, and push the current value so we have access to the kth largest, number 
    elif val > self.nums[0]:
        heappushpop(self.nums,val) # O(logN)
    
    # our heap is a minheap, that keeps track of the kth largest, which is the top of the heap, thus we return the top. 
    return self.nums[0]

# Key insight: 
# 1) We can use a minheap that tracks the smallest out of k set of elements.
# 2) We can use heappushpop() which is more efficient than heappush/pop seperately. 