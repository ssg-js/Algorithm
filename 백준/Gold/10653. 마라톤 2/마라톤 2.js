const input = require('fs').readFileSync(process.platform === "linux" ? '/dev/stdin' : 'sample.txt').toString().trim().split('\n');

const [n, k] = input[0].split(" ").map(Number);
const points = [[]];
for (let i = 0; i < n; i++) {
  points.push(input[1 + i].split(" ").map(Number));
}

const dp = [];
for (let i = 0; i < n + 1; i++) {
  dp.push([]);
  for (let j = 0; j < k + 1; j++) {
    dp[i].push(Infinity);
  }
}

recur(n, k);

console.log(Math.min(...dp[n]))


function recur(cur, pass) {
  if (cur === 1) { return 0; }

  if (dp[cur][pass] !== Infinity) { return dp[cur][pass] }

  let ret = Infinity;
  for (let i = 0; i < pass + 1; i++) {
    if (cur - 1 - i < 1) { continue; } // 최소 1번 체크포인트까지만. 번호가 그보다 작으면 안함.
    ret = Math.min(ret, distance(cur, cur - 1 - i) + recur(cur - 1 - i, pass - i));
  }

  dp[cur][pass] = ret;

  return ret;
}

function distance(a, b) {
  return Math.abs(points[a][0] - points[b][0]) + Math.abs(points[a][1] - points[b][1]);
}