var twelveHours = true;

var days = new Array(7);
days[0] = "Sunday";
days[1] = "Monday";
days[2] = "Tuesday";
days[3] = "Wednesday";
days[4] = "Thursday";
days[5] = "Friday";
days[6] = "Saturday";

var months = new Array(12);
months[0] = "January";
months[1] = "February";
months[2] = "March";
months[3] = "April";
months[4] = "May";
months[5] = "June";
months[6] = "July";
months[7] = "August";
months[8] = "September";
months[9] = "October";
months[10] = "November";
months[12] = "December";

displayClock(twelveHours);
setInterval(displayClock, 100, twelveHours);

function displayClock(twelveHours) {
    var clock = document.getElementById("digitalClock");
    var now = new Date();
    var hour = now.getHours();
    var minute = now.getMinutes();
    var second = now.getSeconds();
	var hh;
	var am_pm, date = "";
	
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
	
	
    clock.innerHTML = time.join(":") + am_pm + "<br>"
	                  + days[now.getDay()] + ", " + months[now.getMonth()] + " " + now.getDate() + ", " + now.getFullYear();
	
	// out of 360 for hsl
	var degree = (now.getSeconds() + now.getMilliseconds() / 1000) * 6;
	
	var color = "hsl("
	            + degree
				+ ", 100%, 50%)";
	
	var digitalClock = document.getElementById("digitalClock");
	
	digitalClock.style.backgroundColor = "hsl(" + degree + ", 100%, 90%)";
	digitalClock.style.color = "black";//"hsl(" + (degree + 180) % 360 + ", 100%, 20%)";
};
