const input = require("fs")
  .readFileSync(process.platform === "linux" ? "/dev/stdin" : "sample.txt")
  .toString()
  .trim()
  .split("\n");

const [n, k] = input[0].split(" ").map(Number);
const dp = [...Array(k)].map(() => Array(n + 1).fill(0n));

// first line
for (let j = 0; j < n + 1; j++) {
  dp[0][j] = BigInt(j + 1);
}

// other lines
for (let i = 1; i < k; i++) {
  for (let j = 0; j < n + 1; j++) {
    dp[i][j] += dp[i - 1][j];
    if (j > 0) dp[i][j] += dp[i][j - 1];
    ``;
  }
}

console.log(String((dp[k - 1][n] - dp[k - 1][n - 1]) % 1000000000n));
