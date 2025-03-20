const input = require("fs")
  .readFileSync(process.platform === "linux" ? "/dev/stdin" : "sample.txt")
  .toString()
  .trim()
  .split("\n");

const n = Number(input[0]);
const info = input[1].trim();
const edges = [...Array(n)].map(() => []);
const memo = [...Array(n)].map(() => Object());
for (let i = 2; i < 2 + n - 1; i++) {
  let [a, b] = input[i].split(" ").map((v) => Number(v) - 1);
  edges[a].push(b);
  edges[b].push(a);
}

let answer = 0;
const visited = [...Array(n)].map(() => false);
for (let i = 0; i < n; i++) {
  if (info[i] == 0) continue;
  visited[i] = true;
  answer += recur(i);
  visited[i] = false;
}
console.log(answer);


// 끝에서부터 산책로 갯수를 세서 반환
function recur(cur) {
  let ret = 0;
  for (let next of edges[cur]) {
    if (visited[next]) { continue; }
    if (memo[cur][next] !== undefined) {
      ret += memo[cur][next];
    } else if (info[next] == 1) {
      ret += 1;
      memo[cur][next] = 1;
    } else {
      visited[next] = true;
      let result = recur(next);
      ret += result;
      memo[cur][next] = result;
      visited[next] = false;
    }
  }
  return ret;
}