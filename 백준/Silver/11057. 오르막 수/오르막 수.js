const input = Number(require('fs').readFileSync("/dev/stdin").toString().trim());

const arr = [...Array(10)].map((_, i) => i + 1);
arr[0] = 1;
for (let t = 1; t < input; t++) {
  for (let i = 1; i < 10; i++) {
    arr[i] = (arr[i - 1] + arr[i]) % 10007;
  }
}
console.log(arr[9] % 10007);