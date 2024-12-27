function solution(n, info) {
    const answer = [];
    
    find(1, [0], n, info, answer);
    
    if (answer.length === 0) {
        answer.push(-1);
    }
    
    return answer;
}

function find(curPoint, arr, spareArrow, info, answer) { // 에 차곡차곡 조건을 만족하게 조합 생성
    if (spareArrow < 0) {
        return;
    }
    
    if (curPoint === 11) {
        if (cal(info, arr) > 0) {
            if (answer.length === 11 && cal(info, arr) <= cal(info, answer)) {
                return;
            }
            arr[10] = spareArrow; // 0점에 남은 화살 몰빵
            while (answer.length > 0) {
                answer.pop();
            }
            arr.forEach((v)=>answer.push(v));
        }
        return;
    }
    
    const curIdx = 10 - curPoint;
    // 현재 점수 얻기
    find(curPoint+1, [info[curIdx]+1, ...arr], spareArrow-info[curIdx]-1, info, answer);
    
    // 현재 점수 포기
    find(curPoint+1, [0, ...arr], spareArrow, info, answer);
    
    return;
}

function cal(arr1, arr2) { // arr1, arr2의 점수 차이 반환
    let aSum = 0;
    let bSum = 0;
    for (let i = 0; i < 11; i++) {
        if (arr1[i] < arr2[i]) {
            bSum += 10-i;
        } else if (arr1[i] > arr2[i]) {
            aSum += 10-i;
        }
    }
    
    return bSum - aSum;
}