function solution(s) {
    var answer = [];
    for (let str of s) {
        const stack = []; 
        let cnt = 0;
        let idx = str.length - 1;
        while (idx >= 0) {
            // stack 마지막이 0일 때 idx에서 11 두개 더 나오는지 검사
            if (stack.length > 0 && stack[stack.length-1] == 0 && checkTwo(idx, str)) {
                cnt += 1;
                stack.pop();
                idx -= 2;
                continue;
            }
            // stack 마지막이 01일 때, idx에서 1인지 검사
            if (stack.length > 1 && stack[stack.length-1] == 1 && stack[stack.length-2] == 0 && str[idx] == 1) {
                cnt += 1;
                stack.pop();
                stack.pop();
                idx -= 1;
                continue;
            }
            stack.push(str[idx]);
            idx -= 1;
        }
        
        str = "";
        idx = -1;
        for (let i = 0; i < stack.length; i++) { // 0 나올때까지 str 만들기
            if (stack[i] == 0) { break; }
            str = "1" + str;
            idx = i;
        }
        idx += 1;
        // 110 넣고 나머지 처리
        for (let i = 0; i < cnt; i++) {
            str = "110" + str;
        }
        for (let i = idx; i < stack.length; i++) {
            str = stack[i] + str;
        }
        answer.push(str);
    }
    
    return answer;
}

function checkTwo(idx, str) { // idx랑 idx-1이 둘 다 1인지 검사
    if (str[idx] != 1) { return false; }
    if (idx - 1 < 0) { return false; } 
    if (str[idx-1] != 1) { return false; }
    return true;
}