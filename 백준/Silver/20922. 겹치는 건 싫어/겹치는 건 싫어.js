const input = require('fs').readFileSync(process.platform === "linux" ? "/dev/stdin" : "./sample.txt").toString().trim().split("\n");

const [n, m] = input[0].split(" ").map(Number);
const seq = input[1].split(" ").map(Number);

const store = new Map();
let ans = 1;
let [l, r] = [0, 1];
store.set(seq[l], 1);

while (l <= r) {
  if (r === n) {
    ans = Math.max(ans, r - l);
    break;
  } else {
    let cnt = 1;
    if (store.has(seq[r])) {
      cnt = store.get(seq[r]) + 1;
    }

    if (cnt > m) {
      ans = Math.max(ans, r - l);
      while (store.get(seq[r]) === m) {
        let tmp = store.get(seq[l]);
        store.set(seq[l], tmp - 1);
        l += 1;
      }
      store.set(seq[r], cnt - 1);
      r += 1;
    } else {
      store.set(seq[r], cnt);
      r += 1;
    }
  }
}
console.log(ans);