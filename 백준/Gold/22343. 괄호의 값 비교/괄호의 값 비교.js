const input = require("fs")
  .readFileSync(process.platform === "linux" ? "/dev/stdin" : "../sample.txt")
  .toString()
  .trim()
  .split("\n");

const tc = Number(input[0]);
let answer = [];
for (let t = 0; t < tc; t++) {
  let a = input[1 + 2 * t];
  let b = input[1 + 2 * t + 1];

  let aResult = getValue(a);
  let bResult = getValue(b);

  if (aResult < bResult) answer.push("<");
  else if (aResult > bResult) answer.push(">");
  else answer.push("=");
}
console.log(answer.join("\n"));

function getValue(str) {
  const open = "(";
  const close = ")";

  let ret = 0;
  let stack = [];
  for (let s of str) {
    if (stack.length === 0 || s === open) {
      stack.push(s);
      continue;
    } else if (s === close) {
      let sum = 0;
      // 닫는 괄호에 대응하는 여는 괄호 찾기, 그전까지는 더할 수들만 있으므로 더하기
      let top = stack.pop();
      while (top !== open) {
        sum += Number(top);
        top = stack.pop();
      }
      // 닫을 때, 안에 값이 있다면 *2, 없다면 +1
      if (sum > 0) {
        sum *= 2;
      } else {
        sum = 1;
      }
      stack.push(sum);
    } else {
      console.log("?");
    }
  }

  // 더하는 애들이랑, 마지막 값은 남아있음
  while (stack.length > 0) {
    ret += Number(stack.pop());
  }

  return ret;
}
