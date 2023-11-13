function solution(today, terms, privacies) {
    var answer = [];
    var today_day = Number(today.substr(0,4)) * 28 * 12 + Number(today.substr(5,2)) * 28 + Number(today.substr(8,2));
    for (var i = 0; i < privacies.length; i++) {
        var date = Number(privacies[i].substr(0,4)) * 28 * 12 + Number(privacies[i].substr(5,2)) * 28 + Number(privacies[i].substr(8,2));
        var type = privacies[i].slice(-1);
        terms.forEach((value) => {
            var t = value.substr(0,1);
            if (type == t) {
                if (date + Number(value.slice(2)) * 28 - 1 < today_day) {
                    answer.push(i+1);
                }
            }
        })
        
    }
    return answer;
}