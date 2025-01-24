function solution(today, terms, privacies) {
    var answer = [];
    
    let date, type, expireDate;
    for (let i = 0; i < privacies.length; i++) {
        [date, type] = privacies[i].split(" ");
        for (let j = 0; j < terms.length; j++) {
            let [t, v] = terms[j].split(" ")
            if (type === t) {
                expireDate = plusMonth(date, v);
                break;
            }
        }
        if (compareDate(expireDate, today)) {
            answer.push(i+1);
        }
    }
    
    return answer;
}

function compareDate(norm, v) { // v가 더 나중이면 true
    let normToDay = toDay(...norm.split('.'));
    let vToDay = toDay(...v.split('.'));
    if (normToDay < vToDay) { return true; }
    return false;
}

function toDay(y, m, d) {
    let ret = 0;
    ret += Number(y) * 28 * 12 + Number(m) * 28 + Number(d);
    return ret;
}

function plusMonth(date, v) {
    let [y, m, d] = date.split(".").map(Number);
    // 월 처리
    m += Number(v);
    if (m > 12) {
        m -= 12;
        y += 1;
    }
    // 일 처리
    d -= 1;
    if (d === 0) {
        d = 28;
        m -= 1;
    }
    if (m === 0) {
        m = 12;
        y -= 1;
    }
    return `${y}.${m}.${d}`;
}