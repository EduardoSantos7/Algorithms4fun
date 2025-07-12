class Solution:
    def partitionLabels(self, s: str) -> List[int]:
        last_seen = dict()

        for i, c in enumerate(s):
            last_seen[c] = i
        
        start = 0
        end = -1
        result = [0]
        partition = 0

        for i, c in enumerate(s):
            end = max(end, last_seen[c])
            result[partition] = end - start + 1
            if i == end and i != len(s) - 1:
                partition += 1
                result.append(0)
                start = i + 1
        
        return result