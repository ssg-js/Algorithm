const input = require('fs').readFileSync(process.platform === "linux" ? '/dev/stdin' : 'sample.txt').toString().trim().split('\n');

// 최대 등수와 최소 등수를 구해야함
// 최소 등수는 'x 앞에 있는 학생 수'로 구할 수 있음
// 최대 등수는 'x 뒤에 있는 학생 수'와 '모든 학생 수'로 구할 수 있음
const [n, m, x] = input[0].split(" ").map(Number);
const losers = Array.from(Array(n + 1), () => []); // 낮은 등수애들 체크
const winners = Array.from(Array(n + 1), () => []); // 높은 등수애들 체크
const visitedForLosers = Array.from(Array(n + 1), () => false); // 아래로 몇명인지 체크
const visitedForWinners = Array.from(Array(n + 1), () => false); // 위로 몇명인지 체크 

for (let i = 0; i < m; i++) {
  let [a, b] = input[1 + i].split(" ").map(Number);
  losers[a].push(b);
  winners[b].push(a);
}

let rank1 = get(x, visitedForWinners, winners);
let rank2 = n - get(x, visitedForLosers, losers) + 1;
console.log(rank1, rank2);


// 앞(winner), 뒤(losers)에서 몇번째인지
function get(person, visited, arr) {
  if (visited[person]) { return 0; }
  visited[person] = true;

  let ret = 0;
  for (let p of arr[person]) {
    ret += get(p, visited, arr);
  }

  return 1 + ret;

}


