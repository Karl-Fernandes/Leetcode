class Solution:
    def canCompleteCircuit(self, gas: List[int], cost: List[int]) -> int:
        if sum(cost) > sum(gas):
            return -1
        
        currSum = 0
        currIndex = 0

        for i in range(len(gas)):
            currSum += gas[i] - cost[i]
            if currSum < 0:
                currIndex = i + 1
                currSum = 0
        

        return currIndex
            
