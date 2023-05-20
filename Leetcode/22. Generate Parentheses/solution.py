class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        if n == 0:
            return [""]

        answer = []
        for left_count in range(n):
            for left_string in self.generateParenthesis(left_count):
                for right_string in self.generateParenthesis(n - left_count - 1):
                    answer.append(f"({left_string}){right_string}")

        return answer