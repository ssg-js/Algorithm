
import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;

public class Main {

    private static int MOD = 987654321;
    public static void main (String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        int n = Integer.parseInt(br.readLine());
        if (n == 0) {
            System.out.println(0);
            return;
        }
        long[] dp = new long[n + 1];
        dp[0] = 1;
        dp[2] = 1;
        for (int i = 4; i < dp.length; i+=2) {
            int rest = i - 2;
            long value = 0;
            for (int k = 0; k <= rest; k+=2) {
                value = (value + (dp[k] * dp[rest-k]) % MOD) % MOD;
            }
            dp[i] = value;
        }
        System.out.println(dp[n]);
    }

}
