

function solution(numbers) {
    var answer = 0;
    loop1: for (let i = 1; i < 10; i++) {
        for (let num of numbers) {
            if (num === i) { continue loop1; }
        }
        answer += i;
    }
    return answer;
}