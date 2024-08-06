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

const [n, m] = input[0].split(" ").map(Number);
const board = [...Array(100001)].fill(0); // 방문 후 2
const delta = [
  function (x) { return x - 1; },
  function (x) { return x + 1; },
  function (x) { return x * 2; }
];
let queue = new Queue();
let cnt, nx;

board[n] = 1;

(() => {
  if (n === m) {
    console.log(0);
    return;
  }

  queue.push(n);
  cnt = 0;

  while (queue.count > 0) {
    let len = queue.count;
    cnt += 1;

    for (let i = 0; i < len; i++) {
      const x = queue.pop();
      for (let func of delta) {
        nx = func(x);
        if (0 <= nx && nx <= 100001 && board[nx] === 0) {
          if (nx === m) {
            console.log(cnt);
            return;
          }
          queue.push(nx);
          board[nx] = 1;
        }
      }
    }
  }

})();
