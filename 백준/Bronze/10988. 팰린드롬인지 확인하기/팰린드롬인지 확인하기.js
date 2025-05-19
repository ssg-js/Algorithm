const input = require("fs")
  .readFileSync(process.platform === "linux" ? "/dev/stdin" : "sample.txt")
  .toString()
  .trim()
  .split("\n");

const text = input[0].trim();
let answer = 1;
for (let i = 0; i < Math.floor(text.length / 2); i++) {
  if (text[i] !== text[text.length - 1 - i]) {
    answer = 0;
    break;
  }
}
console.log(answer);
