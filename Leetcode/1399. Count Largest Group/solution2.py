class Solution:
    def countLargestGroup(self, n: int) -> int:
        """ Returns the number of groups with the largest size. """
        
        # Dictionary to count occurrences of each sum of digits
        sum_count = defaultdict(int)
        
        # Count each sum of digits from 1 to n
        for i in range(1, n + 1):
            digit_sum = sum(int(char) for char in str(i))
            sum_count[digit_sum] += 1
        
        # Determine the maximum size of groups
        max_size = max(sum_count.values())
        
        # Count how many groups have this maximum size
        largest_groups_count = sum(1 for count in sum_count.values() if count == max_size)
        
        return largest_groups_count