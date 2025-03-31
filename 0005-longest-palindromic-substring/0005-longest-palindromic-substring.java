class Solution {
    public String longestPalindrome(String s) {
        String res = "";
        int resLength = 0;

        

        for (int i = 0; i <= s.length() - 1; i++) {
            int left = i; int right = i;
            while (left >= 0 && right <= s.length() - 1 && s.charAt(left) == s.charAt(right)) {
                if (right - left + 1 > resLength) {
                    res = s.substring(left, right + 1);
                    resLength = right - left;
                }
                left--;
                right++;
            }
            

            left = i; right = i + 1;
            while (left >= 0 && right <= s.length() - 1 && s.charAt(left) == s.charAt(right)) {
                if (right - left  + 1 > resLength) {
                    res = s.substring(left, right + 1);
                    resLength = right - left;
                }
                left--;
                right++;
            }
        }
        return res;
    }
}