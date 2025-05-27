/**
 * 50C1 + 50C2 + ... + 50C50 = 50 + 50 * 49 / 2 + 50 * 49 * 48 / 6 + ... => 시간초과
 * a, b, c 의 최대공약수 = a, b의 최대공약수와 c의 최대공약수 => 여기서 필요한 건 a,b 의 최대공약수를 바로 구하는 것
 * dp[i][j] = i번째 수까지 배합했을 때 최대공약수가 j인 것의 갯수
 *
 * gcd를 log(Si) 로 구해야함
 */

const input = require("fs")
  .readFileSync(process.platform === "linux" ? "/dev/stdin" : "../sample.txt")
  .toString()
  .trim()
  .split("\n");

const n = Number(input[0]);
const numbers = [];
let maxNumber = 0;
for (let i = 1; i < 1 + n; i++) {
  let v = Number(input[i]);
  numbers.push(v);
  if (v > maxNumber) maxNumber = v;
}
const dp = [...Array(n)].map(() => Array(maxNumber + 1).fill(0));
dp[0][numbers[0]] = 1; // 첫줄
for (let i = 1; i < n; i++) {
  let number = numbers[i];
  dp[i][number] += 1; // 자기자신
  for (let j = 1; j < maxNumber + 1; j++) {
    dp[i][j] += dp[i - 1][j];
    if (dp[i - 1][j] === 0) continue; // i-1까지 사용해서 j가 최대공약수인 경우가 없다면 i번째 수와 최대공약수를 구할 필요가 없음
    let gcd = getGCD(number, j);
    dp[i][gcd] += dp[i - 1][j]; // i-1까지 수를 골라 최대공약수가 나오는 경우가 더해짐
    dp[i][gcd] %= 10000003;
  }
}
console.log(dp[n - 1][1] % 10000003);

function getGCD(a, b) {
  if (b < a) [a, b] = [b, a];
  while (b % a !== 0) {
    b = b % a;
    [a, b] = [b, a];
  }
  return a;
}
