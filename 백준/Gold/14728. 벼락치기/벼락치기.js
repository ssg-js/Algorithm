const input = require('fs').readFileSync(process.platform === "linux" ? "/dev/stdin" : "./sample.txt").toString().trim().split("\n");
// https://www.acmicpc.net/problem/14728

const [n, T] = input[0].split(" ").map(Number);
const infos = [];
for (let i = 0; i < n; i++) {
  infos.push(input[1 + i].split(" ").map(Number));
}

const dp = [...Array(n)].map(() => [...Array(T + 1)].map(() => 0));
// 첫 줄 처리
for (let j = infos[0][0]; j < T + 1; j++) {
  dp[0][j] = infos[0][1];
}
// 다음 줄 부터 처리
for (let i = 1; i < n; i++) {
  let [time, points] = infos[i];
  for (let j = 0; j < T + 1; j++) {
    if (j >= time) { dp[i][j] = Math.max(dp[i - 1][j], dp[i - 1][j - time] + points); }
    else { dp[i][j] = dp[i - 1][j]; }
  }
}

console.log(dp[n - 1][T]);
