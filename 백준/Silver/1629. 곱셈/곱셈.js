const input = require('fs').readFileSync(process.platform === "linux" ? "/dev/stdin" : "./sample.txt").toString().trim().split("\n");

const [a, b, c] = input[0].split(" ").map(BigInt);

const mul = function (a, b, c) {
  if (b === 1n) { return a % c; }
  let ret = (b % 2n === 0n) ? mul(a, BigInt(b / 2n), c) : mul(a, BigInt((b - 1n) / 2n), c);
  ret = ret * ret % c;
  if (b % 2n === 0n) { return ret; }
  return ret * a % c;
}

console.log(mul(a, b, c).toString());