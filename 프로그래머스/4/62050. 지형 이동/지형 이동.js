function solution(land, height) {
    var answer = 0;
    const n = land.length;
    const infoBoard = [...Array(n)].map(()=>[...Array(n)].map(()=>0)); // 0이면 방문안한곳
    const delta = [[-1, 0], [1, 0], [0, 1], [0, -1]];
    let setNum = 0;
    // height 이하인 점끼리 집합 나누기
    for (let i = 0; i < n; i++) {
        for (let j = 0; j < n; j++) {
            if (infoBoard[i][j] === 0) { // 처리안한곳 찾기
                setNum += 1;
                infoBoard[i][j] = setNum;
                const arr = [[i, j]];
                while (arr.length > 0) {
                    let [x, y] = arr.pop();
                    for (let [dx, dy] of delta) {
                        let [nx, ny] = [x+dx, y+dy];
                        if (0 <= nx && nx < n && 0 <= ny && ny < n && infoBoard[nx][ny] === 0 && Math.abs(land[nx][ny]-land[x][y]) <= height) {
                            arr.push([nx, ny]);
                            infoBoard[nx][ny] = setNum;
                        }
                    }
                }
            }
        }
    }
    // 다른 집합인 곳 인접한 점끼리 [차이, 집합1, 집합2] 로 저장(heap 쓰면 빠름)
    const store = [];
    for (let x = 0; x < n; x++) {
        for (let y = 0; y < n; y++) {
            let [nx, ny] = [x, y+1]; // 오른쪽
            if (0 <= nx && nx < n && 0 <= ny && ny < n && infoBoard[nx][ny] !== infoBoard[x][y]) { // 집합 다르면
                store.push([Math.abs(land[nx][ny] - land[x][y]), [x, y], [nx, ny]]);
            }
            [nx, ny] = [x+1, y]; // 아래
            if (0 <= nx && nx < n && 0 <= ny && ny < n && infoBoard[nx][ny] !== infoBoard[x][y]) { // 집합 다르면
                store.push([Math.abs(land[nx][ny] - land[x][y]), [x, y], [nx, ny]]);
            }
        }
    }
    store.sort((a, b) => a[0]-b[0]);
    // 최소 비용으로 모든 집합 연결
    let cnt = 0;
    for (let i = 0; i < store.length; i++) {
        let [v, a, b] = store[i];
        let [aNum, bNum] = [infoBoard[a[0]][a[1]], infoBoard[b[0]][b[1]]];
        if (aNum === bNum) { continue; } // 같은 집합이면 넘어가기
        answer += v;
        cnt += 1;
        // 둘 비교해서 숫자가 큰 집합애들 작은 집합으로 변환(델타 탐색)
        if (aNum < bNum) { change(b, aNum, infoBoard); }
        else if (aNum > bNum) { change(a, bNum, infoBoard); }
        // setNum-1 만큼 돌았으면 끝
        if (cnt === setNum-1) { break; }
    }
    return answer;
}

function change(point, num, arr) {
    const delta = [[-1, 0], [1, 0], [0, 1], [0, -1]];
    const n = arr.length;
    const origin = arr[point[0]][point[1]];
    const stack = [[...point]];
    arr[point[0]][point[1]] = num;
    while (stack.length > 0) {
        let [x, y] = stack.pop();
        for (let [dx, dy] of delta) {
            let [nx, ny] = [x+dx, y+dy];
            if (0 <= nx && nx < n && 0 <= ny && ny < n && arr[nx][ny] === origin) {
                arr[nx][ny] = num;
                stack.push([nx, ny]);
            }
        }
    }
    return;
}