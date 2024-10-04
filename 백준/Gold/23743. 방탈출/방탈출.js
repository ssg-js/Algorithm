const input = require('fs').readFileSync(process.platform === "linux" ? "/dev/stdin" : "./sample.txt").toString().trim().split("\n");

const [n, m] = input[0].split(" ").map(Number);

const queue = [];
for (let i = 0; i < m; i++) {
  let [x, y, cost] = input[1 + i].split(" ").map(Number);
  queue.push([cost, x, y]);
}
input[m + 1].split(" ").map(Number).forEach((v, i) => {
  queue.push([v, i + 1, n + 1]);
})
queue.sort((a, b) => a[0] - b[0]);

let group = [...Array(n + 2)].map((_, i) => i);
let answer = 0;
let cnt = 0;
for (let [cost, x, y] of queue) {
  if (find(group, x) === find(group, y)) { continue; }
  cnt++;
  answer += cost;
  union(group, x, y);
  if (cnt === n) { break; }
}
console.log(answer);

function find(board, x) {
  if (board[x] === x) { return x; }
  board[x] = find(board, board[x]);
  return board[x];
}

function union(board, x, y) {
  x = find(board, x);
  y = find(board, y);
  if (x < y) {
    board[y] = x;
  } else {
    board[x] = y;
  }
}

