class Solution:
    def isPathCrossing(self, path: str) -> bool:
        x, y = 0, 0
        mem = set([(0,0)])
        for step in path:
            if step == "N":
                y += 1
            elif step == "S":
                y -= 1
            elif step == "W":
                x -= 1
            else:
                x += 1

            if (x, y) in mem:
                return True
            
            mem.add((x,y))
        
        return False