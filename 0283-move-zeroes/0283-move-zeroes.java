
class Solution {
    public void moveZeroes(int[] nums) {
        int nonZeroPos = 0;
        
        for (int i = 0; i < nums.length; i++) {
            if (nums[i] != 0) {
                if (i > nonZeroPos) {  // Only swap if needed
                    int temp = nums[nonZeroPos];
                    nums[nonZeroPos] = nums[i];
                    nums[i] = temp;
                }
                nonZeroPos++;
            }
        }
    }
}