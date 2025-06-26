
import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.StringTokenizer;

public class Main {
    private static int MIN_VALUE = -32768000;
    public static void main (String[] args) throws IOException{
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer st = new StringTokenizer(br.readLine());
        int n = Integer.parseInt(st.nextToken());
        int m = Integer.parseInt(st.nextToken());

        int[][] contain = new int[n+1][m+1];
        int[][] notContain = new int[n+1][m+1];
        for (int i = 0; i < n+1; i++) {
            for (int j = 1; j < m+1; j++) {
                contain[i][j] = MIN_VALUE;
                notContain[i][j] = MIN_VALUE;
            }
            
        }
        for (int i = 1; i < n+1; i++) {
            int number = Integer.parseInt(br.readLine());
            for (int j = 1; j <= (i + 1) / 2; j++) {
                if (j > m) break;
                notContain[i][j] = Math.max(contain[i-1][j], notContain[i-1][j]);
                contain[i][j] = Math.max(notContain[i-1][j-1] + number, contain[i-1][j] + number);
            }
        }
        System.out.println(Math.max(notContain[n][m], contain[n][m]));
    }
}
