# Definition for a street.
# class Street:
#     def openDoor(self):
#         pass
#     def closeDoor(self):
#         pass
#     def isDoorOpen(self):
#         pass
#     def moveRight(self):
#         pass
#     def moveLeft(self):
#         pass
class Solution:
    def houseCount(self, street: Optional['Street'], k: int) -> int:
        i = 0
        while i < k:
            street.closeDoor()
            street.moveRight()
            i += 1
        
        street.openDoor()
        street.moveRight()
        count = 1

        while street.isDoorOpen() is False:
            street.openDoor()
            street.moveRight()
            count += 1
        
        return count