function solution(arr) {
    var answer = [0, 0];
    recur(0, 0, 0, arr.length-1, arr.length-1, arr, answer);
    return answer;
}

function recur(depth, sx, sy, ex, ey, arr, answer) {
    if (sx === ex && sy === ey) { // 여기선 answer 건드리면 안됨 압축되는지 판단을 못함
        if (depth === 0) { answer[arr[sx][sy]] += 1; }
        return arr[sx][sy]; 
    } 
    
    let half = (ex - sx + 1) / 2;
    
    let lu = recur(depth+1, sx, sy, sx+half-1, sy+half-1, arr, answer); // 왼위
    let ru = recur(depth+1, sx, sy+half, sx+half-1, ey, arr, answer); // 오위
    let ld = recur(depth+1, sx+half, sy, ex, sy+half-1, arr, answer); // 왼아래
    let rd = recur(depth+1, sx+half, sy+half, ex, ey, arr, answer); // 오아래
    
    // 다 같으면
    if (lu === ru && ru === ld && ld === rd && lu !== -1) { 
        if (depth === 0) { answer[lu] += 1; }
        return lu; 
    }
    
    // 다르면
    if (lu !== -1) { answer[lu] += 1; }
    if (ru !== -1) { answer[ru] += 1; }
    if (ld !== -1) { answer[ld] += 1; }
    if (rd !== -1) { answer[rd] += 1; }
    return -1; // 지금 배열 처리했다는 표시
}