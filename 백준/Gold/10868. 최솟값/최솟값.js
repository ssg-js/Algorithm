/**
 * 최솟값
 */

const MAX = 1000000000;
const input = require("fs")
  .readFileSync(process.platform === "linux" ? "/dev/stdin" : "sample.txt")
  .toString()
  .trim()
  .split("\n");

const [n, m] = input[0].split(" ").map(Number);
const arr = [];
for (let i = 1; i < n + 1; i++) {
  arr.push(Number(input[i]));
}
let binaryExponent = 0; // to get tree size
while (1 << binaryExponent < n) {
  binaryExponent++;
}
const segmentTree = Array(1 << (binaryExponent + 1)).fill(MAX);
initTree(0, n - 1, 0);
let answer = "";
for (let i = n + 1; i < n + m + 1; i++) {
  const [a, b] = input[i].split(" ").map((v) => Number(v) - 1);
  answer += searchTree(0, n - 1, 0, a, b) + "\n";
}
console.log(answer);

function initTree(start, end, node) {
  if (start === end) {
    segmentTree[node] = arr[start];
    return segmentTree[node];
  }

  const mid = Math.floor((start + end) / 2);
  segmentTree[node] = Math.min(
    initTree(start, mid, node * 2 + 1),
    initTree(mid + 1, end, node * 2 + 2)
  );
  return segmentTree[node];
}

// left, right가 찾는 범위
function searchTree(start, end, node, left, right) {
  if (end < left || right < start) {
    return MAX;
  }
  if (left <= start && end <= right) {
    return segmentTree[node];
  }

  const mid = Math.floor((start + end) / 2);
  return Math.min(
    searchTree(start, mid, node * 2 + 1, left, right),
    searchTree(mid + 1, end, node * 2 + 2, left, right)
  );
}
