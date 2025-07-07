const input = require("fs")
  .readFileSync(process.platform === "linux" ? "/dev/stdin" : "sample.txt")
  .toString()
  .trim()
  .split("\n");

const [n, m] = input[0].split(" ").map(Number);
const board = [];
const visited = [];
for (let i = 0; i < n; i++) {
  board.push(input[1 + i].split(" ").map(Number));
  visited.push([...Array(m)].fill(false));
}
let [H, W, Sr, Sc, Fr, Fc] = input[1 + n].split(" ").map(Number);
Sr--;
Sc--;
Fr--;
Fc--;

const queue = [[Sr, Sc, 0]];
visited[Sr][Sc] = true;
const delta = [
  [0, -1],
  [0, 1],
  [1, 0],
  [-1, 0],
];
let answer = -1;
while (queue.length > 0) {
  let [r, c, sec] = queue.shift();
  if (r === Fr && c === Fc) {
    answer = sec;
    break;
  }
  for (let [dr, dc] of delta) {
    const [nr, nc] = [r + dr, c + dc];
    if (check(nr, nc) && !visited[nr][nc]) {
      visited[nr][nc] = true;
      queue.push([nr, nc, sec + 1]);
    }
  }
}
console.log(answer);

function check(r, c) {
  if (r < 0 || r >= n || c < 0 || c >= m) return false;
  if (r + H - 1 >= n || c + W - 1 >= m) return false;
  for (let i = r; i < r + H; i++) {
    if (board[i][c] === 1) return false;
    if (board[i][c + W - 1] === 1) return false;
  }
  for (let j = c; j < c + W; j++) {
    if (board[r][j] === 1) return false;
    if (board[r + H - 1][j] === 1) return false;
  }
  return true;
}