function solution(fees, records) {
    var answer = [];
    let cars = [];
    for (let info of records) {
        let [time, carNum, type] = info.split(" ");
        if (type === "IN") {
            let [isIn, idx] = isInAndWhere(carNum, cars);
            if (isIn === true) {
                let instance = cars[idx];
                instance.enter(time);
            } else {
                cars.push(new car(carNum, time, ...fees))
            }
        } else {
            let [ , idx] = isInAndWhere(carNum, cars);
            let instance = cars[idx];
            instance.exit(time);
        }
    }
    cars.sort((a, b) => a.number - b.number);
    console.log(cars);
    for (let instance of cars) {
        answer.push(instance.getPrice());
    }
    
    return answer;
}

function getTime(s, e) {
    let [enterHour, enterMin] = s.split(":").map(Number);
    let [exitHour, exitMin] = e.split(":").map(Number);
    let ret = 0;
    
    if (exitMin < enterMin) { 
        exitHour -= 1;
        ret += 60 + exitMin - enterMin;
    } else { ret += exitMin - enterMin; }
    ret += (exitHour - enterHour) * 60;
    
    return ret;
}

function isInAndWhere(number, arr) {
    number = Number(number);
    for (let i = 0; i < arr.length; i++) {
        let instance = arr[i];
        if (instance.number === number) {return [true, i];}
    }
    return [false, ];
}

class car {
    constructor(number, time, ...args) {
        this.number = Number(number);
        this.totalTime = 0;
        this.entered = true;
        this.enterTime = time;
        this.basicTime = args[0];
        this.basicPrice = args[1];
        this.plusTime = args[2];
        this.plusPrice = args[3]
    }
    getPrice() {
        if (this.entered === true) { this.totalTime += getTime(this.enterTime, "23:59"); }
    if (this.totalTime > this.basicTime) {
        return this.basicPrice + Math.ceil((this.totalTime - this.basicTime) / this.plusTime) * this.plusPrice;
    } else { return this.basicPrice; }
    }
    enter(time) {
        this.enterTime = time;
        this.entered = true;
    }
    exit(time) {
        this.totalTime += getTime(this.enterTime, time);
        this.enterTime = "00:00";
        this.entered = false;
    }
}