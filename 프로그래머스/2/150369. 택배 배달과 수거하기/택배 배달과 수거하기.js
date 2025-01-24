function solution(cap, n, deliveries, pickups) {
    var answer = 0;
    let maxDelivery, maxPickup;
    for (let i = n-1; i > -1; i--) {
        if (deliveries[i] > 0) {
            maxDelivery = i;
            break;
        }
    }
    for (let i = n-1; i > -1; i--) {
        if (pickups[i] > 0) {
            maxPickup = i;
            break;
        }
    }
    
    let distance, spare, idx;
    while (maxDelivery >= 0 || maxPickup >= 0) {
        answer += Math.max(maxDelivery+1, maxPickup+1) * 2;
        // 배달
        spare = cap;
        idx = maxDelivery;
        while (spare >= 0 && idx >= 0) {
            deliveries[idx] -= spare;
            spare = -1 * deliveries[idx];
            idx -= 1;
            if (spare >= 0) {
                maxDelivery = idx;
            }
        }
        // 수거
        spare = cap;
        idx = maxPickup;
        while (spare >= 0 && idx >= 0) {
            pickups[idx] -= spare;
            spare = -1 * pickups[idx];
            idx -= 1;
            if (spare >= 0) {
                maxPickup = idx;
            }
        }
        
    }
    
    return answer;
}