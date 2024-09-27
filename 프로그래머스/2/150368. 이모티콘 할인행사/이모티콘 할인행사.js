/*
1. 완탐 조져
*/

function solution(users, emoticons) {
    var answer = [0, 0];
    dfs(users, emoticons, answer);    
    
    
    return answer;
}

function dfs(users, emoticons, answer, combi = []) {
    if (combi.length === emoticons.length) {
        let plusMember = 0
        let totalSales = 0;
        for (let [percent, limit] of users) {
            let tempPrice = 0;

            for (let i = 0; i < combi.length; i++) {
                if (combi[i] >= percent) {
                    tempPrice += emoticons[i] * (100-combi[i]) / 100;
                }                
            }
            
            if (tempPrice >= limit) {
                plusMember += 1;
            } else {
                totalSales += tempPrice;
            }
        }
        if (plusMember === answer[0]) {
            answer[1] = Math.max(totalSales, answer[1]);
        } else if(plusMember > answer[0]) {
                answer[0] = plusMember;
                answer[1] = totalSales;
            }
        return;
    }
    
    for (let percent of [40, 30, 20, 10]) {
        dfs(users, emoticons, answer, [...combi, percent]);
    }
} 