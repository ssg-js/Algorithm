const input = require("fs")
  .readFileSync(process.platform === "linux" ? "/dev/stdin" : "sample.txt")
  .toString()
  .trim()
  .split("\n");

const n = Number(input[0]);
const chars = {};
for (let i = 0; i < n; i++) {
  let str = input[1 + i].trim();
  for (let j = 0; j < str.length; j++) {
    let c = str[j];
    if (chars[c] !== undefined) {
      chars[c] += Math.pow(10, (str.length - j - 1));
    } else {
      chars[c] = Math.pow(10, (str.length - j - 1));
    }
  }
}

// 최댓값 만들기 => 알파벳 노상관
const values = [];
for (let v of Object.values(chars)) {
  values.push(v);
}
values.sort((a, b) => b - a);

let answer = 0;
for (let i = 0; i < values.length; i++) {
  answer += (9 - i) * values[i];
}
console.log(answer);

