/**
 * 큐로 주어진 방문 순서를 하나씩 꺼내기
 * 처음엔 1번, 그 다음부턴 현재 나온 방문 순서와 연결된(그리고 방문하지 않은) 다음 노드를 저장해놓기
 * 노드 배열이 비었다면 다시 스택에서 꺼내서 반복
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

const queue = input[n].split(" ").map(Number);
console.log(solve());

function solve() {
  let nextNodes = new Set([1]);
  const visited = Array(n + 1).fill(false);

  while (queue.length > 0) {
    let cur = queue.shift();
    visited[cur] = true;
    if (nextNodes.size > 0 && !nextNodes.has(cur)) return 0;
    nextNodes = new Set();
    for (let node of edges[cur]) {
      if (visited[node]) continue;
      nextNodes.add(node);
    }
  }
  return 1;
}
