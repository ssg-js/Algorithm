
import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.math.BigInteger;
import java.util.Arrays;

public class Main {
    private static BigInteger BASE = BigInteger.valueOf(36);
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));

        int n = Integer.parseInt(br.readLine());
        // 전체 합(BigInteger)
        BigInteger sum = BigInteger.ZERO;
        // 각 숫자의 갯수에 각 숫자와 z의 차이를 곱하고, 자릿수까지 더한 걸 저장 => 각 숫자를 z로 바꿨을 때, 얼마나 증가하는지 알 수 있는 배열
        BigInteger[] board = new BigInteger[36];
        for (int i = 0; i < board.length; i++) {
            board[i] = BigInteger.ZERO;
        }

        for (int i = 0; i < n; i++) {
            String line = br.readLine().toUpperCase();
            sum = sum.add(toDecimal(line));
            // 각 숫자 처리

            int lineLength = line.length();
            for (int j = 0; j < line.length(); j++) {
                char number = line.charAt(j);
                int pos = lineLength-1-j;
                int numberForIdx = toDecimalNumber(number); // -> 현재 숫자 10진수로 전환한 값, board 인덱스로도 쓰임

                BigInteger increase = BigInteger.valueOf(35 - toDecimalNumber(number)).multiply(BASE.pow(pos)); // -> board에 저장될 값
                board[numberForIdx] = board[numberForIdx].add(increase);
            }
        }
        int k = Integer.parseInt(br.readLine());

        Arrays.sort(board, (a, b) -> b.compareTo(a));

        
        for (int i = 0; i < k; i++) {
            sum = sum.add(board[i]);
        }
        System.out.println(to36(sum));
    }

    private static int toDecimalNumber(char number) { // v
        if (0 <= number - '0' && number - '0' <= 9) {
            return number - '0';
        } else if ('A' <= number && number <= 'Z') {
            return number - 'A' + 10;
        }
        System.out.println("Wrong Format");
        System.out.println(number);
        return -1;
        
    }

    private static char to36Number(int number) { // v
        if (0 <= number && number <= 9) {
            return (char) ('0' + number);
        } else if (10 <= number && number < 36) {
            return (char) ('A' + number - 10);
        }
        return 'f';
    }

    // 36진수 -> 10진수
    private static BigInteger toDecimal(String input) { // v
        BigInteger ret = new BigInteger("0");
        for (int i = 0; i < input.length(); i++) {
            int pos = input.length() - 1 - i;
            BigInteger digit = BASE.pow(pos);

            BigInteger value = new BigInteger(Integer.toString(toDecimalNumber(input.charAt(i))));
            ret = ret.add(value.multiply(digit));
        }
        return ret;
    }

    private static String to36(BigInteger input) { // v
        if (input.equals(BigInteger.ZERO)) return "0";
        StringBuilder ret = new StringBuilder();

        BigInteger zero = new BigInteger("0");
        while (input.compareTo(zero) == 1) {
            int remainder = input.mod(BASE).intValue();
            ret.append(to36Number(remainder));
            input = input.divide(BASE);
        }

        return ret.reverse().toString();
    }
}
