class Solution:
    def fizzBuzz(self, n: int) -> List[str]:
        ans = []
        for i in range(1, n+1):
            mod_3 = i % 3
            mod_5 = i % 5
            if not mod_3 and not mod_5:
                ans.append("FizzBuzz")
            elif not mod_3:
                ans.append("Fizz")
            elif not mod_5:
                ans.append("Buzz")
            else:
                ans.append(f"{i}")

        return ans
