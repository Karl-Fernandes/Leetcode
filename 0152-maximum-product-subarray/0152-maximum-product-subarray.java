class Solution {
    public int maxProduct(int[] nums) {
        int[] m  = new int[nums.length];
        m[0] = nums[0];
        int q = nums[0];

        for (int i = 1; i <= nums.length - 1; i++) {
            if (m[i - 1] < 0) {
                m[i] = nums[i];
            } else {
                m[i] = nums[i] * m[i - 1];
            }
            q = Math.max(q, m[i]);
        }
        
        return q;
    }
}