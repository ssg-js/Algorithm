const input = require('fs').readFileSync(process.platform === "linux" ? "/dev/stdin" : "./sample.txt").toString().trim().split("\n");
// https://www.acmicpc.net/problem/18808 
const [n, m, k] = input[0].split(" ").map(Number);
const stickers = [];
const board = [...Array(n)].map(() => [...Array(m)].map(() => 0));

let idx = 1;
for (let i = 0; i < k; i++) {
  let [r, c] = input[idx].split(" ").map(Number);
  let sticker = [];
  for (let j = 0; j < r; j++) {
    sticker.push(input[idx + 1 + j].split(" ").map(Number));
  }
  idx += r + 1;
  stickers.push(sticker);
}

for (let sticker of stickers) {
  tryAttach(board, sticker);
}

countAttached(board);


function tryAttach(board, sticker) {
  for (let turn = 0; turn < 4; turn++) {
    for (let x = 0; x < board.length; x++) {
      for (let y = 0; y < board[0].length; y++) {
        if (tryFill(board, sticker, x, y)) {
          confirmAttach(board, sticker, x, y);
          return true;
        }
      }
    }
    sticker = rotateSticker(sticker);
  }
  return false;
}

function tryFill(board, sticker, x, y) {
  // board 채워보다가 안되면 리턴
  const [h, w] = [sticker.length, sticker[0].length];
  for (let i = 0; i < h; i++) {
    for (let j = 0; j < w; j++) {
      if (sticker[i][j] === 1) {
        if (x + i >= board.length || y + j >= board[0].length || board[x + i][y + j] === 1) {
          return false;
        }
      }
    }
  }
  return true;
}

function confirmAttach(board, sticker, x, y) {
  const [h, w] = [sticker.length, sticker[0].length];
  for (let i = 0; i < h; i++) {
    for (let j = 0; j < w; j++) {
      if (sticker[i][j] === 1) {
        board[x + i][y + j] = 1;
      }
    }
  }
}

function rotateSticker(sticker) {
  let new_sticker = [];
  const [h, w] = [sticker.length, sticker[0].length];
  for (let j = 0; j < w; j++) {
    let new_push = [];
    for (let i = h - 1; i >= 0; i--) {
      new_push.push(sticker[i][j]);
    }
    new_sticker.push(new_push);
  }
  return new_sticker;
}

function countAttached(board) {
  let cnt = 0;
  for (line of board) {
    for (point of line) {
      if (point === 1) { cnt++; }
    }
  }
  console.log(cnt);
}