class Solution {
    public List<List<Integer>> threeSum(int[] nums) {
        List<List<Integer>> result = new ArrayList<>();
        Arrays.sort(nums);
        
        for (int i = 0; i < nums.length - 2; i++) {
            if (i > 0 && nums[i] == nums[i - 1]) {
                continue; // Skip duplicates
            }
            
            int newTarget = -nums[i];
            List<int[]> twoSumPairs = twoSum(nums, i + 1, newTarget);
            
            for (int[] pair : twoSumPairs) {
                result.add(Arrays.asList(nums[i], pair[0], pair[1]));
            }
        }
        return result;
    }

    private List<int[]> twoSum(int[] nums, int start, int target) {
        List<int[]> pairs = new ArrayList<>();
        int left = start;
        int right = nums.length - 1;

        while (left < right) {
            int sum = nums[left] + nums[right];
            if (sum == target) {
                pairs.add(new int[]{nums[left], nums[right]});
                while (left < right && nums[left] == nums[left + 1]) left++;
                while (left < right && nums[right] == nums[right - 1]) right--;
                left++;
                right--;
            } else if (sum < target) {
                left++;
            } else {
                right--;
            }
        }
        return pairs;
    }
}