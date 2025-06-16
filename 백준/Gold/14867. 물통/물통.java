
import java.io.*;
import java.util.*;

public class Main {
    private static int volumeA, volumeB, targetA, targetB;
    private static boolean[][] visited;

    static class State {
        int A = 0;
        int B = 0;
        State (int a, int b) {
            this.A = a;
            this.B = b;
        }
    }

    private static int bfs() {
        Queue<State> queue = new LinkedList();
        visited = new boolean[volumeA + 1][volumeB + 1];
        queue.add(new State(0, 0));
        visited[0][0] = true;
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
                if (!visited[volumeA][cur.B]) {
                    queue.add(new State(volumeA, cur.B));
                    visited[volumeA][cur.B] = true;
                }
                // b
                if (!visited[cur.A][volumeB]) {
                    queue.add(new State(cur.A, volumeB));
                    visited[cur.A][volumeB] = true;
                }
                // empty
                // a
                if (!visited[0][cur.B]) {
                    queue.add(new State(0, cur.B));
                    visited[0][cur.B] = true;
                }
                // b
                if (!visited[cur.A][0]) {
                    queue.add(new State(cur.A, 0));
                    visited[cur.A][0] = true;
                }

                // move
                // a -> b
                int nextB = cur.B + cur.A;
                int nextA = Math.max(0, nextB - volumeB);
                nextB = Math.min(nextB, volumeB);
                if (!visited[nextA][nextB]) {
                    queue.add(new State(nextA, nextB));
                    visited[nextA][nextB] = true;
                }
                // b <- a
                nextA = cur.A + cur.B;
                nextB = Math.max(0, nextA - volumeA);
                nextA = Math.min(nextA, volumeA);
                if (!visited[nextA][nextB]) {
                    queue.add(new State(nextA, nextB));
                    visited[nextA][nextB] = true;
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
