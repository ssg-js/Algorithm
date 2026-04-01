const input = require("fs")
  .readFileSync(process.platform === "linux" ? "/dev/stdin" : "../sample.txt")
  .toString()
  .trim()
  .split("\n");

let A = input[0].trim();
let B = input[1].trim();

// A가 더 작은거
if (A.length > B.length) {
  [A, B] = [B, A];
}
const N = A.length;
const M = B.length;

let answer = 0;
for (let k = 1; k < N + 1; k++) {
  if (checkPossible(k)) answer = k;
}
console.log(answer);

// 파라미터로 들어온 길이의 구간 중에 알파벳 성분이 같은 구간이 있는지 체크
function checkPossible(k) {
  const elementsOfA = Array(26).fill(0);

  for (let i = 0; i < N - k + 1; i++) {
    // A 신호에서 i부터 k길이의 구간 성분 가져오기
    if (i === 0) {
      // 구간 처음 뽑을 때
      for (let j = i; j < k; j++) {
        elementsOfA[aToN(A, j)]++;
      }
    } else {
      // 첫번째 구간 아니면 성분 배열 업데이트
      elementsOfA[aToN(A, i - 1)]--;
      elementsOfA[aToN(A, i + k - 1)]++;
    }
    const elementsOfB = Array(26).fill(0);

    for (let j = 0; j < M - k + 1; j++) {
      // B에서 k길이의 구간 뽑기
      if (j === 0) {
        // 구간 처음 뽑을 때
        for (let l = j; l < k; l++) {
          elementsOfB[aToN(B, l)]++;
        }
      } else {
        // 첫번째 구간 아니면 성분 배열 업데이트
        elementsOfB[aToN(B, j - 1)]--;
        elementsOfB[aToN(B, j + k - 1)]++;
      }

      // A, B 구간 비교
      if (compare(elementsOfA, elementsOfB)) return true;
    }
  }

  return false;
}

function aToN(str, i) {
  return str.charCodeAt(i) - "a".charCodeAt();
}

function compare(arr1, arr2) {
  let size = 26;
  for (let i = 0; i < size; i++) {
    if (arr1[i] !== arr2[i]) return false;
  }
  return true;
}
