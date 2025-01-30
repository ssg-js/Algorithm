const input = require('fs').readFileSync(process.platform === "linux" ? '/dev/stdin' : 'sample.txt').toString().trim().split('\n');

const n = Number(input[0]);
const m = Number(input[1]);

const board = [];
for (let i = 0; i < n; i++) {
  board.push([]);
  for (let j = 0; j < n; j++) {
    board[i].push(i === j ? 0 : Infinity);
  }
}

for (let i = 0; i < m; i++) {
  let [a, b, c] = input[2 + i].split(" ").map(Number);
  if (c < board[a - 1][b - 1]) {
    board[a - 1][b - 1] = c;
  }
}

for (let k = 0; k < n; k++) {
  for (let i = 0; i < n; i++) {
    for (let j = 0; j < n; j++) {
      if (i === j || i === k || j === k) { continue; }

      if (board[i][k] + board[k][j] < board[i][j]) {
        board[i][j] = board[i][k] + board[k][j];
      }
    }
  }
}

let answer = ``;
for (let i = 0; i < n; i++) {
  for (let j = 0; j < n; j++) {
    answer += `${board[i][j] === Infinity ? 0 : board[i][j]} `;
  }
  answer += `\n`;
}

console.log(answer)

