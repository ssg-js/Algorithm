function solution(n, info) {
    var answer = [];
    
    let maxSub = 0;
    let state = [...Array(11)].map(()=>0);
    let spare, apeach, ryan;
    for (let num = 1; num < (1 << 11); num++) { // 1인 비트는 무조건 어피치보다 많이 맞춰야함
        spare = n;
        // 주어진 비트 상태에 맞게 화살 갯수 정하기
        for (let i = 0; i < 10; i++) { // 1점까지만 구함
            if (num & (1 << (10-i))) {
                spare -= info[i] + 1;
                state[i] = info[i] + 1;
            } else {
                state[i] = 0;
            }
        }
        if (spare < 0) { continue; }
        state[10] = spare;
        // 어피치랑 점수 비교
        apeach = 0;
        ryan = 0;
        for (let i = 0; i < 10; i++) {
            if (info[i] > state[i]) {
                apeach += 10-i;
            }
            if (info[i] < state[i]) {
                ryan += 10-i;
            }
        }
        if (apeach >= ryan) { continue; }
        
        // 가장 큰 점수 차이고, 같으면 가장 낮은 점수를 더 많이 맞힌 경우(num이 작은) 경우 선택
        if (ryan - apeach > maxSub) {
            answer = [...state];
            maxSub = ryan - apeach;
        } else if (ryan - apeach === maxSub) { // 같으면
            let bool = false;
            for (let i = 10; i > -1; i--) {
                if (answer[i] > state[i]) {
                    break;
                }
                if (answer[i] < state[i]) {
                    bool = true;
                    break;
                }
            }
            if (bool) {
                answer = [...state];
            }
        }
        
    }
    
    if (answer.length === 0) {
        answer.push(-1);
    }
    
    return answer;
}