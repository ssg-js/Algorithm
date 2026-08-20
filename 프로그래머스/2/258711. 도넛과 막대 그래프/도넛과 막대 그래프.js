// 생성한 정점을 판별할수 있나? => 일단 들어오는 간선은 없음, 나가는 간선이 최소 2개
// 도넛 모양 => 한 정점에서 나가는 간선 1개 + 들어오는 간선 1개
//         => 정점 갯수가 크기
// 막대 => 나가는 정점 하나 + 들어오고 나가는 정점 여러개 + 들어오는 정점 1개
//     => 정점 갯수가 크기
// 8자 => 한 정점에서 나가는 간선 1개 + 들어오는 간선 1개
//    => (정점 갯수-1)/2가 크기
// 막대모양이랑 도넛 모양 판별이 애매함. 8자는 무조건 나가는간선 1개 들어오는 간선 1개로 판별가능 (먼저 세기)


function solution(edges) {
    var answer = [0, 0, 0, 0];
    let maxNum = 0
    for (let [a, b] of edges) {
        maxNum = Math.max(a, b, maxNum);
    }
    let board = [...Array(maxNum + 1)].map(()=>[0, 0]);
    let pointBoard = [...Array(maxNum + 1)].map(()=>false);
    for (let [a, b] of edges) {
        board[a][0] += 1;
        board[b][1] += 1;
        pointBoard[a] = true;
        pointBoard[b] = true;
    }
    let pointNum = 0;
    for (let bool of pointBoard) {
        if (bool) { pointNum += 1;}
    }
    let graphNum = 0;
    for (let i = 0; i < board.length; i++) {
        if (board[i][0] > 1 && board[i][1] == 0) { // 생성된 정점
            answer[0] = i;
            graphNum = board[i][0];
            continue;
        }
        if (board[i][0] == 2 && board[i][1]) { // 8자
            answer[3] += 1;
        }
    }
    answer[2] = (pointNum - edges.length - 1 + graphNum) + answer[3];
    answer[1] = graphNum - answer[2] - answer[3];
    
    
    
    return answer;
}


