const input = require('fs').readFileSync(process.platform === "linux" ? '/dev/stdin' : 'sample.txt').toString().trim().split('\n');

const n = Number(input[0]);
const m = Number(input[1]);
const state = [];
for (let i = 0; i < n; i++) {
  state.push(input[2 + i].split(" ").map(Number));
}
const travel = input[2 + n].split(" ").map((v) => Number(v) - 1);
// 도시별(0~n-1) 소속 집합(길을 통해 도달가능한 도시끼리 같은 집합)
const parent = [...Array(n)].map((_, i) => i);
// parent 만들기
for (let i = 0; i < n; i++) {
  for (let j = i + 1; j < n; j++) {
    if (state[i][j] === 1) { union(i, j); }
  }
}
// m에 대해서 처리
let answer = 'YES';
if (m > 0) {
  const p = find(travel[0]);
  for (let i = 1; i < m; i++) {
    let city = travel[i];
    if (p !== find(city)) {
      answer = 'NO';
      break;
    }
  }
}
console.log(answer);


function find(x) {
  if (x === parent[x]) { return x; }
  let ret = find(parent[x]);
  parent[x] = ret;
  return ret;
}


function union(x, y) {
  let px = find(x);
  let py = find(y);
  if (px > py) { parent[px] = py; }
  else { parent[py] = px; }
}