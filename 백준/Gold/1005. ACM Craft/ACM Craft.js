const input = require('fs').readFileSync(process.platform === "linux" ? '/dev/stdin' : 'sample.txt').toString().trim().split('\n');

const tc = Number(input[0]);
let plus = 0;
for (let z = 0; z < tc; z++) {
  const [n, k] = input[1 + plus].split(" ").map(Number);
  const costs = input[1 + plus + 1].split(" ").map(Number);
  const baseBuildings = [...Array(n)].map(() => []);
  for (let i = 0; i < k; i++) {
    let [a, b] = input[1 + plus + 2 + i].split(" ").map((v) => Number(v) - 1);
    baseBuildings[b].push(a);
  }
  const target = Number(input[1 + plus + 2 + k]) - 1;
  const memo = Array(n).fill(-1); // i건물이 짓기위한 최소의 시간
  console.log(recur(target, memo, baseBuildings, costs));

  plus += 3 + k;
}


function recur(cur, memo, baseBuildings, costs) { // cur 건물을 짓기위한 최소의 시간 반환
  if (memo[cur] >= 0) { return memo[cur]; }

  let ret = 0;
  for (let b of baseBuildings[cur]) {
    let result = recur(b, memo, baseBuildings, costs);
    if (result > ret) { ret = result; }
  }

  memo[cur] = costs[cur] + ret;

  return memo[cur];
}
