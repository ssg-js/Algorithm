const input = require('fs').readFileSync(process.platform === "linux" ? '/dev/stdin' : 'sample.txt').toString().trim().split('\n');

// 최대 등수와 최소 등수를 구해야함
// 최소 등수는 'x 앞에 있는 학생 수'로 구할 수 있음
// 최대 등수는 'x 뒤에 있는 학생 수'와 '모든 학생 수'로 구할 수 있음
const [n, m, x] = input[0].split(" ").map(Number);
const losers = Array.from(Array(n + 1), () => []); // 낮은 등수애들 체크
const winners = Array.from(Array(n + 1), () => []); // 높은 등수애들 체크
const visitedForLosers = Array.from(Array(n + 1), () => -1); // 아래로 몇명인지 체크
const visitedForWinners = Array.from(Array(n + 1), () => -1); // 위로 몇명인지 체크 

for (let i = 0; i < m; i++) {
  let [a, b] = input[1 + i].split(" ").map(Number);
  losers[a].push(b);
  winners[b].push(a);
}

let rank1 = 1 + getWinners(x);
let rank2 = n - getLosers(x);
console.log(rank1, rank2)


// 그냥 돌리면 1->3->2 의 경우랑 1->2 경우처럼 중복된 경우가 생김 => visited에서 뒤에 몇명있는지를 체크하면 좋을듯
function getLosers(person) { // losers로 돌림, 뒤에 몇명있는지 반환
  if (losers[person].length === 0) { return 0; }

  if (visitedForLosers[person] !== -1) { return visitedForLosers[person]; }

  let ret = 0;
  for (let p of losers[person]) {
    let result = 1 + getLosers(p);
    if (result > ret) { ret = result; } // 최대값 저장 => 중간에 사람이 많은게 더 "정확"한 사람 수임
  }
  visitedForLosers[person] = ret;

  return ret;

}

function getWinners(person) { // winners로 돌림, 앞에 몇명있는지 반환
  if (winners[person].length === 0) { return 0; }

  if (visitedForWinners[person] !== -1) { return visitedForWinners[person]; }

  let ret = 0;
  for (let p of winners[person]) {
    let result = 1 + getWinners(p);
    if (result > ret) { ret = result; } // 최대값 저장 => 중간에 사람이 많은게 더 "정확"한 사람 수임
  }
  visitedForWinners[person] = ret;

  return ret;
}



