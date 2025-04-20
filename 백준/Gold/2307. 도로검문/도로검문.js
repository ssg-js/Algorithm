// 도로검문
const input = require("fs")
  .readFileSync(process.platform === "linux" ? "/dev/stdin" : "../sample.txt")
  .toString()
  .trim()
  .split("\n");

const [n, m] = input[0].split(" ").map(Number);
const edges = [...Array(n + 1)].map(() => []); // i번째 노드에 연결된 점, 거리 정보
for (let i = 0; i < m; i++) {
  let [a, b, c] = input[1 + i].split(" ").map(Number);
  edges[a].push([b, c]);
  edges[b].push([a, c]);
}
let latency = 0;
const originalDist = [...Array(n + 1)].fill(Infinity);
const pq = [[0, 1]]; // [거리, 노드]
originalDist[1] = 0;
while (pq.length > 0) {
  const [dist, node] = minHeapPop(pq);
  if (dist > originalDist[node]) continue; // 이미 더 짧은 경로가 존재
  for (const [nextNode, nextDist] of edges[node]) {
    if (originalDist[nextNode] > dist + nextDist) {
      originalDist[nextNode] = dist + nextDist;
      minHeapPush(pq, [originalDist[nextNode], nextNode]);
    }
  }
}

for (let del = 2; del < n; del++) {
  const delDist = [...Array(n + 1)].fill(Infinity);
  pq.push([0, 1]);
  delDist[1] = 0;
  while (pq.length > 0) {
    const [dist, node] = minHeapPop(pq);
    if (dist > delDist[node]) continue; // 이미 더 짧은 경로가 존재
    for (const [nextNode, nextDist] of edges[node]) {
      if (nextNode === del) continue; // 삭제할 노드
      if (delDist[nextNode] > dist + nextDist) {
        delDist[nextNode] = dist + nextDist;
        minHeapPush(pq, [delDist[nextNode], nextNode]);
      }
    }
  }
  let v = delDist[n] - originalDist[n];
  if (latency < v) {
    latency = v;
  }
}
if (latency === Infinity) {
  console.log(-1);
} else {
  console.log(latency);
}
function minHeapPush(arr, v) {
  arr.push(v);
  let idx = arr.length - 1;
  let parent = Math.floor((idx - 1) / 2);
  while (idx > 0 && arr[parent][0] > arr[idx][0]) {
    [arr[parent], arr[idx]] = [arr[idx], arr[parent]];
    idx = parent;
    parent = Math.floor((idx - 1) / 2);
  }
}

function minHeapPop(arr) {
  if (arr.length === 0) return null;
  if (arr.length === 1) return arr.pop();
  const ret = [...arr[0]];
  arr[0] = arr.pop();
  let idx = 0;
  let child = 1;
  if (child + 1 < arr.length && arr[child][0] > arr[child + 1][0]) {
    child++;
  }
  while (child < arr.length && arr[child][0] < arr[idx][0]) {
    [arr[child], arr[idx]] = [arr[idx], arr[child]];
    idx = child;
    child = child * 2 + 1;
    if (child + 1 < arr.length && arr[child][0] > arr[child + 1][0]) {
      child++;
    }
  }
  return ret;
}
