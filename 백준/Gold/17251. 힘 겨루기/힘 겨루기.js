const input = require('fs').readFileSync(process.platform === "linux" ? "/dev/stdin" : "./sample.txt").toString().trim().split("\n");

const n = Number(input[0].split(' '));
const arr = input[1].split(' ').map(Number);

const leftMax = [...Array(n)].map((v) => 0);
let redWins = 0;

const rightMax = [...Array(n)].map((v) => 0);
let blueWins = 0;

leftMax[0] = arr[0];
rightMax[n - 1] = arr[n - 1];

for (let i = 1; i < n; i++) {
  leftMax[i] = Math.max(leftMax[i - 1], arr[i]);
  rightMax[n - 1 - i] = Math.max(rightMax[n - i], arr[n - 1 - i]);
}

for (let i = 0; i < n - 1; i++) {
  if (leftMax[i] > rightMax[i + 1]) { redWins += 1; }
  if (leftMax[i] < rightMax[i + 1]) { blueWins += 1; }
}

if (redWins > blueWins) { console.log('R'); }
else if (redWins < blueWins) { console.log('B'); }
else { console.log('X'); }