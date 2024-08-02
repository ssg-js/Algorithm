const input = require('fs').readFileSync(process.platform === "linux" ? "/dev/stdin" : "./sample.txt").toString().trim().split("\n");

const [n, T] = input[0].split(" ").map(Number);
const notMarked = [...Array(n + 1)].map(() => true);
const arr = [[0, 0]];

for (let i = 1; i < n + 1; i++) {
  let [x, y] = input[i].split(" ").map(Number);
  arr.push([x, y]);
}

arr.sort((a, b) => a[1] === b[1] ? a[0] - b[0] : a[1] - b[1]);

(() => {
  const queue = [0];
  let cnt = 0;
  notMarked[0] = false;

  while (queue.length > 0) {
    let l = queue.length;
    cnt += 1;
    for (let i = 0; i < l; i++) {
      const curIdx = queue.shift();
      const [x, y] = arr[curIdx];
      let preStop, postStop;

      for (let di = 1; di < n + 1; di++) {
        let preIdx = curIdx - di;
        let postIdx = curIdx + di;
        preStop = true;
        postStop = true;
        //forward
        if (preIdx >= 0 && Math.abs(y - arr[preIdx][1]) <= 2) {
          preStop = false;
          if (Math.abs(x - arr[preIdx][0]) <= 2) {
            if (arr[preIdx][1] === T) {
              console.log(cnt);
              return;
            }
            if (notMarked[preIdx]) {
              notMarked[preIdx] = false;
              queue.push(preIdx);
            }
          }
        }
        //backward
        if (postIdx < n + 1 && Math.abs(y - arr[postIdx][1]) <= 2) {
          postStop = false;
          if (Math.abs(x - arr[postIdx][0]) <= 2) {
            if (arr[postIdx][1] === T) {
              console.log(cnt);
              return;
            }
            if (notMarked[postIdx]) {
              notMarked[postIdx] = false;
              queue.push(postIdx);
            }
          }
        }

        if (preStop && postStop) { break; }

      }
    }
  }
  console.log(-1);
})();