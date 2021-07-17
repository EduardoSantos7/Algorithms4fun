class Solution:
    def countMatches(self, items: List[List[str]], ruleKey: str, ruleValue: str) -> int:
        index_to_check = 0 if ruleKey == "type" else 1 if ruleKey == "color" else 2
        count = 0
        for item in items:
            if item[index_to_check] == ruleValue:
                count += 1
        return count
