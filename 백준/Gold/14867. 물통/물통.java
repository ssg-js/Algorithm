
import java.io.*;
import java.util.*;

public class Main {
    private static int volumeA, volumeB, targetA, targetB;
    private static HashSet<String> visited;

    static class State {
        int A = 0;
        int B = 0;
        State (int a, int b) {
            this.A = a;
            this.B = b;
        }
    }

    private static String makeKey(int a, int b) {
        return Integer.toString(a) + "," + Integer.toString(b);
    }

    private static int bfs() {
        Queue<State> queue = new LinkedList<>();
        visited = new HashSet<>();
        queue.add(new State(0, 0));
        visited.add(makeKey(0, 0));
        int count = 0;
        while (!queue.isEmpty()) {
            int size = queue.size();
            for (int s = 0; s < size; s++) {
                State cur = queue.poll();
                // answer
                if (cur.A == targetA && cur.B == targetB) {
                    return count;
                }
                // fill
                // a
                String key;
                key = makeKey(volumeA, cur.B);
                if (!visited.contains(key)) {
                    queue.add(new State(volumeA, cur.B));
                    visited.add(key);
                }
                // b
                key = makeKey(cur.A, volumeB);
                if (!visited.contains(key)) {
                    queue.add(new State(cur.A, volumeB));
                    visited.add(key);
                }
                // empty
                // a
                key = makeKey(0, cur.B);
                if (!visited.contains(key)) {
                    queue.add(new State(0, cur.B));
                    visited.add(key);
                }
                // b
                key = makeKey(cur.A, 0);
                if (!visited.contains(key)) {
                    queue.add(new State(cur.A, 0));
                    visited.add(key);
                }

                // move
                // a -> b
                int nextB = cur.B + cur.A;
                int nextA = Math.max(0, nextB - volumeB);
                nextB = Math.min(nextB, volumeB);
                key = makeKey(nextA, nextB);
                if (!visited.contains(key)) {
                    queue.add(new State(nextA, nextB));
                    visited.add(key);
                }
                // b <- a
                nextA = cur.A + cur.B;
                nextB = Math.max(0, nextA - volumeA);
                nextA = Math.min(nextA, volumeA);
                key = makeKey(nextA, nextB);
                if (!visited.contains(key)) {
                    queue.add(new State(nextA, nextB));
                    visited.add(key);
                }
                
            }
            count++;
        }
        return -1;
    }
    
    public static void main (String args[]) throws IOException{
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer st = new StringTokenizer(br.readLine());
        volumeA = Integer.parseInt(st.nextToken());
        volumeB = Integer.parseInt(st.nextToken());
        targetA = Integer.parseInt(st.nextToken());
        targetB = Integer.parseInt(st.nextToken());

        System.out.println(bfs());
        
    }  

    

    
}
