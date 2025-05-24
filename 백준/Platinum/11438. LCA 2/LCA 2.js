/**
 * lca 2
 * 노드의 개수가 100,000개, 주어지는 순서쌍이 100,000개일 때 두 순서쌍의 가장 가까운 공통 조상 노드를 출력하기
 * 트리 만들기: 각 노드의 2^k번째 조상을 저장 -> 부모 정보를 가져와서 만들기 -> 100,000 * log(100,000)
 * 순서쌍으로 갯수 찾기: 한번 찾는데 log(100,000) 그리고 총 갯수 100,000
 * 총 시간 : 3.4*10^6 -> O(nlog(n))
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
const parents = [...Array(n + 1)].map(() => []);
parents[1].push(-1);
depths[1] = 1;
setTree();

const m = Number(input[n]);
let answer = "";
for (let i = 1 + n; i < 1 + n + m; i++) {
  let [a, b] = input[i].split(" ").map(Number);
  answer += findLCA(a, b) + "\n";
}
console.log(answer);

function setTree(cur = 1) {
  for (let child of edges[cur]) {
    if (depths[child] !== -1) continue;
    depths[child] = depths[cur] + 1;
    // 2^k번째 조상 넣어주기
    parents[child].push(cur);
    let idx = 0;
    while (depths[child] - (1 << idx) > 0) {
      idx++;
    }
    for (let i = 1; i < idx; i++) {
      parents[child].push(parents[parents[child][i - 1]][i - 1]);
    }
    setTree(child);
  }
}

function findLCA(a, b) {
  if (depths[a] > depths[b]) [a, b] = [b, a];
  // depth 맞추기
  b = findParent(b, depths[a]);

  if (a === b) return a;

  // 같은 가장 가까운 공통 조상 -> 같지 않은 가장 먼 (depth가 같은) 조상의 바로 위 부모
  // 두번째로 가장 멀리 있는 조상부터 비교하면서 같지 않은 조상이 나오면 갱신
  let ret = 0;
  for (let k = Math.floor(Math.log2(depths[a] - 1)); k > -1; k--) {
    if (parents[a][k] !== parents[b][k]) {
      a = parents[a][k];
      b = parents[b][k];
    }
    ret = parents[a][k];
  }
  return ret;
}

// 해당 dep인 조상 반환
function findParent(a, depth) {
  if (depths[a] < depth) return console.log("error");

  while (depths[a] > depth) {
    a = parents[a][Math.floor(Math.log2(depths[a] - depth))];
  }

  return a;
}
