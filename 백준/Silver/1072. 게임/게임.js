const input = require('fs').readFileSync(process.platform === "linux" ? "/dev/stdin" : "./sample.txt").toString().trim().split("\n");

const [x, y] = input[0].split(" ").map(Number);

if (x === y) { console.log(-1); }
else {
  const z = Math.floor(y * 100 / x);

  if (z === 99) { console.log(-1); }
  else {
    let ans = Math.ceil(((z + 1) * x - 100 * y) / (99 - z));

    console.log(ans);
  }
}