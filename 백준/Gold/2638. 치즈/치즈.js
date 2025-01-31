const input = require('fs').readFileSync(process.platform === "linux" ? '/dev/stdin' : 'sample.txt').toString().trim().split('\n');

const [n, m] = input[0].split(" ").map(Number);
const board = [];
const cheeze = [];
for (let i = 0; i < n; i++) {
  board.push(input[1 + i].split(" ").map(Number));
  for (let j = 0; j < m; j++) {
    if (board[i][j] === 1) {
      cheeze.push([i, j]);
    }
  }
}
const delta = [[0, 1], [0, -1], [1, 0], [-1, 0]]
board[0][0] = -1
outerCheck([0, 0]);
let cnt = 0;
let outerSide;
while (cheeze.length > 0) {
  cnt += 1
  // 사라질 치즈 찾기
  let toRemove = []; // 없어질 치즈들
  let size = cheeze.length;
  for (let k = 0; k < size; k++) {
    let [i, j] = cheeze.shift();
    outerSide = 0;
    for (let [di, dj] of delta) {
      let [ni, nj] = [i + di, j + dj];
      if (0 <= ni && ni < n && 0 <= nj && nj < m && board[ni][nj] === -1) {
        outerSide += 1;
      }
    }
    if (outerSide >= 2) {
      toRemove.push([i, j]);
    } else {
      cheeze.push([i, j]);
    }
  }
  // 사라질 치즈 제거 후 외부환경 다시 산정
  for (let [x, y] of toRemove) {
    board[x][y] = -1;
  }
  outerCheck(...toRemove);
}

console.log(cnt);


function outerCheck(...args) {
  let q = [...args];
  while (q.length > 0) {
    let [i, j] = q.shift();
    for (let [di, dj] of delta) {
      let [ni, nj] = [i + di, j + dj];
      if (0 <= ni && ni < n && 0 <= nj && nj < m && board[ni][nj] === 0) {
        board[ni][nj] = -1;
        q.push([ni, nj]);
      }
    }
  }
}
