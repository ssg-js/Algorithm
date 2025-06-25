import java.io.*;
import java.util.*;

public class Main {
    public static void main (String[] args) throws IOException{
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        int n = Integer.parseInt(br.readLine());
        StringTokenizer st = new StringTokenizer(br.readLine());
        int[] arr = new int[n];
        for (int i = 0; i < n; i++) {
            arr[i] = Integer.parseInt(st.nextToken());
        }
        int answer = 0;
        HashMap<Integer, Boolean> dp = new HashMap<>(); // 현재까지 수를 두개 골라서 나올 수 있는 합
        for (int i = 1; i < arr.length; i++) {
            // dp 채우기
            for (int j = 0; j < i; j++) {
                dp.put(arr[j] + arr[i-1], true);
            }
            for (int j = 0; j < i; j++) {
                // 하나를 세번
                if (arr[j] * 3 == arr[i]) {
                    answer++;
                    break;
                }
                // 하나 고르고 나머지 두개 고르기
                int value = arr[i] - arr[j];
                if (dp.containsKey(value)) {
                    answer++;
                    break;
                }
            }
            
        }
        System.out.println(answer );

    }


}
