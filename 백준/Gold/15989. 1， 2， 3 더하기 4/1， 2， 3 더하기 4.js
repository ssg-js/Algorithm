/**
 * 1, 2, 3 더하기 4
 * 바텀업 1, 2, 3 으로 만들기
 * 1로만 만드는 경우 다 1
 * 1, 2로 a 만드는 경우 = (1로만 a만드는 경우) + (1, 2로 a만드는 경우) = dp[1][a] + dp[2][a-2]
 */

const input = require("fs")
  .readFileSync(process.platform === "linux" ? "/dev/stdin" : "sample.txt")
  .toString()
  .trim()
  .split("\n");

const t = Number(input[0]);
let answer = "";
for (let tc = 0; tc < t; tc++) {
  const n = Number(input[tc + 1]);
  const dp = [...Array(4)].map(() => Array(n + 1).fill(0));
  // first line
  for (let j = 0; j < n + 1; j++) {
    dp[1][j] = 1;
  }
  // other lines
  for (let i = 2; i < 4; i++) {
    for (let j = 0; j < n + 1; j++) {
      dp[i][j] = dp[i - 1][j];
      if (j - i >= 0) {
        dp[i][j] += dp[i][j - i];
      }
    }
  }
  answer += dp[3][n] + "\n";
}
console.log(answer);
