const input = require('fs').readFileSync(process.platform === "linux" ? '/dev/stdin' : 'sample.txt').toString().trim().split('\n');

const [n, m, k] = input[0].split(' ').map(Number);
const board = [];
for (let i = 1; i < 1 + n; i++) {
  board.push(input[i].split(' ').map(Number));
}
const operations = [];
for (let i = 1 + n; i < 1 + n + k; i++) {
  operations.push(input[i].split(' ').map(Number));
}
// 연산 순서 정하고 rotate 후 배열의 최소값 도출
const answers = [];
for (let combi of shuffle(k)) {
  let copy = [];
  for (let a of board) {
    copy.push([...a]);
  }
  for (let i of combi) {
    rotate(copy, ...operations[i]);
  }
  answers.push(getValue(copy));
}
console.log(Math.min(...answers));


function shuffle(n, depth = 0) {
  const ret = [];
  if (depth === n) { return [[]]; }
  for (let i = 0; i < n; i++) {
    for (let combi of shuffle(n, depth + 1)) {
      if (combi.includes(i)) { continue; }
      ret.push([i, ...combi]);
    }
  }
  return ret;
}

function rotate(arr, r, c, s) { // r, c를 기준으로 s개의 테두리 회전
  r -= 1;
  c -= 1;
  for (let k = 1; k < s + 1; k++) {
    let first = arr[r - k][c - k];
    // 왼쪽
    for (let i = r - k; i < r + k; i++) {
      arr[i][c - k] = arr[i + 1][c - k];
    }
    // 아래
    for (let j = c - k; j < c + k; j++) {
      arr[r + k][j] = arr[r + k][j + 1];
    }
    // 오른쪽
    for (let i = r + k; i > r - k; i--) {
      arr[i][c + k] = arr[i - 1][c + k];
    }
    // 위
    for (let j = c + k; j > c - k + 1; j--) {
      arr[r - k][j] = arr[r - k][j - 1];
    }
    arr[r - k][c - k + 1] = first;
  }
}

function getValue(arr) {
  const sums = [];
  for (let i = 0; i < arr.length; i++) {
    sums.push(arr[i].reduce((acc, cur) => acc + cur, 0));
  }
  return Math.min(...sums);
}