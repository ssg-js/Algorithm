const input = require("fs")
  .readFileSync(process.platform === "linux" ? "/dev/stdin" : "sample.txt")
  .toString()
  .trim()
  .split("\n");

const [n, m] = input[0].split(" ").map(Number);
const oneWay = [...Array(n + 1)].map(() => Array(n + 1).fill(false));
const twoWay = [...Array(n + 1)].map(() => Array(n + 1).fill(false));
for (let i = 0; i < m; i++) {
  let [u, v, b] = input[1 + i].split(" ").map(Number);
  twoWay[u][v] = true;
  twoWay[v][u] = true;
  if (b === 1) {
    oneWay[u][v] = true;
    oneWay[v][u] = true;
  } else {
    oneWay[u][v] = true;
  }
}

const table = [...Array(n + 1)].map(() => Array(n + 1).fill(Infinity));
for (let i = 1; i < n + 1; i++) {
  table[i][i] = 0;
  for (let j = 1; j < n + 1; j++) {
    if (!twoWay[i][j]) continue;
    if (oneWay[i][j]) table[i][j] = 0;
    else table[i][j] = 1;
  }
}

for (let k = 1; k < n + 1; k++) {
  for (let i = 1; i < n + 1; i++) {
    for (let j = 1; j < n + 1; j++) {
      table[i][j] = Math.min(table[i][j], table[i][k] + table[k][j]);
    }
  }
}

const k = Number(input[1 + m]);
let answer = "";
for (let i = 0; i < k; i++) {
  let [s, e] = input[2 + m + i].split(" ").map(Number);
  answer += `${table[s][e]}\n`;
}
console.log(answer);