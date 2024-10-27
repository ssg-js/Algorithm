const input = require('fs').readFileSync(process.platform === "linux" ? "/dev/stdin" : "./sample.txt").toString().trim().split("\n");

const t = Number(input[0]);
let ans = ``;
for (let i = 1; i < 1 + t; i++) {
  let [s, t] = input[i].split(" ").map(Number);
  const board = [...Array(124)].map(() => []); // 도착지점을 저장해 해당 도착지점이 맞는 case마다 visited 처리
  board[s].push(t);
  const queue = [[s, t, 0]];
  let queueIdx = 0;
  let cnt, cur, target;

  while (queueIdx < queue.length) {
    [cur, target, cnt] = queue[queueIdx];
    queueIdx += 1;

    // A
    if (cur * 2 === target + 3) {
      ans += `${cnt + 1}\n`
      break;
    }
    if (cur * 2 < target + 3) {
      if (cur * 2 < board.length && !(target + 3 in board[cur * 2])) {
        board[cur * 2].push(target + 3);
        queue.push([cur * 2, target + 3, cnt + 1]);
      }
    }
    // B
    if (cur + 1 === target) {
      ans += `${cnt + 1}\n`
      break;
    }
    if (cur + 1 < board.length && !(target in board[cur + 1])) {
      board[cur + 1].push(target);
      queue.push([cur + 1, target, cnt + 1]);
    }
  }
}
console.log(ans);