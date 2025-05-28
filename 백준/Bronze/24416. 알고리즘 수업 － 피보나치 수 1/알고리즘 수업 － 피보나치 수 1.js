const input = require("fs")
  .readFileSync(process.platform === "linux" ? "/dev/stdin" : "sample.txt")
  .toString()
  .trim()
  .split("\n");

const n = Number(input[0]);
console.log(fib(n), fibonacci(n));

function fib(n) {
  if (n === 1 || n === 2) return 1;
  return fib(n - 1) + fib(n - 2);
}

function fibonacci(n) {
  if (n === 1 || n === 2) return 0;
  let ret = 0;
  for (let i = 3; i < n + 1; i++) {
    ret += 1;
  }
  return ret;
}
