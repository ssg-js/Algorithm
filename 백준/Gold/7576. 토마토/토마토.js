const input = require('fs').readFileSync(process.platform === "linux" ? "/dev/stdin" : "./sample.txt").toString().trim().split("\n");

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

const [m, n] = input[0].split(" ").map(Number);
const board = []; // 방문 후 2
const delta = [[-1, 0], [0, 1], [1, 0], [0, -1]];
let queue = new Queue();
let cnt, nx, ny;

for (let i = 1; i < 1 + n; i++) {
  board.push(input[i].split(" ").map(Number));
  for (let j = 0; j < m; j++) {
    if (board[i - 1][j] === 1) {
      queue.push([i - 1, j]);
    }
  }
}



(() => {
  let isRipe = false;
  let isUnRipe = false;
  let unRipeCnt = 0;
  for (let i = 0; i < n; i++) {
    for (let j = 0; j < m; j++) {
      if (board[i][j] === 1) { isRipe = true; }
      if (board[i][j] === 0) {
        isUnRipe = true;
        unRipeCnt += 1;
      }
    }
  }

  if (isRipe === true && isUnRipe === false) {
    console.log(0);
    return;
  }

  cnt = -1;
  while (queue.count > 0) {
    let len = queue.count;
    cnt += 1;

    for (let i = 0; i < len; i++) {
      const [x, y] = queue.pop();
      for (let [dx, dy] of delta) {
        nx = x + dx;
        ny = y + dy;
        if (0 <= nx && nx < n && 0 <= ny && ny < m && board[nx][ny] === 0) {
          queue.push([nx, ny]);
          unRipeCnt -= 1;
          board[nx][ny] = 1;
        }
      }
    }
  }

  if (unRipeCnt > 0) { console.log(-1); }
  else { console.log(cnt); }
})();
