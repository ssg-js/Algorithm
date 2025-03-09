const input = require("fs")
  .readFileSync(process.platform === "linux" ? "/dev/stdin" : "sample.txt")
  .toString()
  .trim()
  .split("\n");

const n = Number(input[0]);
const arr = input[1].split(" ").map(Number);
let answer = Infinity;
let [left, right] = [0, n - 1];
while (left < right) {
  let result = arr[left] + arr[right];
  if (Math.abs(result) < Math.abs(answer)) { answer = result; }
  if (result === 0) { break; }
  else if (result > 0) { right -= 1; }
  else { left += 1; }
}
console.log(answer);