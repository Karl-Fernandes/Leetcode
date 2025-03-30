class Solution {
    public boolean isPalindrome(String s) {
                String result = s.toLowerCase().replaceAll("[^a-zA-Z0-9]", "");
                int n = result.length() - 1;
                System.out.println(n);

                if (n == 0) {
                    System.out.println("Hello");
                    return true;
                }

                for (int i=0; i <= Math.floorDiv(n, 2); i++) {
                    if (result.charAt(i) != result.charAt(n-i)) {
                        return false;
                    }
                }
                return true;

    }
}