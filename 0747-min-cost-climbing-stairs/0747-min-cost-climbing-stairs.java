class Solution {
    public int minCostClimbingStairs(int[] cost) {
        int n = cost.length;
        int[] memo = new int[n];
        Arrays.fill(memo, -1);
        
        return Math.min(minCost(n - 1, cost, memo), minCost(n - 2, cost, memo));
    }

    public int minCost(int i, int[] cost, int[] memo) {
        if (i == 0 || i == 1) { 
            return cost[i];
        }

        if (memo[i] != -1) return memo[i]; 

        memo[i] = cost[i] + Math.min(minCost(i - 1, cost, memo), minCost(i - 2, cost, memo));
        return memo[i];
    }

}