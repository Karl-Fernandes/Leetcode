class Solution {
    public int lengthOfLongestSubstring(String s) {
        int left = 0;
        int right = 0;
        int res = 0;
        
        if (s.length() == 0) return 0;
        
        HashSet<Character> visited = new HashSet<Character>();

        while (right < s.length()) {
            char currentChar = s.charAt(right);
            if (!visited.contains(currentChar)) {
                visited.add(currentChar);
                right++;
                res = Math.max(res, right - left);
            } else {
                visited.remove(Character.valueOf(s.charAt(left)));
                left++;
            }
        } 

        return res;
    }
}