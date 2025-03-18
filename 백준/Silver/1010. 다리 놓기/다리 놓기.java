import java.util.*;
import java.io.*;

class Main {
    static int[][] combinations = new int[31][31];
    
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        int t = Integer.parseInt(br.readLine());
        StringBuilder sb = new StringBuilder();
        for (int tc = 0; tc < t; tc++) {
            StringTokenizer st = new StringTokenizer(br.readLine());
            int a = Integer.parseInt(st.nextToken());
            int b = Integer.parseInt(st.nextToken());
            sb.append(combi(b, a)).append("\n");
        }
        
        System.out.println(sb);
        
    }
    
    static int combi(int n, int k) {
        if (combinations[n][k] > 0) return combinations[n][k];
        if (k == 0 || k == n) return combinations[n][k] = 1;
        return combinations[n][k] = combi(n - 1, k) + combi(n - 1, k - 1);
    }
}