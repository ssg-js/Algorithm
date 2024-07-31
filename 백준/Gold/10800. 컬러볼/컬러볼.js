const input = require('fs').readFileSync(process.platform === "linux" ? "/dev/stdin" : "./sample.txt").toString().trim().split("\n");

n = Number(input[0]);
const arr = [];
const ans = [...Array(n)].map(() => 0);
const cntOfColor = [...Array(n + 1)].map(() => 0);
const cntOfSize = [...Array(2001)].map(() => 0);
let sum = 0;

for (let i = 1; i < n + 1; i++) {
  const [color, size] = input[i].split(" ").map(Number);
  arr.push({
    color: color,
    size: size,
    index: i - 1,
  });
}

arr.sort((a, b) => {
  if (a.size === b.size) { return a.color - b.color; }
  return a.size - b.size;
});

for (let i = 0; i < n; i++) {
  const { color, size, index } = arr[i];

  if (i !== 0 && arr[i - 1].color === color && arr[i - 1].size === size) { ans[index] = ans[arr[i - 1].index]; }
  else { ans[index] = sum - cntOfColor[color] - cntOfSize[size]; }

  cntOfColor[color] += size;
  cntOfSize[size] += size;
  sum += size;

}

console.log(ans.join("\n"));