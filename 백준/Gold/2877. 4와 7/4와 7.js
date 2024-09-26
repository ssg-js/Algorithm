const input = require('fs').readFileSync(process.platform === "linux" ? "/dev/stdin" : "./sample1.txt").toString().trim().split("\n");
// https://www.acmicpc.net/problem/2877

const k = input[0];

solve(k);

function findDigits(k) {
  let n = 1;
  while (n < 30) {
    if (k < 2 ** (n + 1) - 1) { break; }
    n++;
  }
  return n;
}

function getFavoriteNum(k, n) {
  let ans = "";
  for (let i = 1; i < n + 1; i++) {
    if ((k - (2 ** i - 1)) % 2 ** i < 2 ** (i - 1)) { ans = "4" + ans; }
    else { ans = "7" + ans; }
  }
  return ans;
}

function solve(k) {
  console.log(getFavoriteNum(k, findDigits(k)));
}