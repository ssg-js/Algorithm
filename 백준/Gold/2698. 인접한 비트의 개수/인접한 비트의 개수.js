const input = require('fs').readFileSync(process.platform === "linux" ? "/dev/stdin" : "./sample1.txt").toString().trim().split("\n");

const procedure = [...Array(101)].map(() => [...Array(101)].map(() => [0, 0]));
const results = [...Array(101)].map(() => [...Array(101)].map(() => 0));

for (let i = 1; i < 101; i++) {
  if (i === 1) { results[0][i] = 2; continue; }
  if (i === 2) { results[0][i] = 3; continue; }

  results[0][i] = results[0][i - 1] + results[0][i - 2];
}

for (let i = 1; i < 101; i++) {
  if (i === 1) {
    procedure[1][i][1] = 0;
    results[1][i] = procedure[1][i][0] + procedure[1][i][1];
    continue;
  }

  procedure[1][i][0] = results[1][i - 1];
  procedure[1][i][1] = (i - 3 >= 0 ? (results[0][i - 3] > 0 ? results[0][i - 3] : 1) : 1) + results[1][i - 2];
  results[1][i] = procedure[1][i][0] + procedure[1][i][1];
}

for (let i = 2; i < 101; i++) {
  for (let j = 1; j < 101; j++) {
    if (j <= i) { continue; }

    procedure[i][j][1] = procedure[i - 1][j - 1][1] + results[i][j - 2];
    procedure[i][j][0] = results[i][j - 1];
    results[i][j] = procedure[i][j][1] + procedure[i][j][0];
  }
}

for (let t = 0; t < Number(input[0]); t++) {
  const [n, k] = input[1 + t].split(' ').map(Number);

  console.log(results[k][n]);

}