const input = require('fs').readFileSync(process.platform === "linux" ? "/dev/stdin" : "./sample.txt").toString().trim().split("\n");

const [n, m] = input[0].split(" ").map(Number);
const board = []; // 방문 후 2
const delta = [[-1, 0], [0, 1], [1, 0], [0, -1]];
let queue = [];
let width, nx, ny;
let picCnt = 0;
let maxWidth = 0;

for (let i = 1; i < 1 + n; i++) {
  board.push(input[i].split(" ").map(Number));
}

for (let i = 0; i < n; i++) {
  for (let j = 0; j < m; j++) {
    if (board[i][j] === 1) {
      picCnt += 1;
      queue = [[i, j]];
      board[i][j] = 2;
      width = 1;

      while (queue.length > 0) {
        const [x, y] = queue.shift();
        for (let [dx, dy] of delta) {
          nx = x + dx;
          ny = y + dy;
          if (0 <= nx && nx < n && 0 <= ny && ny < m && board[nx][ny] === 1) {
            queue.push([nx, ny]);
            board[nx][ny] = 2;
            width += 1;
          }
        }
      }

      if (width > maxWidth) { maxWidth = width; }
    }
  }
}

console.log(picCnt + '\n' + maxWidth);