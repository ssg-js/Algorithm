const input = require('fs').readFileSync(process.platform === "linux" ? "/dev/stdin" : "./sample.txt").toString().trim().split("\n");

const n = Number(input[0]);
const wellPrice = [];
const prices = [];
for (let i = 0; i < n; i++) {
  wellPrice.push(Number(input[1 + i]));
}
for (let i = 0; i < n; i++) {
  prices.push([...input[n + 1 + i].split(" ").map(Number), wellPrice[i]]);
}
prices.push([...wellPrice, 0]);

const queue = [];
for (let i = 0; i < n + 1; i++) {
  for (let j = i + 1; j < n + 1; j++) {
    queue.push([prices[i][j], i, j]);
  }
}
queue.sort((a, b) => a[0] - b[0]);

let group = [...Array(n + 1)].map((_, i) => i);
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

