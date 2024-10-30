function solution(points, routes) {
    var answer = 0;
    let state = []; // [현재좌표, 로봇idx, 목표 지점idx]
    for (let i = 0; i < routes.length; i++) {
        state.push([points[routes[i][0]-1][0]-1, points[routes[i][0]-1][1]-1, i, 1]);
    }
    answer += check(state);
    
    while (state.length) {
        let nextState = [];
        for (let [x, y, rIdx, tIdx] of state) {
            let [tx, ty] = [points[routes[rIdx][tIdx]-1][0]-1, points[routes[rIdx][tIdx]-1][1]-1];
            
            if (x === tx && y === ty) {
                if (tIdx + 1 < routes[rIdx].length) {
                    [tx, ty] = [points[routes[rIdx][tIdx+1]-1][0]-1, points[routes[rIdx][tIdx+1]-1][1]-1];
                    tIdx += 1;
                } else { continue; }
            }
            let np = move(x, y, tx, ty);
            nextState.push([np[0], np[1], rIdx, tIdx]);
        }
        answer += check(nextState);
        state = nextState;
    }
    
    return answer;
}

function check(arr) { // 위험한 상황 갯수 반환
    const board = [...Array(101)].map(()=>[...Array(101)].map(()=>0));
    let ret = 0;
    for (let [x, y, a, b] of arr) {
        if (board[x][y] === 1) {
            ret += 1;
            board[x][y] = 2;
        } else if (board[x][y] === 0) {
            board[x][y] = 1;
        }
    }
    return ret;
}

function move(x, y, nx, ny) {
    if (x < nx) {
        return [x+1, y];
    } else if (x > nx) {
        return [x-1, y];
    } else {
        if (y < ny) {
            return [x, y+1];
        } else {
            return [x, y-1];
        }
    }
}