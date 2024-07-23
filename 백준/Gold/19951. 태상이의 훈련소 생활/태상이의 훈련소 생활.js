const input = require('fs').readFileSync(process.platform === "linux" ? "/dev/stdin" : "./sample.txt").toString().trim().split("\n");

const [n, m] = input[0].split(" ").map(Number);
const initBoard = input[1].split(" ").map(Number);
const prefixSum = [...Array(n)].map(() => 0);

for (let i = 2; i < 2 + m; i++) {
  let [start, end, value] = input[i].split(" ").map(Number);

  start -= 1;
  end -= 1;
  prefixSum[start] += value;
  if (end + 1 < n) { prefixSum[end + 1] += -value; }
}

initBoard[0] += prefixSum[0];
for (let i = 1; i < n; i++) {
  prefixSum[i] = prefixSum[i - 1] + prefixSum[i];
  initBoard[i] += prefixSum[i];
}

console.log(initBoard.join(" "));