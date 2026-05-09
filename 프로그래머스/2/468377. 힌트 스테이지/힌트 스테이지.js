
function solution(cost, hint) {
  var answer = Infinity;
  const n = cost.length;
  const k = hint[0].length - 1;

  const stack = [[0, 0, 0]]; // [stage, bought bundles, cost]

  while (stack.length > 0) {
    let [stage, bundles, totalCost] = stack.pop();

    // 번들에서 현재 스테이지 힌트를 몇번 쓸 수 있는지 추출
    let count = 0;
    for (let i = 0; i < n - 1; i++) {
      if ((bundles & (1 << i)) === 0) continue;

      hint[i].forEach((v, i) => {
        if (i === 0) return; // 구매비용은 패쓰
        if (v - 1 === stage) count++;
      });
    }
    count = Math.min(count, n - 1);

    let total = totalCost + cost[stage][count];
    // 마지막 스테이지면 answer 와 비교
    if (stage === n - 1) {
      if (total < answer) answer = total;
      continue;
    }

    // 현재 스테이지에서 번들을 구매하는 경우와 아닌 경우를 스택에 저장
    stack.push([stage + 1, bundles | (1 << stage), total + hint[stage][0]]);
    stack.push([stage + 1, bundles, total]);
  }

  return answer;
}
