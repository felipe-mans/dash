var twelveHours = true;
displayClock(twelveHours);
setInterval(displayClock, 1000, twelveHours);

function displayClock(twelveHours) {
    var clock = document.getElementById("digitalClock");
    var now = new Date();
    var hour = now.getHours();
    var minute = now.getMinutes();
    var second = now.getSeconds();
    
	var hh;
	var am_pm = "";
	if(twelveHours) {
	    // ~~ is equivalent to Math.floor here
		hh = hour % 12;
		am_pm = hour >= 12 ? " PM" : " AM";
	}
	else {
		hh = "" + ~~(hour/10) + hour % 10;
	}
   	var time = [hh,
                "" + ~~(minute/10) + minute % 10,
                "" + ~~(second/10) + second % 10];
    clock.innerHTML = time.join(":") + am_pm;
};
