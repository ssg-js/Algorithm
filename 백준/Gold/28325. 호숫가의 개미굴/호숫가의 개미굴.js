
const input = require("fs")
  .readFileSync(process.platform === "linux" ? "/dev/stdin" : "../sample.txt")
  .toString()
  .trim()
  .split("\n");
const n = Number(input[0]);
const state = input[1].split(" ").map(Number);
let answer = 0n;
let sectionSize = 0;
for (let v of state) {
  if (v > 0) {
    // 쪽방
    let count = Math.floor(sectionSize / 2);
    if (sectionSize % 2 > 0) count++;
    answer += BigInt(v) + BigInt(count);
    sectionSize = 0;
  } else {
    // 구역
    sectionSize++;
  }
}
if (sectionSize > 0) {
  let count = Math.floor(sectionSize / 2);
  if (sectionSize % 2 > 0) count++;
  answer += BigInt(count);
}

console.log(answer.toString());
