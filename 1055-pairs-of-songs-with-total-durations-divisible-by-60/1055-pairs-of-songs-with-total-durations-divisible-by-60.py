class Solution:
    def numPairsDivisibleBy60(self, time: List[int]) -> int:
        total = 0
        count = defaultdict(int)

        for num in time:
            remainder = num % 60 #30
            complement = (60-remainder)%60 #30
            total += count[complement]
            count[remainder] += 1

        return total