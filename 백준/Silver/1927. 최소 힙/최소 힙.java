import java.util.*;
import java.io.*;

class Main {
    
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        int n = Integer.parseInt(br.readLine());
        PriorityQueue<Integer> minQueue = new PriorityQueue<Integer>();
        
        int input;
        StringBuilder sb = new StringBuilder();
        for (int i = 0; i < n; i++) {
            input = Integer.parseInt(br.readLine());
            if (input > 0) {
                minQueue.add(input);
            } else {
                if (!minQueue.isEmpty()) {
                    sb.append(minQueue.poll()).append('\n');
                } else {
                    sb.append(0).append('\n');
                }
            }
        }
        System.out.println(sb);
    }
}