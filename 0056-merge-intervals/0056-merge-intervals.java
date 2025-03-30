class Solution {
    public int[][] merge(int[][] intervals) {
        if (intervals.length <= 1) {
            return intervals;
        }

        // Sort the intervals by their start time
        Arrays.sort(intervals, (a, b) -> Integer.compare(a[0], b[0]));

        // Initialize result array with same size as input (we'll truncate later)
        List<int[]> res = new ArrayList<>();
        res.add(intervals[0]); // Add first interval




        for (int i = 1; i < intervals.length; i++) {
            int[] last = res.get(res.size() - 1);
            int[] current = intervals[i];

            if (last[1] >= current[0]) {
                last[1] = Math.max(last[1], current[1]);
            } else {
                res.add(current);
            }
        }
     return res.toArray(new int[res.size()][]);   
      }
}