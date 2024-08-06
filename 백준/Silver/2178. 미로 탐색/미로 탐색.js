const input = require('fs').readFileSync(process.platform === "linux" ? "/dev/stdin" : "./sample.txt").toString().trim().split("\n");

const [n, m] = input[0].split(" ").map(Number);
const board = []; // 방문 후 2
const delta = [[-1, 0], [0, 1], [1, 0], [0, -1]];
let queue = [];
let cnt, nx, ny;

for (let i = 1; i < 1 + n; i++) {
  board.push(Array.from(input[i]).map(Number));
}

queue.push([0, 0]);
board[0][0] = 2;

(() => {
  cnt = 1;
  while (queue.length > 0) {
    let len = queue.length;
    for (let i = 0; i < len; i++) {
      const [x, y] = queue.shift();
      for (let [dx, dy] of delta) {
        nx = x + dx;
        ny = y + dy;
        if (0 <= nx && nx < n && 0 <= ny && ny < m && board[nx][ny] === 1) {
          if (nx === n - 1 && ny === m - 1) {
            console.log(cnt + 1);
            return;
          }
          queue.push([nx, ny]);
          board[nx][ny] = 2;
        }
      }
    }

    cnt += 1;
  }

})();