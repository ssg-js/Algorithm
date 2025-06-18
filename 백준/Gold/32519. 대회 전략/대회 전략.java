
import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.ArrayList;
import java.util.StringTokenizer;

public class Main {
    static int[][] points, times;
    static int n, t;

    // subtask 객체
    private static class Subtask {
        int time, point;
        Subtask(int time, int point) {
            this.time = time;
            this.point = point;
        }
    }

    // arraylist에 각 서브태스크를 푸는 데 걸리는 점수와 시간을 추가함
    // arr은 넣을 arrayList, idx는 해당 문제를 가리키는 인덱스
    // arraylist와 point, times idx를 받아서 해당 정보로 arraylist 채우기, 아무것도 안 고를 경우도 넣어야함
    // point 값을 합친 값을 들고 있으면서 이전값보다 큰지 비교, time 합친 값도 맥스 값을 넘으면 더 이상 진행하지 않음
    /**
     * 
     * @param arr
     * @param idx
     */
    private static void setList(ArrayList<Subtask> arr, int idx) {
        int totalPoint = 0;
        int totalTime = 0;
        arr.add(new Subtask(totalTime, totalPoint));

        int curMaxPoint = -1;
        for (int i = 0; i < n; i++) {
            totalPoint += points[idx][i];
            totalTime += times[idx][i];
            // 
            if (totalPoint <= curMaxPoint) {
                continue;
            }
            curMaxPoint = totalPoint;
            // 현재 서브태스크를 푸는 데 시간이 기준 시간보다 올라가면 더 이상 담지 않음
            if (totalTime > t) {
                break;
            }
            arr.add(new Subtask(totalTime, curMaxPoint));
        }   
    }

    public static void main (String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer st = new StringTokenizer(br.readLine());
        n = Integer.parseInt(st.nextToken());
        t = Integer.parseInt(st.nextToken());
        points = new int[3][n];
        for (int i = 0; i < 3; i++) {
            st = new StringTokenizer(br.readLine());
            for (int j = 0; j < n; j++) {
                points[i][j] = Integer.parseInt(st.nextToken());
            }
        }
        times = new int[3][n];
        for (int i = 0; i < 3; i++) {
            st = new StringTokenizer(br.readLine());
            for (int j = 0; j < n; j++) {
                times[i][j] = Integer.parseInt(st.nextToken());
            }
        }

        // points와 times을 묶어서 다시 저장
        // 저장하면서 이전 point 값보다 작은 경우(현재 포인트가 음수인 경우)는 저장하지 않음 => 길이가 가변적인 배열이므로 arraylist로 만들기
        ArrayList<Subtask> first = new ArrayList<>();
        setList(first, 0);
        ArrayList<Subtask> second = new ArrayList<>();
        setList(second, 1);
        ArrayList<Subtask> third = new ArrayList<>();
        setList(third, 2);

        // a, b, c 순으로 1, 2, 3번의 서브태스크 번호일 때, c idx를 외부에 저장하고 a, b를 조합해 남은 시간에 해당하는 c문제의 서브테스크를 idx부터 내려가면서 찾기
        int answer = 0;
        for (int i = 0; i < first.size(); i++) {
            int thirdIdx = third.size() - 1;
            Subtask firstSubtask = first.get(i);
            int firstRestTime = t - firstSubtask.time;
            
            // 1번 시간을 뺀 나머지 시간으로
            for (int j = 0; j < second.size(); j++) {
                Subtask secondSubtask = second.get(j);
                int secondRestTime = firstRestTime - secondSubtask.time;
                if (secondRestTime < 0) {
                    break;
                }

                // 1, 2번 시간을 밴 나머지 시간으로 만들 수 있는 가장 큰 3번 문제 값을 찾기
                // third는 뒤에서 부터 검사
                for (int k = thirdIdx; k > -1; k--) {
                    Subtask thirdSubstack = third.get(k);
                    if (secondRestTime >= thirdSubstack.time) {
                        thirdIdx = k;
                        int total = firstSubtask.point + secondSubtask.point + thirdSubstack.point;
                        if (total > answer) {
                            answer = total;
                        }
                        break;
                    }
                }
            }

        }
        System.out.println(answer);

    }
}
