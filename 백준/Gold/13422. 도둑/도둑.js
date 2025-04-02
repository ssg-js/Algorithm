const input = require("fs")
  .readFileSync(process.platform === "linux" ? "/dev/stdin" : "sample.txt")
  .toString()
  .trim()
  .split("\n");

const tc = Number(input[0]);
let answer = ``;
for (let t = 0; t < tc; t++) {
  let [n, m, k] = input[1 + t * 2].split(" ").map(Number);
  const arr = input[1 + t * 2 + 1].split(" ").map(Number);
  let count = 0;
  for (let i = 1; i < n; i++) {
    arr[i] += arr[i - 1];
  }
  if (n === m) {
    if (arr[n - 1] < k) count++;
  } else {
    for (let i = 0; i < n; i++) {
      if (i < m) {
        let v = arr[i] + arr[n - 1] - arr[i + n - m];
        if (v < k) count++;
        continue;
      }
      let v = arr[i] - arr[i - m];
      if (v < k) count++;
    }
  }
  answer += `${count}\n`;
}
console.log(answer);
