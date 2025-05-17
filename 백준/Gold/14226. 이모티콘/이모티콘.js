/**
 * 이모티콘
 * 클립보드도 방문처리??
 * 1024 * 1024
 */

const input = require("fs")
  .readFileSync(process.platform === "linux" ? "/dev/stdin" : "sample.txt")
  .toString()
  .trim()
  .split("\n");

const target = Number(input[0]);
const MAX = 1024;
const visited = [...Array(MAX + 1)].map(() => Array(MAX + 1).fill(false));
const queue = [[1, 0, 0]];
visited[1][0] = true;
while (queue.length > 0) {
  let [number, clipboard, time] = queue.shift();
  if (number === target) {
    console.log(time);
    break;
  }
  // 클립보드에 복사
  if (number < target && !visited[number][number]) {
    visited[number][number] = true;
    queue.push([number, number, time + 1]);
  }
  // 붙여넣기
  if (
    clipboard > 0 &&
    number + clipboard < MAX &&
    !visited[number + clipboard][clipboard]
  ) {
    visited[number + clipboard][clipboard] = true;
    queue.push([number + clipboard, clipboard, time + 1]);
  }
  // 하나 삭제
  if (number > 1 && !visited[number - 1][clipboard]) {
    visited[number - 1][clipboard] = true;
    queue.push([number - 1, clipboard, time + 1]);
  }
}

// 1, 1, 2, 2, 4, 6, 6, 12, 18
