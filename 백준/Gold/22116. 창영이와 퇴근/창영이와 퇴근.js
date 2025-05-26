class PriorityQueue {
  constructor(compare = (a, b) => a - b) {
    this.queue = [];
    this.size = 0;
    this.compare = compare;
  }

  insert(v) {
    this.queue.push(v);
    this.size++;
    let cur = this.size - 1;
    let parent = Math.floor((cur - 1) / 2);
    while (cur > 0 && this.compare(this.queue[cur], this.queue[parent]) < 0) {
      [this.queue[cur], this.queue[parent]] = [
        this.queue[parent],
        this.queue[cur],
      ];
      cur = parent;
      parent = Math.floor((cur - 1) / 2);
    }
  }

  poll() {
    if (this.size === 1) {
      this.size--;
      this.first = null;
      return this.queue.pop();
    }

    let ret = this.queue[0];
    if (typeof this.queue[0] === Array) {
      ret = [...this.queue[0]];
    }
    this.queue[0] = this.queue.pop();
    this.size--;
    let cur = 0;
    let child = 2 * cur + 1;
    if (
      child + 1 < this.size &&
      this.compare(this.queue[child + 1], this.queue[child]) < 0
    ) {
      child++;
    }
    while (
      child < this.size &&
      this.compare(this.queue[child], this.queue[cur]) < 0
    ) {
      [this.queue[cur], this.queue[child]] = [
        this.queue[child],
        this.queue[cur],
      ];
      cur = child;
      child = 2 * child + 1;
      if (
        child + 1 < this.size &&
        this.compare(this.queue[child + 1], this.queue[child]) < 0
      ) {
        child++;
      }
    }
    return ret;
  }

  isEmpty() {
    if (this.size === 0) return true;
    return false;
  }
}
const input = require("fs")
  .readFileSync(process.platform === "linux" ? "/dev/stdin" : "sample.txt")
  .toString()
  .trim()
  .split("\n");

const n = Number(input[0]);
const board = [];
for (let i = 1; i < n + 1; i++) {
  board.push(input[i].split(" ").map(Number));
}
console.log(solve());

function solve() {
  const pq = new PriorityQueue((a, b) => a[0] - b[0]);
  const delta = [
    [-1, 0],
    [0, 1],
    [1, 0],
    [0, -1],
  ];
  const dist = [...Array(n)].map(() => Array(n).fill(1000000000));
  pq.insert([0, 0, 0]); // [이 루트로 만난 경사값중 최댓값, 좌표]
  dist[0][0] = 0;
  while (!pq.isEmpty()) {
    let [maxSlope, x, y] = pq.poll();
    if (maxSlope != 0 && maxSlope > dist[x][y]) continue;

    for (let [dx, dy] of delta) {
      [nx, ny] = [x + dx, y + dy];
      if (nx < 0 || nx >= n || ny < 0 || ny >= n) continue;
      let nextMaxSlope = Math.max(
        maxSlope,
        Math.abs(board[x][y] - board[nx][ny])
      );
      if (nextMaxSlope < dist[nx][ny]) {
        dist[nx][ny] = nextMaxSlope;
        pq.insert([nextMaxSlope, nx, ny]);
      }
    }
  }
  return dist[n - 1][n - 1];
}
