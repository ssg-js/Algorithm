function solution(queue1, queue2) {
    var answer = -2;
    const queue = [...queue1, ...queue2];
    let ascendingStart, ascendingEnd, descendingStart, descendingEnd, cnt, ascendingValue, descendingValue, n;
    n = queue.length;
    const sum = 
    ascendingValue = queue1.reduce((acc, cur)=>acc+cur, 0);    
    descendingValue = ascendingValue;
    const targetValue = (ascendingValue + queue2.reduce((acc, cur)=>acc+cur, 0)) / 2;
    if (targetValue % 1 > 0) { return -1; }
    
    ascendingStart = 0;
    ascendingEnd = queue1.length-1;
    descendingStart = 0;
    descendingEnd = queue1.length -1;
    cnt = 0;
    
    while (cnt < 2 * n) { 
        if (ascendingValue > targetValue) {
            ascendingValue -= queue[ascendingStart];
            ascendingStart = (ascendingStart + 1) % n;
        } else if (ascendingValue < targetValue) {
            ascendingEnd = (ascendingEnd + 1) % n;
            ascendingValue += queue[ascendingEnd];
        } else { return cnt;}
        
        if (descendingValue > targetValue) {
            descendingValue -= queue[descendingStart];
            descendingStart = (descendingStart + 1) % n;
        } else if (descendingValue < targetValue) {
            descendingEnd = (descendingEnd + 1) % n;
            descendingValue += queue[descendingEnd];
        } else { return cnt;}
            
        cnt += 1;
    }
    
    
    return -1;
}