const input = require("fs")
  .readFileSync(process.platform === "linux" ? "/dev/stdin" : "sample.txt")
  .toString()
  .trim()
  .split("\n");

const [n, k] = input[0].split(" ").map(Number);
const dp = [...Array(k)].map(() => Array(n + 1).fill(0n));

// first line
for (let j = 0; j < n + 1; j++) {
  dp[0][j] = 1n;
}

// other lines
for (let i = 1; i < k; i++) {
  for (let j = 0; j < n + 1; j++) {
    for (let prev = j; prev >= 0; prev--) {
      dp[i][j] += dp[i - 1][prev];
    }
  }
}

console.log(String(dp[k - 1][n] % 1000000000n));
