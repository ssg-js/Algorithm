function solution(bandage, health, attacks) {
    var answer = health;
    const [bandageTime, recoveryVolume, additiveRecovery] = bandage;

    for (let i=0; i < attacks.length; i++) {
        const [attackTime, attackPower] = attacks[i];
        
        // recovery
        if (i > 0) {
            const subTime = attackTime-attacks[i-1][0]-1;
            if (subTime > 0) {
                answer = Math.min(health, answer + (subTime * recoveryVolume));
                if (subTime >= bandageTime) { 
                    answer = Math.min(health, answer + Math.floor(subTime / bandageTime) * additiveRecovery); 
                }    
            }
            
        }
        
        // attacked
        answer -= attackPower;
        if (answer <= 0) {
            answer = -1;
            return answer;
        }
    }
    
    return answer;
}