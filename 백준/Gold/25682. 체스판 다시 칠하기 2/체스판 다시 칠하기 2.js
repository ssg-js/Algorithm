const input = require('fs').readFileSync(process.platform === "linux" ? "/dev/stdin" : "./sample1.txt").toString().trim().split("\n");

const [n, m, k] = input[0].split(" ").map(Number);
const board = [];
for (let i = 0; i < n; i++) {
  board.push(input[1 + i].trim());
}

const states = [...Array(n)].map(() => [...Array(m)].map(() => 0));
for (let i = 0; i < m; i++) {
  if (i === 0) {
    if (board[i][i] !== 'B') {
      states[i][i] = 1;
    }
    continue;
  }

  states[0][i] = states[0][i - 1];
  if (i % 2 === 0) {
    if (board[0][i] !== 'B') {
      states[0][i] += 1;
    }
  } else {
    if (board[0][i] !== 'W') {
      states[0][i] += 1;
    }
  }
}
for (let i = 1; i < n; i++) {
  states[i][0] = states[i - 1][0];
  if (i % 2 === 0) {
    if (board[i][0] !== 'B') {
      states[i][0] += 1;
    }
  } else {
    if (board[i][0] !== 'W') {
      states[i][0] += 1;
    }
  }
}

for (let i = 1; i < n; i++) {
  for (let j = 1; j < m; j++) {
    states[i][j] = states[i - 1][j] + states[i][j - 1] - states[i - 1][j - 1];

    if (i % 2 === 0) {
      if (j % 2 === 0) {
        if (board[i][j] !== 'B') {
          states[i][j] += 1;
        }
      } else {
        if (board[i][j] !== 'W') {
          states[i][j] += 1;
        }
      }
    } else {
      if (j % 2 === 0) {
        if (board[i][j] !== 'W') {
          states[i][j] += 1;
        }
      } else {
        if (board[i][j] !== 'B') {
          states[i][j] += 1;
        }
      }
    }
  }
}

let answer = 4000000;
let cnt;
for (let i = 0; i < n - k + 1; i++) {
  for (let j = 0; j < m - k + 1; j++) {
    cnt = states[i + k - 1][j + k - 1];

    if (j > 0) { cnt -= states[i + k - 1][j - 1]; }
    if (i > 0) { cnt -= states[i - 1][j + k - 1]; }
    if (i > 0 && j > 0) { cnt += states[i - 1][j - 1]; }

    answer = Math.min(answer, cnt, k * k - cnt);
  }
}

console.log(answer)