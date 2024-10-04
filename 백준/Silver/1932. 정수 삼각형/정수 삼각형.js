const input = require('fs').readFileSync(process.platform === "linux" ? "/dev/stdin" : "./sample.txt").toString().trim().split("\n");

const n = Number(input[0]);
const infos = [];
const dp = [];
for (let i = 0; i < n; i++) {
  infos.push(input[1 + i].split(" ").map(Number));
  dp.push([...Array(i + 1)].map(() => 0));
}

for (let i = 0; i < n; i++) {
  dp[n - 1][i] = infos[n - 1][i];
}

for (let i = n - 2; i > -1; i--) {
  for (let j = 0; j < i + 1; j++) {
    dp[i][j] = Math.max(infos[i][j] + dp[i + 1][j], infos[i][j] + dp[i + 1][j + 1]);
  }
}

console.log(dp[0][0]);
