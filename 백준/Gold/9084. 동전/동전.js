const input = require('fs').readFileSync(process.platform === "linux" ? "/dev/stdin" : "./sample.txt").toString().trim().split("\n");
// https://www.acmicpc.net/problem/9084

/**
 * 1. 완탐 : 각 동전을 1~10000(최대)개까지 생각하며 경우의 수를 센다 => 복잡도 계산이 안됨
 * 2. dp : 한정된 가격을 채우기 위해 최대 20개의 동전을 사용 => 20 * 10000
 *         dp[i][j]의 값은 j 값을 만들기위해 i까지 동전을 써서 만들수 있는 모든 경우의 수
 */

const t = Number(input[0]);
for (let c = 0; c < t; c++) {
  const n = Number(input[1 + 3 * c]);
  const coinValues = [0];
  coinValues.push(...input[1 + 3 * c + 1].split(" ").map(Number));
  const targetValue = Number(input[1 + 3 * c + 2]);
  const dp = [...Array(n + 1)].map(() => [...Array(targetValue + 1)].map(() => 0));

  for (let i = 1; i < n + 1; i++) {
    for (let j = 1; j < targetValue + 1; j++) {
      dp[i][j] = dp[i - 1][j]
      if (j >= coinValues[i]) {
        dp[i][j] += dp[i][j - coinValues[i]]
      }
      if (j === coinValues[i]) {
        dp[i][j] += 1;
      }
    }
  }

  console.log(dp[n][targetValue]);
}
