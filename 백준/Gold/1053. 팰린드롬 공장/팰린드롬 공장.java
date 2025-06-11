import java.io.*;

public class Main {
    private static char[] arr;
    private static int n;
    private static int[][] dp;
    public static void main (String[] args) throws IOException {
        String line = new BufferedReader(new InputStreamReader(System.in)).readLine();
        n = line.length();
        arr = line.toCharArray();

        int answer = 200_000_000;
        // 원본
        dp = new int[n][n];

        for (int k = 1; k < n; k++) {
            for (int i = 0; i < n; i++) {
                int j = i + k;
                if (j >= n) continue;
                dp[i][j] = Math.min(dp[i + 1][j] + 1, dp[i][j-1] + 1);
                dp[i][j] = Math.min(dp[i][j], (k < 2 ? 0 : dp[i+1][j-1]) + (arr[i] == arr[j] ? 0 : 1));
            }
        }
        if (dp[0][n-1] < answer) {
            answer = dp[0][n-1];
        }
        // 교환
        for (char[] caseArr : combination()) {
            dp = new int[n][n];

            for (int k = 1; k < n; k++) {
                for (int i = 0; i < n; i++) {
                    int j = i + k;
                    if (j >= n) continue;
                    dp[i][j] = Math.min(dp[i + 1][j] + 1, dp[i][j-1] + 1);
                    dp[i][j] = Math.min(dp[i][j], (k < 2 ? 0 : dp[i+1][j-1]) + (caseArr[i] == caseArr[j] ? 0 : 1));
                }
            }
            if (dp[0][n-1] + 1 < answer) {
                answer = dp[0][n-1] + 1;
            }
        }
        System.out.println(answer);
    }

    private static char[][] combination () {
        char[][] ret = new char[coefficient(n)][n];
        int caseIdx = 0;
        for (int i = 0; i < n-1; i++) {
            for (int j = i + 1; j < n; j++) {
                for (int k = 0; k < n; k++) {
                    ret[caseIdx][k] = arr[k];
                }
                char tmp = ret[caseIdx][i];
                ret[caseIdx][i] = ret[caseIdx][j];
                ret[caseIdx][j] = tmp;
                caseIdx++;
            }
        }
        
        return ret;
    }

    private static int coefficient (int v) {
        return v * (v-1) / 2;
    }
}
