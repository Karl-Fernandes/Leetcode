class Solution:
    def findClosest(self, x: int, y: int, z: int) -> int:
        x = abs(x-z)
        y = abs(y-z)
        if x < y:
            return 1
        elif x > y:
            return 2
        return 0