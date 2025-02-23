const input = require('fs').readFileSync(process.platform === "linux" ? '/dev/stdin' : 'sample.txt').toString().trim().split('\n');

const n = Number(input[0]);
let s = '';
for (let i = 0; i < n; i++) {
  s = s + input[1 + i].trim();
}


let [l, r] = [0, s.length - 1];
let str = '';
while (l <= r) {
  let [ln, rn] = [s[l].charCodeAt(), s[r].charCodeAt()];
  if (ln === rn) {
    let [tempL, tempR] = [l, r];
    while (tempL <= tempR && s[tempL] === s[tempR]) {
      tempL++;
      tempR--;
    }
    // 더 빠른 쪽으로 이동
    if (s[tempL].charCodeAt() < s[tempR].charCodeAt()) {
      str += s[l];
      l++;
    } else {
      str += s[r];
      r--;
    }

  } else if (ln < rn) {
    str += s[l];
    l++;
  } else {
    str += s[r];
    r--;
  }
}


const answer = [];
for (let i = 0; i < Math.floor(n / 80); i++) {
  answer.push(str.slice(i * 80, (i + 1) * 80));
}
answer.push(str.slice(Math.floor(n / 80) * 80, n));

console.log(answer.join("\n"));
