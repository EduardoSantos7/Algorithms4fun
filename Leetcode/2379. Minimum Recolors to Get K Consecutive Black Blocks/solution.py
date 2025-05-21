class Solution:
    def minimumRecolors(self, blocks: str, k: int) -> int:
        # Use two pointers to mark the current window, and counters for the operations and total black blocks
        left, curr_ops, curr_black_blocks, min_ops = 0, 0, 0, 101
        for i, right in enumerate(blocks):
            # If the current block is W increase operations and current black block by 1 else only black block counter
            if right == "W":
                curr_ops += 1
                curr_black_blocks += 1
            else:
                curr_black_blocks += 1
            # When the windwow length reaches 7:
            # move the left pointer and depending its color decrease the ops and blocks.
            if curr_black_blocks == k:
                # and get the min operations so far
                min_ops = min(min_ops, curr_ops)
                block = blocks[left]
                if block == "W":
                    curr_ops -= 1
                    curr_black_blocks -= 1
                else:
                    curr_black_blocks -= 1
                left += 1
        
        return min_ops