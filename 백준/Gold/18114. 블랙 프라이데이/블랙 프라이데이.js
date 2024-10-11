const input = require('fs').readFileSync(process.platform === "linux" ? "/dev/stdin" : "./sample.txt").toString().trim().split("\n");

const [n, c] = input[0].split(" ").map(Number);
const stuff = input[1].split(" ").map(Number);
const visited = new Map();
stuff.sort((a, b) => a - b);

let ans = 0;
for (let weight of stuff) {
  if (c === weight || visited.has(c - weight)) {
    ans = 1;
    break;
  }
  for (let subWeight of stuff) {
    if (subWeight >= weight) { break; }
    if (c - weight - subWeight === weight || c - weight - subWeight === subWeight) { break; }
    if (visited.has(c - weight - subWeight)) {
      ans = 1;
      break;
    }
  }
  if (ans === 1) { break; }

  visited.set(weight, true);
}

console.log(ans);