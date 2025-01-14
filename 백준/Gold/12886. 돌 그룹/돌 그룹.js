const input = require('fs').readFileSync(process.platform === "linux" ? '/dev/stdin' : 'sample.txt').toString().trim().split('\n');

let [a, b, c] = input[0].split(' ').map(Number);

class Queue {
  constructor(v) {
    this.startNode = new Node(v);
    this.lastNode = this.startNode;
  }

  push(v) {
    this.lastNode.nextNode = new Node(v);
    if (this.startNode === null) {
      this.startNode = this.lastNode.nextNode;
    }
    this.lastNode = this.lastNode.nextNode;
  }

  pop() {
    let ret = this.startNode.value;
    this.startNode = this.startNode.nextNode;
    return ret;
  }
}

class Node {
  constructor(v) {
    this.value = v;
    this.nextNode = null;
  }
}

if ((a + b + c) % 3 !== 0) { console.log(0); }
else { solve(a, b, c); }

function solve(a, b, c) {
  const queue = new Queue([a, b, c]);
  if (isSame([a, b, c])) {
    console.log(1);
    return;
  }
  const visited = [...Array(1500)].map(() => [...Array(1500)].map(() => false));
  visited[a][b] = true;
  visited[b][a] = true;

  while (queue.startNode) {
    let arr = queue.pop();

    // 3C2 경우의 수로 둘의 크기가 같지 않는 두 그룹 고르고 X+X, Y-X 만들기
    for (let [i, j] of [[0, 1], [1, 2], [0, 2]]) {
      if (arr[i] === arr[j]) { continue; } // 같으면 패쓰
      let tmp = [...arr]; // 복사안하면 arr 변함
      if (tmp[i] > tmp[j]) {
        tmp[i] -= tmp[j];
        tmp[j] += tmp[j];
      } else if (tmp[i] < tmp[j]) {
        tmp[j] -= tmp[i];
        tmp[i] += tmp[i];
      }
      if (visited[tmp[i]][tmp[j]] || visited[tmp[j]][tmp[i]]) { continue; }
      visited[tmp[i]][tmp[j]] = true;
      visited[tmp[j]][tmp[i]] = true;
      if (isSame(tmp)) { // 같으면 끝
        console.log(1);
        return;
      }
      queue.push(tmp);
    }

  }

  console.log(0);
  return;
}

function isSame(arr) {
  for (let i = 1; i < arr.length; i++) {
    if (arr[i - 1] !== arr[i]) {
      return false;
    }
  }
  return true;
}
