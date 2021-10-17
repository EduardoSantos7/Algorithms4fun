class Solution:
    def findCenter(self, edges: List[List[int]]) -> int:
        mem = {}

        for edge in edges[:3]:
            mem[edge[0]] = mem.get(edge[0], 0) + 1
            mem[edge[1]] = mem.get(edge[1], 0) + 1

        most_frequent = 0
        key_most_frequent = 0

        for node_id, times_appear in mem.items():
            if times_appear > most_frequent:
                most_frequent = times_appear
                key_most_frequent = node_id

        return key_most_frequent
