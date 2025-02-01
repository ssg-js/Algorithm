
// 중간(n//2, n//2)에서 왼쪽으로 나선형으로 큐에 넣기
function enqueue(board, queue) {
  let delta = [[0, -1], [1, 0], [0, 1], [-1, 0]];
  let n = board.length;

  let [x, y] = [Math.floor(n / 2), Math.floor(n / 2)];
  let k = 0;
  // 변의 길이가 1(왼), 1(아래), 2(오), 2(위), 3(왼), 3(아래), 4(오), 4(위), ...
  // => 크기는 2의 배수(k//2+1), 방향은 4의 배수(k % 4)
  // 
  loop1: while (true) {
    let [width, dir] = [Math.floor(k / 2) + 1, Math.floor(k % 4)];
    let [dx, dy] = delta[dir];
    for (let w = 0; w < width; w++) { // 크기만큼 방향으로 이동해서 queue에 추가
      [x, y] = [x + dx, y + dy];
      if (x < 0 || y < 0 || x >= n || y >= n) { break loop1; } // board 넘기면 그만
      if (board[x][y] === 0) { break loop1; } // 빈 공간이면 그만, 처음에 중간 왼쪽부터 시작해서 괜찮음
      queue.push(board[x][y]); // 추가
    }
    k += 1;
  }
}

// blizzard 시전
// 인덱스 규칙
// 3 왼: 0(+0), 9(+3), ... => k번째 위치 : (2 * 3 + 3) + (4 * 3 + 5) + .. + 6(k-1) + 2k-1 => 4(k)(k+1) -7k - 1
// 2 밑: 2(+2), 13(+4), ... => k번째 위치 : 4(k)(k+1) -7k - 1 + k * 2
// 4 오: 4(+2), 17(+4), ... => k번재 위치 : 4(k)(k+1) -7k - 1 + k * 2 * 2 
// 1 위: 6(+2), 21(+4), ... => k번재 위치 : 4(k)(k+1) -7k - 1 + k * 2 * 3
function magic(queue, dir, dis) {
  // 식에 넣을 방향으로 다시 처리
  switch (dir) {
    case 3:
      dir = 0;
      break;
    case 2:
      dir = 1;
      break;
    case 4:
      dir = 2;
      break;
    case 1:
      dir = 3;
      break;
  }
  // 위의 식대로 거리별 위치의 구슬 0처리
  let i;
  for (let k = 1; k < dis + 1; k++) {
    i = 4 * k * (k + 1) - 7 * k - 1 + dir * 2 * k;
    if (i >= queue.length) { break; }
    queue[i] = 0;
  }
}

const input = require('fs').readFileSync(process.platform === "linux" ? '/dev/stdin' : 'sample.txt').toString().trim().split('\n');

const [n, m] = input[0].split(" ").map(Number);
const board = [];
for (let i = 0; i < n; i++) {
  board.push(input[1 + i].split(" ").map(Number));
}
const blizzard = [];
for (let i = 0; i < m; i++) {
  blizzard.push(input[1 + n + i].split(" ").map(Number));
}
let queue = [];
const status = [0, 0, 0, 0];

enqueue(board, queue);
for (let [dir, dis] of blizzard) {
  magic(queue, dir, dis); // 마법 사용
  // 0 제거
  let size = queue.length;
  let pearl;
  for (let i = 0; i < size; i++) {
    pearl = queue.shift();
    if (pearl === 0) { continue; }
    queue.push(pearl);
  }

  // 4개 이상 연속된 구슬이 없을 때까지 폭파
  let done; // 연속된 구슬 없는지 검사
  let cnt; // 지금 같은 구슬이 반복된 횟수
  let groupNum; // 지금 세고있는 구슬 번호 => 달라질 때 이전 구슬 cnt가 4이상이면 pop해서 제거

  while (true) {
    done = true;
    cnt = 0;
    groupNum = 0;
    size = queue.length; // 중간에 queue 길이가 변경되므로 변수로 받아서 돌려야함 
    for (let i = 0; i < size; i++) {
      pearl = queue.shift();
      if (pearl !== groupNum) {
        // 이전 구슬 그룹 폭파 여부 조사
        if (cnt >= 4) {
          done = false;
          status[groupNum] += cnt;
          for (let c = 0; c < cnt; c++) {
            queue.pop();
          }
        }
        // 새 구슬 그룹 갱신
        cnt = 1;
        groupNum = pearl;
      } else {
        cnt += 1;
      }
      queue.push(pearl);
    }
    // 마지막에 딱 걸치는 그룹이 길이가 4이상인 경우 처리해줘야함
    if (cnt >= 4) {
      done = false;
      status[groupNum] += cnt;
      for (let c = 0; c < cnt; c++) {
        queue.pop();
      }
    }
    if (done) { break; }
  }
  if (queue.length === 0) { break; } // 남은 구슬이 없는 경우 종료 => 안하면 밑에 temp에서 이상한 값 가져옴
  // 구슬 변신
  let temp = [];
  let maxLength = n * n - 1; // queue의 최대 길이
  cnt = 0;
  groupNum = queue[0]; // 초기값이 다르면 밑에 조건문에서 존재하지 않는 경우로 빠짐
  for (let pearl of queue) {
    if (groupNum !== pearl) { // 다르면 이전 그룹 정보로 구슬 변신 정보 저장
      if (temp.length === maxLength) { break; }
      temp.push(cnt);
      if (temp.length === maxLength) { break; }
      temp.push(groupNum);
      groupNum = pearl;
      cnt = 1;
    } else {
      cnt += 1;
    }
  }
  // 마지막 그룹 처리
  if (temp.length < maxLength) { temp.push(cnt); }
  if (temp.length < maxLength) { temp.push(groupNum); }
  queue = temp;
}

let answer = 0;
for (let i = 1; i < status.length; i++) {
  answer += i * status[i];
}
console.log(answer);
