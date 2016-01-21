displayClock();
setInterval(displayClock, 1000);

function displayClock() {
    var clock = document.getElementById("digitalClock");
    var now = new Date();
    var hour = now.getHours();
    var minute = now.getMinutes();
    var second = now.getSeconds();
    
    // ~~ is equivalent to Math.floor here
    var time = ["" + ~~(hour/10) + hour % 10,
                "" + ~~(minute/10) + minute % 10,
                "" + ~~(second/10) + second % 10];
    clock.innerHTML = time.join(":") + (hour >= 12 ? " p.m." : " a.m.");
};
