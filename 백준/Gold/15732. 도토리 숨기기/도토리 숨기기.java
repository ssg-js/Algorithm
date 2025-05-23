/* 
 * 도토리 숨기기
 * 상자의 개수 N(1 ≤ N ≤ 1,000,000)과 규칙의 개수 K(1 ≤ K ≤ 10,000), 도토리의 개수 D(1 ≤ D ≤ 1,000,000,000)
 * 각 상자에 간격에 맞춰 도토리를 넣으면 O(N * K)라서 시간초과
 * 이분 탐색으로 상자를 고르고(log(n)) 그 상자까지의 도토리 개수를 구하기(k) => O(klog(n))
 * 그 상자까지의 도토리 갯수는 k개의 정보에서 구할 수 있음
 * 고려할 점 : 현재 박스가 마지막 도토리가 들어가있는 경우 => 딱 맞추거나, 모자른 경우가 있음
 * 고려할 점 : 나올 수 있는 최대 도토리 갯수가 10^10 > 2^31 - 1 이므로 long으로 해야함 
 * 고려할 점 : 현재까지 도토리 개수가 정확히 현재 상자까지 인지를 확인해야함
 * => 예를 들어, cur 상자에서 k개의 정보로 도토리 갯수를 구하는데, 모든 도토리를 숨기는 정보에서 마지막으로 넣은 도토리가 cur보다 앞이라면 현재 cur은 답이아님.
*/


import java.io.*;
import java.util.StringTokenizer;

public class Main {
    public static void main(String[] args) throws IOException{
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer st = new StringTokenizer(br.readLine());
        int n = Integer.parseInt(st.nextToken());
        int k = Integer.parseInt(st.nextToken());
        int d = Integer.parseInt(st.nextToken());
        int[][] info = new int[k][3];
        for (int i = 0; i < k; i++) {
            st = new StringTokenizer(br.readLine());
            int a = Integer.parseInt(st.nextToken());
            int b = Integer.parseInt(st.nextToken());
            int c = Integer.parseInt(st.nextToken());
            info[i][0] = a;
            info[i][1] = b;
            info[i][2] = c;
        }
        int left = 1;
        int right = n;
        while (left <= right) {
            int curBox = (left + right) / 2; // 현재 상자
            long count = 0; // 현재 상자까지의 도토리 개수
            for (int i = 0; i < k; i++) {
                int start = info[i][0];
                int end = Math.min(info[i][1], curBox);
                if (start > end) continue; // 현재 상자까지 갯수에 영향을 안줌
                int div = info[i][2];
                int number = (end - start) / div + 1;
                count += number;
                if (count > d) continue;
            }
            if (count < d) {
                left = curBox + 1;
            } else {
                right = curBox - 1;
            }
        }
        System.out.println(right+1);
    }
}
