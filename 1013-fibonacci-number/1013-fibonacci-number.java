class Solution {
    public int fib(int n) {
       int[] cache = new int[n + 1];  
        Arrays.fill(cache, -1); 

        return fibHelper(n, cache);
    }


    private int fibHelper(int n, int[] cache) {
        if (n == 0) return 0;
        if (n == 1) return 1;

        if (cache[n] != -1) {
            return cache[n];
        }

        cache[n] = fibHelper(n-1, cache) + fibHelper(n-2, cache);
        return cache[n];
    }
}