const input = require('fs').readFileSync(process.platform === "linux" ? "/dev/stdin" : "./sample1.txt").toString().trim().split("\n");

const [n, m] = input[0].split(' ').map(Number);
const arr = input[1].split(' ').map(Number);

const primeNumBoard = [...Array(10000)].map(() => true);
primeNumBoard[0] = false;
primeNumBoard[1] = false;
for (let i = 2; i < primeNumBoard.length; i++) {
  if (!primeNumBoard[i]) { continue; }

  for (let k = i + i; k < primeNumBoard.length; k = k + i) {
    primeNumBoard[k] = false;
  }
}

let answer = [];

function solve(idx, depth, value) {
  if (depth === 0) {
    if (primeNumBoard[value] && !answer.includes(value)) {
      answer.push(value);
    }
    return;
  }
  if (idx === arr.length) { return; }

  solve(idx + 1, depth - 1, value + arr[idx]);
  solve(idx + 1, depth, value);
}

solve(0, m, 0);
answer.sort((a, b) => a - b);
if (answer.length > 0) {
  console.log(...answer);
} else { console.log(-1); }