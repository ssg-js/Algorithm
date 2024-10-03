const input = require('fs').readFileSync(process.platform === "linux" ? "/dev/stdin" : "./sample1.txt").toString().trim().split("\n");
// https://www.acmicpc.net/problem/2610

let n = Number(input[0]);
let m = Number(input[1]);
const INF = 100000
let table = [...Array(n + 1)].map(() => [...Array(n + 1)].map(() => INF))
for (let i = 0; i < table.length; i++) {
  table[i][i] = 0;
}
for (let i = 2; i < 2 + m; i++) {
  let [a, b] = input[i].split(" ").map(Number);
  table[a][b] = 1;
  table[b][a] = 1;
}

for (let k = 1; k < n + 1; k++) {
  for (let i = 1; i < n + 1; i++) {
    for (let j = 1; j < n + 1; j++) {
      if (i === j || i === k || j === k) { continue; }
      table[i][j] = Math.min(table[i][j], table[i][k] + table[k][j]);
    }
  }
}

let cnt = 0;
let repNum = [];
const visited = [...Array(n + 1)].map(() => false);
for (let i = 1; i < n + 1; i++) {
  if (visited[i] === true) { continue; }
  cnt++;
  const sameGroup = [];
  for (let k = i; k < n + 1; k++) {
    if (table[i][k] !== INF) {
      sameGroup.push(k);
      visited[k] = true;
    }
  }

  let minTime = INF;
  let minK = INF;
  for (let k of sameGroup) {
    let maxTime = 0;
    for (let nk of sameGroup) {
      maxTime = Math.max(maxTime, table[k][nk]);
    }
    if (maxTime < minTime) {
      minTime = maxTime;
      minK = k;
    }
  }
  repNum.push(minK);
}

repNum.sort((a, b) => a - b);
console.log([cnt, ...repNum].join('\n'))