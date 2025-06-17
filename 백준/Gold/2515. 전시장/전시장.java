

import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.StringTokenizer;

public class Main {

    
    public static void main (String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer st = new StringTokenizer(br.readLine());
        int n = Integer.parseInt(st.nextToken());
        int s = Integer.parseInt(st.nextToken());
        int[] costs = new int[20_000_001];
        int[] dp = new int[20_000_001];
        int maxHeight = 0;
        for (int i = 0; i < n; i++) {
            st = new StringTokenizer(br.readLine());
            int h = Integer.parseInt(st.nextToken());
            int c = Integer.parseInt(st.nextToken());
            if (costs[h] < c) {
                costs[h] = c;
            }
            if (maxHeight < h) {
                maxHeight = h;
            }
        }
        for (int i = s; i < maxHeight+1; i++) {
            dp[i] = Math.max(costs[i] + dp[i-s], dp[i-1]);
        }

        System.out.println(dp[maxHeight]);
    }

    

}
