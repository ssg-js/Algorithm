
import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.StringTokenizer;

public class Main {
    static int MIN_VALUE = -400_000_000;

    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer st = new StringTokenizer(br.readLine());
        int n = Integer.parseInt(st.nextToken());
        int m = Integer.parseInt(st.nextToken());
        int[][] board = new int[n][m];
        // O(n^2)
        for (int i = 0; i < n; i++) {
            st = new StringTokenizer(br.readLine());
            for (int j = 0; j < m; j++) {
                board[i][j] = Integer.parseInt(st.nextToken());
            }
        }
        // O(n^2)
        int[][] prefixSums = new int[n][m]; // 행이 누적합 배열임
        for (int i = 0; i < n; i++) {
            for (int j = 0; j < m; j++) {
                if (j == 0) {
                    prefixSums[i][j] = board[i][j];
                    continue;
                }
                prefixSums[i][j] = board[i][j] + prefixSums[i][j-1];
            }
        }
        int maxMetrixSum = MIN_VALUE;
        for (int leftColumn = 0; leftColumn < m; leftColumn++) {
            // 초기 column 값 만들어야 함. 초기값을 만들면서 column배열 갱신해야함
            for (int rightColumn = leftColumn; rightColumn < m; rightColumn++) {
                int ret = Kadane(prefixSums, leftColumn, rightColumn);
                if (ret > maxMetrixSum) {
                    maxMetrixSum = ret;
                }
            }
            
        }
        System.out.println(maxMetrixSum);

    }

    /**
     * 1차원 배열의 값을 갱신하고, 연속된 구간합의 최댓값을 리턴
     * @param arr
     * @return
     */
    private static int Kadane(int[][] prefixSum, int leftColumn, int rightColumn) {
        int maxSum = MIN_VALUE;
        int curSum = 0;
        
        // 최대 구간합 구하기
        for (int i = 0; i < prefixSum.length; i++) {
            int value = prefixSum[i][rightColumn];
            if (leftColumn > 0) {
                value -= prefixSum[i][leftColumn - 1];
            }
            curSum = Math.max(value, curSum + value);
            if (maxSum < curSum) {
                maxSum = curSum;
            }
        }

        return maxSum;  
    }


}
