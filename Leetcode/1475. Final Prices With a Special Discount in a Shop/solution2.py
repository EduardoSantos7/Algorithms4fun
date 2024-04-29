# Using monotonic stack
class Solution:
    def finalPrices(self, prices: List[int]) -> List[int]:
        st=[]
        res=[]
        for i in range(len(prices)):
            while st and prices[st[-1]]>=prices[i]:
                index=st.pop()
                res[index]=prices[index]-prices[i]
            res.append(prices[i])
            st.append(i)
        return res