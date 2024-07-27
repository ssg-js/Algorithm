function solution(players, callings) {
    var answer = [];
    // 이름에 따른 등수
    const name_to_rank = new Map();
    // 등수에 따른 이름
    const rank_to_name = new Map();
    players.forEach((value, idx, obj) => {
        name_to_rank.set(value, idx);
        rank_to_name.set(idx, value);
    })
    for (var name of callings) {
        var rank = name_to_rank.get(name);
        var opponent = rank_to_name.get(rank-1);
        name_to_rank.set(name, rank-1).set(opponent, rank);
        rank_to_name.set(rank-1, name).set(rank, opponent);
    }
    for (var i = 0; i<players.length; i++) {
        answer.push(rank_to_name.get(i));
    }
    return answer;
}