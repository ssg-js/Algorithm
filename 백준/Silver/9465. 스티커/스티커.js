const input = require('fs').readFileSync(process.platform === "linux" ? '/dev/stdin' : 'sample.txt').toString().trim().split('\n');

for (let t = 0; t < Number(input[0]); t++) {
  let n = Number(input[1 + (t * 3)]);
  const arr = [];
  for (let i = 0; i < 2; i++) {
    arr.push([0, ...input[2 + (t * 3) + i].split(" ").map(Number)]);
  }
  const dp = [...Array(2)].map(() => [...Array(n + 1)].map(() => 0));
  // 첫 번째 값 넣기
  dp[0][1] = arr[0][1];
  dp[1][1] = arr[1][1];
  // 위, 아래로 번갈아가며 dp값 채우기
  for (let j = 2; j < n + 1; j++) {
    dp[0][j] = Math.max(dp[1][j - 1] + arr[0][j], dp[0][j - 1]);
    dp[1][j] = Math.max(dp[0][j - 1] + arr[1][j], dp[1][j - 1]);
  }
  console.log(Math.max(dp[0][n], dp[1][n]));
}