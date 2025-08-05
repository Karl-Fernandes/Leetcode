class Solution:
    def numPairsDivisibleBy60(self, time: List[int]) -> int:
        remainders = [0] * 60
        count = 0
        
        for t in time:
            r = t % 60
            complement = (60 - r) % 60
            count += remainders[complement]
            remainders[r] += 1
        
        return count
