import java.io.*;
import java.util.*;

public class Main {
    public static void main (String[] args) throws IOException{
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        int n = Integer.parseInt(br.readLine());
        int answer = 0;
        for (int i = 0; i < n; i++) {
            String s = br.readLine();
            HashMap<Character, Boolean> map = new HashMap<>();
            char prev = s.charAt(0);
            int count = 1;
            map.put(prev, true);
            for (int j = 1; j < s.length(); j++) {
                char c = s.charAt(j);
                if (prev != c) {
                    if (map.containsKey(c)) break;
                    prev = c;
                    map.put(c, true);
                }
                count++;
            }
            if (count == s.length()) answer++;
        }
        System.out.println(answer);
    }

}
