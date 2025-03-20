const input = require("fs")
  .readFileSync(process.platform === "linux" ? "/dev/stdin" : "sample.txt")
  .toString()
  .trim()
  .split("\n");

const [n, h] = input[0].split(" ").map(Number);
const board = Array(h).fill(0);
if (n % 2 === 1) {
  board[0] += Math.floor(n / 2) + 1;
} else {
  board[0] += Math.floor(n / 2);
}

for (let i = 0; i < n; i++) {
  let size = Number(input[1 + i]);
  if (i % 2 === 0) { // 석순 : idx 0 부터 size전까지
    board[size] -= 1;
  } else { // 종유석 : idx h-size부터 n전까지
    board[h - size] += 1;
  }
}

let minObs = board[0];
let count = 1;
for (let i = 1; i < h; i++) {
  board[i] += board[i - 1];
  if (board[i] === minObs) {
    count++;
  } else if (board[i] < minObs) {
    minObs = board[i];
    count = 1;
  }
}


console.log(minObs, count);