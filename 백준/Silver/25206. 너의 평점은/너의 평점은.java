import java.io.*;
import java.util.*;

public class Main {
    public static void main (String[] args) throws IOException{
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer st;
        int n = 20;

        HashMap<String, Double> map = new HashMap<>();
        map.put("A+", 4.500000);
        map.put("A0", 4.000000);
        map.put("B+", 3.500000);
        map.put("B0", 3.000000);
        map.put("C+", 2.500000);
        map.put("C0", 2.000000);
        map.put("D+", 1.500000);
        map.put("D0", 1.000000);
        map.put("F", 0.000000);


        double sum = 0;
        double points = 0;
        for (int i = 0; i < n; i++) {
            st = new StringTokenizer(br.readLine());
            String tmp1 = st.nextToken();
            double point = Double.parseDouble(st.nextToken());
            String tmp2 = st.nextToken();
            if (tmp2.equals("P")) continue;
            sum += map.get(tmp2) * point;
            points += point;
        }
        double answer = sum / points;
        System.out.printf("%.6f\n", answer);
    }

}
