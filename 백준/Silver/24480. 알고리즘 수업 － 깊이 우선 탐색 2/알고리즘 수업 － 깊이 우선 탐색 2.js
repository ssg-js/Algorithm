const input = require('fs').readFileSync(process.platform === "linux" ? "/dev/stdin" : "./sample1.txt").toString().trim().split("\n");

const [n, m, r] = input[0].split(" ").map(Number);
const edges = [...Array(n + 1)].map(() => []);
for (let i = 0; i < m; i++) {
  const [a, b] = input[1 + i].split(" ").map(Number);
  edges[a].push(b);
  edges[b].push(a);
}

for (let i = 1; i < n + 1; i++) {
  edges[i].sort((a, b) => b - a);
}
const visited = [...Array(n + 1)].map(() => 0); // 0번 인덱스에 현재까지 순서 저장
visited[r] = 1;
visited[0] = 1;

dfs(edges, r, visited);
visited.shift();
console.log(visited.join("\n"))

function dfs(edges, r, visited) {
  for (let node of edges[r]) {
    if (visited[node] > 0) { continue; }
    visited[node] = visited[0] + 1;
    visited[0] += 1;
    dfs(edges, node, visited);
  }
}
