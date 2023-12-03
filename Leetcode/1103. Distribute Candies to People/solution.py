class Solution:
    def distributeCandies(self, candies: int, num_people: int) -> List[int]:
        # Initialize the result array with zeros
        result = [0] * num_people
        
        # Initialize the current number of candies to give
        candy = 1
        
        while candies > 0:
            # Iterate over each person
            for i in range(num_people):
                # If not enough candies left, give all remaining
                if candies < candy:
                    result[i] += candies
                    candies = 0
                    break
                else:
                    # Distribute the candies and reduce the total count
                    result[i] += candy
                    candies -= candy
                
                # Increment the candy for the next person
                candy += 1
                
        return result