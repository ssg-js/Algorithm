function solution(land, height) {
    let answer = 0;
    const n = land.length;
    const visited = [...Array(n)].map(()=>[...Array(n)].map(()=>false));
    const delta = [[-1, 0], [1, 0], [0, 1], [0, -1]];
    const heap = [[0, 0, 0]];
    while (heap.length > 0) {
        let [v, x, y] = minHeapPop(heap);
        if (visited[x][y]) { continue; }
        visited[x][y] = true;
        answer += v;
        for (let [dx, dy] of delta) {
            let [nx, ny] = [x+dx, y+dy];
            if (0 <= nx && nx < n && 0 <= ny && ny < n && !visited[nx][ny]) {
                let sub = Math.abs(land[x][y]-land[nx][ny]);
                minHeapPush(heap, [(sub <= height ? 0 : sub), nx, ny]);
            }
        }
    }
    
    return answer;
}

function minHeapPush(arr, node) {
    arr.push(node);
    let idx = arr.length - 1; // 힙에서 가장 마지막 위치
    while (idx > 0 && arr[Math.floor((idx-1)/2)][0] > arr[idx][0]) { // 현재 num이 num의 부모노드보다 작으면 교체
        arr[idx] = arr[Math.floor((idx-1)/2)];
        arr[Math.floor((idx-1)/2)] = node;
        idx = Math.floor((idx-1)/2);
    }
}

function minHeapPop(arr) {
    if (arr.length === 0) { 
        console.log('heap is empty');
        return NaN;
    }
    // 힙에서 제일 처음 위치랑 마지막 위치 교환
    if (arr.length === 1) { return arr.pop(); }
    let temp = arr[arr.length-1];
    arr[arr.length-1] = arr[0];
    arr[0] = temp;
    const ret = arr.pop();
    let idx = 0;
    while (idx < arr.length) {
        const [llIdx, rlIdx] = [2*idx+1, 2*idx+2];
        if (llIdx >= arr.length) { break; }
        let minChild = llIdx;
        if (rlIdx < arr.length && arr[rlIdx][0] < arr[llIdx][0]) {
            minChild = rlIdx;
        }
        if (arr[idx][0] > arr[minChild][0]) {
            let temp = arr[idx];
            arr[idx] = arr[minChild];
            arr[minChild] = temp
            idx = minChild;
        } else { break; }
    }
    return ret;
}