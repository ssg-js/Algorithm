const input = require('fs').readFileSync(process.platform === "linux" ? '/dev/stdin' : 'sample.txt').toString().trim().split('\n');

const n = Number(input[0]);
let prices = [];
let total = 0; // 모든 가격 더했을 때 최댓값, 최대 50 * 10,000 = 500,000
for (let i = 0; i < n; i++) { // N
  prices.push(Number(input[1 + i]));
  total += prices[i];
}
prices.sort((a, b) => a - b); // Nlog(N)
const newPrices = []; // [가격, 갯수] 로 정리
let preNum = -1; // 이전 가격
let cnt = -1; // preNum 가격 갯수
let zero = 1;
for (let i = 0; i < n; i++) { // N
  if (preNum !== prices[i]) { // 새로운 가격
    if (preNum === 0) {
      zero += cnt;
    } else if (cnt != -1) { newPrices.push([preNum, cnt]); }
    preNum = prices[i];
    cnt = 1;
    continue;
  }
  // 같은 가격
  cnt += 1;
}
newPrices.push([preNum, cnt]);

// 소수 먼저 구하기 total까기, 10000 * N
const primeNums = Array.from(Array(total + 1), () => true); // 최대 1MB
primeNums[0] = false;
primeNums[1] = false;
for (let i = 2; i < total + 1; i++) {
  if (!primeNums[i]) { continue; }
  for (let j = i * 2; j < total + 1; j = j + i) {
    primeNums[j] = false;
  }
}
// dp : i번째 사탕가격까지 사용해서 j라는 가격을 만드는 경우의 수
const dp = Array(total + 1).fill(0);
dp[0] = 1;
let maxNum = 0;
for (let [price, cnt] of newPrices) {
  for (let i = maxNum; i >= 0; i--) { // price 더할 가격. i가 0부터 올라간다면, i를 처리할 때 i-1에서 이미 처리한 경우를 중복해서 처리함
    for (let j = 1; j <= cnt; j++) {
      let cur = i + price * j;
      if (cur > total) { break; } // 넘치면 break, total 넘는 경우가 없음
      if (maxNum < cur) { maxNum = cur; } // 처리한 경우의 가격의 최댓값을 저장해서 그만큼만 뒤에 검사
      dp[cur] += dp[i] // i값에서 현재 cur값을 만들었으므로 더해줌
    }
  }
}

let answer = 0;
for (let j = 2; j <= maxNum; j++) {
  if (primeNums[j]) { answer += dp[j]; }
}
console.log(answer * zero);