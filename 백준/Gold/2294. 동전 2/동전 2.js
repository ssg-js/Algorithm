const input = require('fs').readFileSync(process.platform === "linux" ? "/dev/stdin" : "./sample.txt").toString().trim().split("\n");
// https://www.acmicpc.net/problem/9084

/**
 * 현재 동전을 포함해 현재 값을 만드는 최소 값을 만들 때, 현재 동전을 쓰는 경우와 안쓰는 경우에서, 현재 이전의 동전까지 쓰는 경우와, 현재 동전을 쓰는 경우를 쓰게
 * i = 현재동전까지 쓰는 경우, j = 만들 값
 * j를 만드는 현재 동전 갯수 = min(현재 동전을 포함하지 않고 j를 만들 때 갯수의 최소값, 현재 동전을 포함해서 j를 만들 때 갯수의 최소값)
 * dp[i][j] = min(dp[i-1][j], dp[i][j-(현재동전값)] + 1)
 * 현재 동전값이 j를 넘어가면?????? 그때까진 위의 값을 그대로 들고와야함(dp[i-1][j])
 * 전체 0으로 초기화할 경우 0이 최솟값이라 값이 제대로 안나옴 => 100000으로 초기화 => dp[n][k]값이 100000인 경우 답은 -1
 */

const [n, k] = input[0].split(" ").map(Number);
const coinValues = [0];
for (let i = 0; i < n; i++) {
  coinValues.push(Number(input[1 + i]));
}
const dp = [...Array(n + 1)].map(() => [...Array(k + 1)].map(() => 100000));

dp[0][0] = 0;
for (let i = 1; i < n + 1; i++) {
  for (let j = 0; j < k + 1; j++) {
    if (coinValues[i] > j) { dp[i][j] = dp[i - 1][j]; }
    else { dp[i][j] = Math.min(dp[i - 1][j], dp[i][j - coinValues[i]] + 1); }
  }
}
console.log(dp[n][k] !== 100000 ? dp[n][k] : -1);