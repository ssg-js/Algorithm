const input = require('fs').readFileSync(process.platform === "linux" ? "/dev/stdin" : "./sample.txt").toString().trim().split("\n");

const str = input[0];
const q = Number(input[1]);
const board = [...Array(26)].map(() => [...Array(str.length)].map(() => 0));
const norm = 'a'.charCodeAt();

for (let i = 0; i < 26; i++) {
  let char = String.fromCharCode(norm + i);
  if (str[0] === char) { board[i][0] = 1; }
  for (let j = 1; j < str.length; j++) {
    if (str[j] === char) { board[i][j] = board[i][j - 1] + 1; }
    else { board[i][j] = board[i][j - 1]; }
  }
}

for (let i = 2; i < 2 + q; i++) {
  let [char, s, e] = input[i].split(" ");
  s = Number(s);
  e = Number(e);
  if (s === 0) { console.log(board[char.charCodeAt() - norm][e]); }
  else { console.log(board[char.charCodeAt() - norm][e] - board[char.charCodeAt() - norm][s - 1]); }
}
