function solution(sequence) {
  var answer = -Infinity;
  let n = sequence.length;
  let prefixSum1 = [...sequence];
  let prefixSum2 = [...sequence];

  for (let i = 0; i < n; i++) {
    let pulse1 = Math.pow(-1, i % 2);
    let pulse2 = Math.pow(-1, (i + 1) % 2);

    prefixSum1[i] *= pulse1;
    prefixSum2[i] *= pulse2;
  }

  let min = 0;
  for (let i = 0; i < n; i++) {
    if (i > 0) prefixSum1[i] += prefixSum1[i - 1];

    let sum = prefixSum1[i];
    if (min !== Infinity) sum -= min;

    if (sum > answer) answer = sum;

    if (prefixSum1[i] < min) min = prefixSum1[i];

    if (answer === null) console.log(i, prefixSum1[i], sum, min);
  }

  min = 0;
  for (let i = 0; i < n; i++) {
    if (i > 0) prefixSum2[i] += prefixSum2[i - 1];

    let sum = prefixSum2[i];
    if (min !== Infinity) sum -= min;

    if (sum > answer) answer = sum;

    if (prefixSum2[i] < min) min = prefixSum2[i];

    if (answer === null) console.log(i, prefixSum2[i], sum, min);
  }

  return answer;
}

console.log(solution([3, -6, 1]));
