import java.io.*;
import java.util.*;

public class Main {
    private static int n;
    public static void main (String[] args) throws IOException{
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        n = Integer.parseInt(br.readLine());
        PriorityQueue<int[]> pq = new PriorityQueue<int[]>(new Comparator<int[]>() {
            @Override
            public int compare(int[] a, int[] b) {
                if (a[0] != b[0]) return a[0] - b[0];
                return b[1] - a[1];
            }
        });
        for (int i = 0; i < n; i++) {
            StringTokenizer st = new StringTokenizer(br.readLine());
            int d = Integer.parseInt(st.nextToken());
            int w = Integer.parseInt(st.nextToken());
            pq.add(new int[]{d, w});
        }
        PriorityQueue<Integer> solved = new PriorityQueue<>();
        while (!pq.isEmpty()) {
            int[] cur = pq.poll();
            int curD = cur[0];
            int curW = cur[1];
            if (curD > solved.size()) {
                solved.add(curW);
            } else {
                if (solved.peek() > curW) continue;
                solved.poll();
                solved.add(curW);
            }
        }
        int answer = 0;
        while (!solved.isEmpty()) {
            answer += solved.poll();
        }
        System.out.println(answer);
    }
}
