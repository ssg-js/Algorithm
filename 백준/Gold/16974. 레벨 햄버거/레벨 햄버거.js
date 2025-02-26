const input = require("fs")
  .readFileSync(process.platform === "linux" ? "/dev/stdin" : "sample.txt")
  .toString()
  .trim()
  .split("\n");

const [n, x] = input[0].split(" ").map(Number);
solve(n, x);


function solve(n, x) {
  const burgers = Array(n + 1).fill(0); // 각 레이어별 패티 개수
  let size = 1n; // 버거 크기
  burgers[0] = 1n;
  for (let i = 1; i < n + 1; i++) {
    burgers[i] = 1n + 2n * burgers[i - 1];
    size = 3n + 2n * size;
  }
  let [l, r] = [1n, BigInt(size)];
  let answer = 0n;
  // r에서부터 x개를 체크하면서 분할 탐색
  x = BigInt(x);
  while (l <= r) {
    let xPos = r - x + 1n; // r에서 x개 먹을 때 위치
    // l, r 사이를 벗어났을때
    if (xPos < l) {
      answer += burgers[n];
      break;
    }
    if (xPos > r) {
      break;
    }
    let mid = (l + r) / 2n;
    if (xPos === mid) {
      // 중간
      answer += 1n + (n > 0 ? burgers[n - 1] : 0n);
      break;
    } else if (xPos < mid) {
      // 중간의 왼쪽
      answer += 1n + burgers[n - 1];
      x -= r - mid + 1n
      r = mid - 1n;
      l++;
      n--;
    } else {
      // 중간의 오른쪽a
      x--;
      r--;
      l = mid + 1n;
      n--;
    }
  }
  console.log(String(answer));

}
