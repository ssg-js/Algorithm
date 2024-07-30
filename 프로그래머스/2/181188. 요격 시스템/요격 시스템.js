function solution(targets) {
    var answer = 0;
    targets.sort((a, b) => {
        return a[1] - b[1];
    })
    var end = 0;
    for (var point of targets) {
        if (point[0] >= end) {
            answer += 1;
            end = point[1]
        }
    }
    
    return answer
    
}