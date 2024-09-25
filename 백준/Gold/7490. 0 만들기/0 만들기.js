const input = require('fs').readFileSync(process.platform === "linux" ? "/dev/stdin" : "./sample.txt").toString().trim().split("\n");
// https://www.acmicpc.net/problem/7490

/**
 * dfs로 ["+", "-", " "] 하나씩 들어감. 그리고 수식은 문자열로 모아서 n에 도달하면 계산 후 출력할 지 말지 판단
 */
const t = input[0];
for (let i = 0; i < t; i++) {
  const n = Number(input[1 + i]);

  zeroMaker(n);
  console.log();
}

/**
 * 
 * @param {number} n 
 * @param {string} formula 
 * @param {number} cur 
 * @param {Array} arr 
 */
function zeroMaker(n, formula = '1', cur = 1, arr = [" ", "+", "-"]) {

  if (cur === n) { // 
    const v = calculate(formula);
    if (v === 0) { console.log(formula); }
    return;
  }

  for (let i of arr) {
    zeroMaker(n, formula + i + String(cur + 1), cur + 1);
  }
}

function calculate(s) {
  let ret = 0;
  let value = 0;
  s = s.replaceAll(' ', '');

  for (let i = s.length - 1; i > -1; i--) {
    if (s[i] === "+") { ret += value; }
    else if (s[i] === "-") { ret -= value; }
    else {
      let idx = i;
      while (idx > -1) {
        if (isNaN(s[idx])) { break; }
        if (idx === i) { value = Number(s[idx]); }
        else { value = value + (10 ** (i - idx)) * Number(s[idx]); }
        idx--;
      }
      i = idx + 1;
    }
  }
  return ret + value;
}