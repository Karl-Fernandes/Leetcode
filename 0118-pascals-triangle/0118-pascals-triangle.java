import java.util.ArrayList;
import java.util.List;

class Solution {
    public List<List<Integer>> generate(int numRows) {
        // Base case: If there's only 1 row, return [[1]]
        if (numRows == 1) {
            List<List<Integer>> triangle = new ArrayList<>();
            triangle.add(List.of(1));
            return triangle;
        }

        // Get the triangle up to numRows - 1 recursively
        List<List<Integer>> triangle = generate(numRows - 1);

        // Get the last row to compute the new row
        List<Integer> prevRow = triangle.get(triangle.size() - 1);
        List<Integer> newRow = new ArrayList<>();

        // First element is always 1
        newRow.add(1);

        // Compute middle elements by summing adjacent numbers from prevRow
        for (int i = 1; i < prevRow.size(); i++) {
            newRow.add(prevRow.get(i - 1) + prevRow.get(i));
        }

        // Last element is always 1
        newRow.add(1);

        // Add the new row to the triangle
        triangle.add(newRow);

        return triangle;
    }
}
