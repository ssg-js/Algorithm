
const input = require("fs")
  .readFileSync(process.platform === "linux" ? "/dev/stdin" : "../sample.txt")
  .toString()
  .trim()
  .split("\n");
const n = Number(input[0]);
const state = input[1].split(" ").map(BigInt);
let answer = 0n;
let sectionSize = 0;
let firstSectionSize = 0;
let idx = 0;
// 1번을 포함한 구역
for (let i = 0; i < n; i++) {
  if (state[i] > 0n) break;
  firstSectionSize++;
  idx++;
}
// 나머지 구역
for (let i = idx; i < n; i++) {
  const v = state[i];
  if (v > 0n) {
    // 쪽방
    let count = Math.floor(sectionSize / 2);
    if (sectionSize % 2 > 0) count++;
    answer += v + BigInt(count);
    sectionSize = 0;
  } else {
    // 구역
    sectionSize++;
  }
}
firstSectionSize += sectionSize;
let count = Math.floor(firstSectionSize / 2);
if (firstSectionSize !== n && firstSectionSize % 2 > 0) count++;
answer += BigInt(count);

console.log(answer.toString());
