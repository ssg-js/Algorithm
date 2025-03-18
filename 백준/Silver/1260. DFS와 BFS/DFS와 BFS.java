import java.util.*;
import java.io.*;

class Main {
    static int n, m, v;
    static StringBuilder sb = new StringBuilder();
    static ArrayList<Integer>[] edges;
    static boolean[] visited;
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer st = new StringTokenizer(br.readLine());
        n = Integer.parseInt(st.nextToken());
        m = Integer.parseInt(st.nextToken());
        v = Integer.parseInt(st.nextToken()) - 1;
        edges = new ArrayList[n];
        for (int i = 0; i < n; i++) edges[i] = new ArrayList<>();
        for (int i = 0; i < m; i++) {
            st = new StringTokenizer(br.readLine());
            int a = Integer.parseInt(st.nextToken()) - 1;
            int b = Integer.parseInt(st.nextToken()) - 1;
            edges[a].add(b);
            edges[b].add(a);
        }
        for (int i = 0; i < n; i++) edges[i].sort(null);
        
        visited = new boolean[n];
        visited[v] = true;
        dfs(v);
        sb.append("\n");
        bfs(v);
        System.out.println(sb);
    }
    
    static void dfs(int v) {
        sb.append(v+1).append(" ");
        for (int nv : edges[v]) {
            if (!visited[nv]) {
                visited[nv] = true;
                dfs(nv);
            }
        }
    }
    
    static void bfs(int v) {
        visited = new boolean[n];
        visited[v] = true;
        ArrayDeque<Integer> queue = new ArrayDeque<>();
        queue.add(v);
        while (!queue.isEmpty()) {
            int cur = queue.poll();
            sb.append(cur + 1).append(" ");
            for (int nv : edges[cur]) {
                if (!visited[nv]) {
                    visited[nv] = true;
                    queue.add(nv);
                }
            }
        }
    }
}