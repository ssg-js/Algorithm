import java.util.*;
import java.lang.*;
import java.io.*;

class Main {
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        int n = Integer.parseInt(br.readLine());
        String[] str = br.readLine().split(" ");
        
        int sum = 0;
        int max = 0;
        for (int i = 0; i < n; i++) {
            int cur = Integer.parseInt(str[i]);
            if (cur > max) {
                max = cur;
            }
            sum += cur;
        }
        float answer = (float)sum * 100 / (float)max / (float)n;
        
        System.out.println(answer);
        
    }
}