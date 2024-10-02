const input = require('fs').readFileSync(process.platform === "linux" ? "/dev/stdin" : "./sample1.txt").toString().trim().split("\n");
// https://www.acmicpc.net/problem/2610

let n = Number(input[0]);
let m = Number(input[1]);
const edges = [...Array(n + 1)].map(() => []);
const groupNum = [...Array(n + 1)].map((_, i) => i);
let cnt = 0;
const answer = [];
const visited = [...Array(n + 1)].map(() => false);

for (let i = 0; i < m; i++) {
  let [a, b] = input[i + 2].split(" ").map(Number);
  edges[a].push(b);
  edges[b].push(a);
  union(a, b);
}
for (let i = 1; i < n + 1; i++) {
  find(i);
}


for (let i = 1; i < groupNum.length; i++) {
  if (visited[i] === true) { continue; }
  cnt++;
  const iter = [];
  let retNum = 0;
  let minDeliveryTime = 10000;
  let num = groupNum[i];
  // 같은 그룹애들 구하기
  for (let j = 1; j <= groupNum.length; j++) {
    if (groupNum[j] === num) {
      iter.push(j);
      visited[j] = true;
    }
  }

  // 대표자 선정
  for (let chosen of iter) {
    let tempTime = bfs(chosen);
    if (tempTime < minDeliveryTime) {
      minDeliveryTime = tempTime;
      retNum = chosen;
    }
  }

  answer.push(retNum);
}
answer.sort((a, b) => a - b);
console.log([cnt, ...answer].join('\n'));

function find(p) {
  if (groupNum[p] === p) { return p; }
  groupNum[p] = find(groupNum[p]);
  return groupNum[p];
}

function union(a, b) {
  na = find(a);
  nb = find(b);
  if (na < nb) {
    groupNum[nb] = na;
  } else {
    groupNum[na] = nb;
  }
}

function bfs(k) {
  let queue = [k];
  let idx = 0;
  let cnt = 0;
  let visited = [...Array(n + 1)].map(() => false);
  visited[k] = true;
  while (queue.length > idx) {
    let limit = queue.length - idx;
    for (let i = 0; i < limit; i++) {
      let cur = queue[idx];
      idx++;
      for (let nk of edges[cur]) {
        if (visited[nk] === false) {
          queue.push(nk);
          visited[nk] = true;
        }
      }
    }
    cnt++;
  }

  return cnt;
}
