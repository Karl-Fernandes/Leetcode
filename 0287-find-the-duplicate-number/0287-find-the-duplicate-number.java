class Solution {
    public int findDuplicate(int[] nums) {
        int slow = nums[0];
        int fast = nums[0];

        do {
            slow = nums[slow];
            fast = nums[nums[fast]];
        } while (slow != fast);

        int currentNode = nums[0];
        while (currentNode != slow) {
            currentNode = nums[currentNode];
            slow = nums[slow];
        }  

        return slow;      
    }
}