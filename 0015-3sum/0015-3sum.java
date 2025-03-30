import java.util.ArrayList;
import java.util.Arrays;
import java.util.List;
import java.util.HashSet;
import java.util.Set;

class Solution {
    public List<List<Integer>> threeSum(int[] nums) {
        List<List<Integer>> result = new ArrayList<>();
        Arrays.sort(nums);
        
        for (int i = 0; i < nums.length - 2; i++) {
            if (i > 0 && nums[i] == nums[i - 1]) {
                continue;
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
        Set<Integer> seen = new HashSet<>();
        
        for (int j = start; j < nums.length; j++) {
            int complement = target - nums[j];
            if (seen.contains(complement)) {
                pairs.add(new int[]{complement, nums[j]});
                while (j + 1 < nums.length && nums[j] == nums[j + 1]) {
                    j++;
                }
            }
            seen.add(nums[j]);
        }
        return pairs;
    }
}