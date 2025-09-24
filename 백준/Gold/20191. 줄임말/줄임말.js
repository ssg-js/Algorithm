/**
 * t의 모든 알파벳에 대해 위치를 저장해놓기 => 같은 문자가 여러번 등장할 수 있으므로 배열로 오름차순으로 저장(나중에 터질수도)
 * s의 각 알파벳을 순회하며 이전 알파벳이 t에 존재하는 위치보다 뒤에 위치에 존재하는지 체크
 * 1. 해당 알파벳이 존재하는 가장 마지막 위치가 이전 체크한 위치보다 작거나 같으면 한번 더 반복해야함.
 * 2. 크다면 그대로 체크
 */

const input = require("fs")
  .readFileSync(process.platform === "linux" ? "/dev/stdin" : "../sample.txt")
  .toString()
  .trim()
  .split("\n");

const s = input[0];
const t = input[1];

const poses = {};
for (let i = 0; i < t.length; i++) {
  let c = t[i];
  if (poses[c] === undefined) {
    poses[c] = [i];
  } else {
    poses[c].push(i);
  }
}

let answer = 1;
let checkingIdx = -1;
for (let c of s) {
  if (poses[c] === undefined) {
    answer = -1;
    break;
  }

  let failed = true;
  for (let idx of poses[c]) {
    if (idx > checkingIdx) {
      checkingIdx = idx;
      failed = false;
      break;
    }
  }
  if (failed) {
    answer++;
    checkingIdx = poses[c][0];
  }
}

console.log(answer);
