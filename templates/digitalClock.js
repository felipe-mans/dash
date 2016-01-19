displayClock();
setInterval(displayClock, 1000);

function displayClock() {
    var clock = document.getElementById("digitalClock");
    var now = new Date();
    var second = now.getSeconds();
    var minute = now.getMinutes();
    var hour = now.getHours();
    clock.innerHTML = [hour % 13, minute, second].join(":").toString()
                      + (hour > 12) ? "pm" : "am";
};
