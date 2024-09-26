const input = require('fs').readFileSync(process.platform === "linux" ? "/dev/stdin" : "./sample.txt").toString().trim().split("\n");
// https://www.acmicpc.net/problem/21610

const d = [[0, 0], [0, -1], [-1, -1], [-1, 0], [-1, 1], [0, 1], [1, 1], [1, 0], [1, -1]];
const [n, m] = input[0].split(" ").map(Number);
const board = [];
for (let i = 0; i < n; i++) {
  board.push(input[1 + i].split(" ").map(Number));
}
let cloud = [[n - 1, 0], [n - 1, 1], [n - 2, 0], [n - 2, 1]]
solve(n, m, cloud, board);


function moveAndWater(n, di, si, cloud, board, visited) {
  // 1. 구름 이동
  for (let i = 0; i < cloud.length; i++) {
    let [x, y] = [(n * si + cloud[i][0] + d[di][0] * si) % n, (n * si + cloud[i][1] + d[di][1] * si) % n];
    cloud[i] = [x, y];
    // 2. 비내리기 3. 구름 사라짐
    board[x][y] += 1;
    visited[x][y] = true;
  }
}

function waterCopy(n, cloud, board) {
  // 4. 물복사버그
  for (let [x, y] of cloud) {
    for (let i = 2; i < d.length; i += 2) {
      let [nx, ny] = [x + d[i][0], y + d[i][1]];

      if (0 <= nx && nx < n && 0 <= ny && ny < n) {
        if (board[nx][ny] > 0) { board[x][y] += 1; }
      }
    }
  }
}

function otherCloudProcess(n, cloud, board, visited) {
  // 5. 구름 재생성
  let beforeCloud = [...cloud];
  cloud = [];
  for (let i = 0; i < n; i++) {
    for (let j = 0; j < n; j++) {
      if (!visited[i][j] && board[i][j] >= 2) {
        cloud.push([i, j]);
        board[i][j] -= 2;
      }
    }
  }
  return cloud;
}

function countWater(n, board) {
  // 물의 양
  let ans = 0;
  for (let i = 0; i < n; i++) {
    for (let j = 0; j < n; j++) {
      ans += board[i][j];
    }
  }
  return ans;
}

function solve(n, m, cloud, board) {
  for (let i = 1 + n; i < 1 + n + m; i++) {
    let [di, si] = input[i].split(" ").map(Number);
    let visited = [...Array(n)].map(() => [...Array(n)].map(() => false));

    moveAndWater(n, di, si, cloud, board, visited);

    waterCopy(n, cloud, board);

    cloud = otherCloudProcess(n, cloud, board, visited);

  }

  console.log(countWater(n, board));
}