const input = require('fs').readFileSync(process.platform === "linux" ? "/dev/stdin" : "./sample1.txt").toString().trim().split("\n");

const str = input[0];
const arr = str.split(":");
const zeroCnt = 9 - arr.length;
const answer = [];
for (let i = 0; i < arr.length; i++) {
  s = arr[i]
  if (i > 0 && i < arr.length - 1 && s.length === 0) {
    for (let k = 0; k < zeroCnt; k++) {
      answer.push("0000");
    }
    continue;
  }
  answer.push(fill(s));
}

console.log(answer.join(":"))

function fill(s) {
  let k = 4 - s.length;
  let ret = ""
  for (let i = 0; i < k; i++) {
    ret += "0";
  }
  return ret + s;
}