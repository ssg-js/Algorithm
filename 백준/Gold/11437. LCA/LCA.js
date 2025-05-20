/**
 * lca
 *
 * 최소 두가지로 나눠지는 트리를 생각했는데 자식이 하나인 트리면 터짐
 */

const input = require("fs")
  .readFileSync(process.platform === "linux" ? "/dev/stdin" : "sample.txt")
  .toString()
  .trim()
  .split("\n");

const n = Number(input[0]);
const edges = [...Array(n + 1)].map(() => []);
for (let i = 1; i < n; i++) {
  let [a, b] = input[i].split(" ").map(Number);
  edges[a].push(b);
  edges[b].push(a);
}

const depths = Array(n + 1).fill(-1);
const parents = [...Array(n + 1)].map(() =>
  Array(Math.floor(Math.log2(n)) + 1).fill(-1)
);
depths[1] = 1;
setDepth();

let answer = "";
const m = Number(input[n]);
for (let i = 1 + n; i < 1 + n + m; i++) {
  let [a, b] = input[i].split(" ").map(Number);
  answer += findLCA(a, b);
  answer += "\n";
}
console.log(answer);

function setDepth(cur = 1) {
  for (let child of edges[cur]) {
    if (depths[child] !== -1) continue;
    depths[child] = depths[cur] + 1;
    // 2^k번째 부모정보 채우기
    for (let i = 0; i < Math.floor(Math.log2(depths[child])) + 1; i++) {
      if (i === 0) {
        parents[child][i] = cur;
      } else {
        parents[child][i] = parents[parents[child][i - 1]][i - 1];
      }
      if (parents[child][i] === 1) {
        break;
      }
    }
    setDepth(child);
  }
}

function findLCA(a, b) {
  if (depths[a] > depths[b]) [a, b] = [b, a]; // a가 깊이가 적은거로
  b = findParent(b, depths[a]);

  if (a === b) return a;

  // 레벨 공통 조상 중 가장 가까운 조상 찾기
  let ret = 0;
  for (let i = Math.floor(Math.log2(depths[a] - 1)); i > -1; i--) {
    if (parents[a][i] !== parents[b][i]) {
      a = parents[a][i];
      b = parents[b][i];
    }
    ret = parents[a][i];
  }

  return ret;
}

function findParent(a, depth) {
  if (depths[a] === depth) return a;

  while (depths[a] !== depth) {
    let dis = depths[a] - depth;
    for (let i = 0; i < n; i++) {
      if (Math.pow(2, i) > dis) {
        dis -= Math.pow(2, i - 1);
        a = parents[a][i - 1];
        break;
      }
    }
  }

  return a;
}
