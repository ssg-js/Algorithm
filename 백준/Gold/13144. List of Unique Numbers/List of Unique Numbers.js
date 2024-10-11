const input = require('fs').readFileSync(process.platform === "linux" ? "/dev/stdin" : "./sample.txt").toString().trim().split("\n");

const n = Number(input[0]);
const seq = input[1].split(" ").map(Number);

let [left, right] = [0, 0];
const visited = new Map();

let ans = 0;
while (left <= right) {
  if (left === right) {
    visited.set(seq[left], true);
    right += 1;
  }
  if (right === n) {
    ans += (right - left) * (right - left + 1) / 2;
    break;
  } else if (visited.has(seq[right])) {
    ans += right - left;
    visited.delete(seq[left]);
    left += 1;
  } else {
    visited.set(seq[right], true);
    right += 1;
  }
}
console.log(ans);
