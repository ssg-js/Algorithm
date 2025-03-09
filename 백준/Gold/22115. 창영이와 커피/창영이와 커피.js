const input = require("fs")
  .readFileSync(process.platform === "linux" ? "/dev/stdin" : "sample.txt")
  .toString()
  .trim()
  .split("\n");

const [n, k] = input[0].split(" ").map(Number);
const arr = input[1].split(" ").map(Number);
const dp = [...Array(n)].map(() => Array(k + 1).fill(Infinity));
for (let i = 0; i < n; i++) {
  dp[i][0] = 0;
}

for (let i = 0; i < n; i++) {
  let v = arr[i];
  if (i === 0) {
    dp[i][v] = 1;
    continue;
  }
  // 두번째 줄부터
  for (let j = 0; j < k + 1; j++) {
    if (j === v) {
      dp[i][j] = 1;
      continue;
    }
    dp[i][j] = dp[i - 1][j];
    if (j < v) { continue; } // v값보다 작은 애들은 위에꺼 들어오기만함
    let alt = dp[i - 1][j - v] + 1;
    if (alt < dp[i][j]) { dp[i][j] = alt; }
  }
}

if (dp[n - 1][k] !== Infinity) {
  console.log(dp[n - 1][k]);
} else {
  console.log(-1)
}
