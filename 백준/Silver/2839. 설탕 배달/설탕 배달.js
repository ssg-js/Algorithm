const input = require("fs")
  .readFileSync(process.platform === "linux" ? "/dev/stdin" : "sample.txt")
  .toString()
  .trim()
  .split("\n");

const n = Number(input[0]);
let answer = -1;
for (let five = Math.floor(n / 5); five > -1; five--) {
  let rest = n - 5 * five;
  if (rest % 3 !== 0) continue;
  answer = five + rest / 3;
  break;
}
console.log(answer);
