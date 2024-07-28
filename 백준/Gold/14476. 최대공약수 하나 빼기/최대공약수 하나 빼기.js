const input = require('fs').readFileSync(process.platform === "linux" ? "/dev/stdin" : "./sample.txt").toString().trim().split("\n");

const n = Number(input[0]);
const arr = input[1].split(" ").map(Number);
const leftArr = [...Array(n)].map(() => 0);
const rightArr = [...Array(n)].map(() => 0);

function euclideanAlgorithm(x, y) {
  let a = (x >= y) ? x : y;
  let b = (x >= y) ? y : x;
  let ret = a % b;

  a = b;
  b = ret
  while (b !== 0) {
    ret = a % b;
    a = b;
    b = ret;
  }

  return a;
}

leftArr[0] = arr[0];
rightArr[n - 1] = arr[n - 1];

for (let i = 1; i < n; i++) {
  leftArr[i] = euclideanAlgorithm(leftArr[i - 1], arr[i]);
  rightArr[n - 1 - i] = euclideanAlgorithm(rightArr[n - i], arr[n - 1 - i]);
}

(() => {
  let maxGcv = 0;
  let num = 0;

  arr.forEach((v, i) => {
    let gcv = 0;
    if (i == 0) { gcv = rightArr[i + 1]; }
    else if (i == n - 1) { gcv = leftArr[i - 1]; }
    else { gcv = euclideanAlgorithm(leftArr[i - 1], rightArr[i + 1]); }

    if (v % gcv === 0) { return }
    if (gcv > maxGcv) {
      maxGcv = gcv;
      num = v;
    }
  })

  if (maxGcv === 0) { console.log(-1); }
  else { console.log(maxGcv, num); }
})();