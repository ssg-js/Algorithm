const input = require('fs').readFileSync(process.platform === "linux" ? "/dev/stdin" : "./sample.txt").toString().trim().split("\n");
// https://www.acmicpc.net/problem/4179
// node
class Node {
  constructor(value) {
    this.value = value;
    this.next = null;
    this.prev = null;
  }

}

// queue
class Queue {
  constructor() {
    this.init();
  }

  init() {
    this.count = 0;
    this.start = null;
    this.end = null;
  }

  push(value) {
    const node = new Node(value);

    if (this.count === 0) {
      this.start = node;
      this.end = node;
    } else {
      const endOfQueue = this.end;
      endOfQueue.next = node;
      node.prev = endOfQueue;
      this.end = node;
    }

    this.count += 1;
  }

  pop() {
    if (this.count === 0) { return; }

    const value = this.start.value;

    if (this.count === 1) {
      this.init();
    } else {
      this.start = this.start.next;
      this.start.prev = null;
      this.count -= 1;
    }

    return value;
  }
}

const [n, m] = input[0].split(" ").map(Number);
const board = []; // 방문 후 2
const delta = [[-1, 0], [0, 1], [1, 0], [0, -1]];
let playerQueue = new Queue();
let fireQueue = new Queue();
let cnt, nx, ny;

for (let i = 1; i < 1 + n; i++) {
  board.push(Array.from(input[i].slice(0, m)));
  for (let j = 0; j < m; j++) {
    if (board[i - 1][j] === "J") { playerQueue.push([i - 1, j]); }
    if (board[i - 1][j] === "F") { fireQueue.push([i - 1, j]); }
  }
}

(() => {
  cnt = 0;
  while (playerQueue.count > 0) {
    let len = playerQueue.count;
    cnt += 1;

    for (let i = 0; i < len; i++) {
      const [x, y] = playerQueue.pop();
      if (board[x][y] === "F") { continue; } // https://www.acmicpc.net/board/view/141761
      if (x === 0 || x === n - 1 || y === 0 || y === m - 1) {
        console.log(cnt);
        return;
      }
      for (let [dx, dy] of delta) {
        nx = x + dx;
        ny = y + dy;
        if (0 <= nx && nx < n && 0 <= ny && ny < m && board[nx][ny] === ".") {
          // 여기서 return 처리하면 안됨 => 불이 번지는 케이스 후에 처리해야함
          playerQueue.push([nx, ny]);
          board[nx][ny] = "J";
        }
      }
    }

    len = fireQueue.count;
    for (let i = 0; i < len; i++) {
      const [x, y] = fireQueue.pop();

      for (let [dx, dy] of delta) {
        nx = x + dx;
        ny = y + dy;
        if (0 <= nx && nx < n && 0 <= ny && ny < m && (board[nx][ny] === "." || board[nx][ny] === "J")) {
          fireQueue.push([nx, ny]);
          board[nx][ny] = "F";
        }
      }
    }
  }

  console.log("IMPOSSIBLE");

})();
