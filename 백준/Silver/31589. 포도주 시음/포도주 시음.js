const input = require('fs').readFileSync(process.platform === "linux" ? "/dev/stdin" : "./sample.txt").toString().trim().split("\n");

let [n, k] = input[0].split(" ").map(Number);
const arr = input[1].split(" ").map(Number);
let leftIdx, rightIdx, ans;

arr.sort((a, b) => a - b);
leftIdx = 0;
rightIdx = n - 1;
ans = arr[rightIdx];
rightIdx -= 1;
k -= 1;

while (k >= 2 && leftIdx < rightIdx) {
  ans += arr[rightIdx] - arr[leftIdx];
  leftIdx += 1;
  rightIdx -= 1;
  k -= 2;
}

console.log(ans);