const input = require('fs').readFileSync(process.platform === "linux" ? "/dev/stdin" : "./sample.txt").toString().trim().split("\n");

const n = Number(input[0]);
const arr = input[1].split(" ").map(Number);
const dp = [...Array(n - 1)].map(() => [...Array(21)].map(() => BigInt(0)));
let curNum, preValue, result;

dp[0][arr[0]] = BigInt(1);

for (let i = 1; i < n - 1; i++) {
  curNum = arr[i];
  for (let num = 0; num < 21; num++) {
    if (dp[i - 1][num] > 0) {
      preValue = BigInt(dp[i - 1][num]);

      result = num - curNum;
      if (result >= 0) { dp[i][result] += preValue; }
      result = num + curNum;
      if (result <= 20) { dp[i][result] += preValue; }
    }
  }
}

console.log((dp[n - 2][arr[n - 1]] === -1 ? 0 : dp[n - 2][arr[n - 1]]).toString());