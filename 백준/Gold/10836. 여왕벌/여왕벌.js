const input = require("fs")
  .readFileSync(
    process.platform === "linux" ? "/dev/stdin" : "../../sample.txt"
  )
  .toString()
  .trim()
  .split("\n");

const [m, n] = input[0].split(" ").map(Number);
const arr = Array(m * 2 - 1).fill(1);
for (let i = 0; i < n; i++) {
  let [zero, one, two] = input[1 + i].split(" ").map(Number);
  for (let k = zero; k < zero + one; k++) arr[k] += 1;
  for (let k = zero + one; k < zero + one + two; k++) arr[k] += 2;
}

let answer = ``;
let repeat = ``;
for (let i = m; i < arr.length; i++) {
  repeat += ` ${arr[i]}`;
}
repeat += `\n`;
for (let i = m - 1; i >= 0; i--) {
  answer += `${arr[i]}` + repeat;
}

console.log(answer);
