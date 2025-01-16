const input = require('fs').readFileSync(process.platform === "linux" ? '/dev/stdin' : 'sample.txt').toString().trim().split('\n');

const [r, c] = input[0].split(' ').map(Number);
const board = []
for (let i = 1; i < 1 + r; i++) {
  board.push(input[i].trim());
}
const n = Number(input[1 + r]);
const heights = input[2 + r].split(' ').map(Number);

for (let i = 0; i < n; i++) {
  let candi = throwStick(board, heights[i], i);
  let cluster = getFloatingCluster(board, candi);
  if (cluster.length === 0) { continue; }
  fall(board, cluster);
}

console.log(board.join('\n'));

function throwStick(arr, h, side) { // 하나씩 번갈아 때리는 거임
  let [r, c] = [arr.length, arr[0].length];
  let i = r - h;
  let ret = []; // 끊어진 부분 상하좌우에 'x'인 곳
  const delta = [[-1, 0], [1, 0], [0, -1], [0, 1]];
  if (side % 2 === 0) {
    for (let j = 0; j < c; j++) {
      if (arr[i][j] === 'x') {
        arr[i] = arr[i].substring(0, j) + '.' + arr[i].substring(j + 1);
        for (let [dx, dy] of delta) {
          let [nx, ny] = [i + dx, j + dy];
          if (0 <= nx && nx < r && 0 <= ny && ny < c && arr[nx][ny] === 'x') {
            ret.push([nx, ny]);
          }
        }
        break;
      }
    }
  } else {
    for (let j = c - 1; j > -1; j--) {
      if (arr[i][j] === 'x') {
        arr[i] = arr[i].substring(0, j) + '.' + arr[i].substring(j + 1);
        for (let [dx, dy] of delta) {
          let [nx, ny] = [i + dx, j + dy];
          if (0 <= nx && nx < r && 0 <= ny && ny < c && arr[nx][ny] === 'x') {
            ret.push([nx, ny]);
          }
        }
        break;
      }
    }
  }

  return ret;
}

function getFloatingCluster(arr, candi) {
  let ret = [];
  let [r, c] = [arr.length, arr[0].length];
  const delta = [[-1, 0], [0, -1], [0, 1], [1, 0]];
  const visited = [...Array(r)].map(() => [...Array(c)].map(() => false));
  for (let [i, j] of candi) { // 점들마다 클러스터가 땅에 닿아있는지 체크, candi에서 뺀 점들 '.'인지 검사해야함
    if (arr[i][j] === '.') { continue; }
    if (visited[i][j]) { continue; }

    let isFloating = true;
    let tmp = [[i, j]]; // 현재 점을 포함한 클러스터
    let stack = [[i, j]];
    visited[i][j] = true;
    while (stack.length > 0) {
      let [x, y] = stack.pop();
      for (let [dx, dy] of delta) {
        let [nx, ny] = [x + dx, y + dy];
        if (0 <= nx && nx < r && 0 <= ny && ny < c && arr[nx][ny] === 'x') {
          if (visited[nx][ny]) { continue; } // 1. 같은 클러스터 2. 이전에 바닥을 닿았던 클러스터
          if (nx === r - 1) {
            isFloating = false;
            continue;
          } // 땅에 닫아있으면 현재 클러스터 종료
          tmp.push([nx, ny]);
          stack.push([nx, ny]);
          visited[nx][ny] = true;
        }
      }
    }
    if (isFloating) {
      ret = tmp;
      break;
    }
  }
  return ret;
}

function fall(arr, cluster) { // 클러스터의 한 칸 밑이 비었는지 체크하고 하강, 다른 문자로 표시하고 하강이 끝나면 원래 문자로 치환
  if (cluster.length === 0) { return; }
  let points = [...cluster];
  let [r, c] = [arr.length, arr[0].length];
  mark(arr, points);
  loop1: while (true) {
    // 떨어질 수 있는지 체크
    for (let [x, y] of cluster) {
      if (x + 1 >= r || arr[x + 1][y] === 'x') { break loop1; }
    }
    // 중력작용
    for (let [x, y] of points) { // cluster 모든 점 '.'으로 만들기
      arr[x] = arr[x].substring(0, y) + '.' + arr[x].substring(y + 1);
    }
    // cluster 하강하고 다시 'o' 표시
    for (let i = 0; i < points.length; i++) {
      points[i][0] += 1;
      let [x, y] = points[i];
      arr[x] = arr[x].substring(0, y) + 'o' + arr[x].substring(y + 1);
    }
  }
  recover(arr, points);

  return;
}

function mark(arr, points) {
  for (let [x, y] of points) {
    arr[x] = arr[x].substring(0, y) + 'o' + arr[x].substring(y + 1);
  }
  return;
}

function recover(arr, points) {
  for (let [x, y] of points) {
    arr[x] = arr[x].substring(0, y) + 'x' + arr[x].substring(y + 1)
  }
  return;
}
