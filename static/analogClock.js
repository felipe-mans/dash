var canvas = document.getElementById("analogClock");
var ctx = canvas.getContext("2d");
var RADIUS = canvas.height / 2;
ctx.translate(RADIUS, RADIUS);

// draw everything just a little bit inside the canvas
RADIUS = RADIUS * 0.90;

drawClock(ctx, RADIUS);

function drawClock(ctx, r) {
    var now = new Date();
	// sum up to 360 for hsl
	var degree = (now.getSeconds() + now.getMilliseconds() / 1000) * 6;// + now.getMinutes() * 60 / 10
	var changeColor = document.getElementById("analogChangeColor").checked;
	var colorOutside = changeColor ? "hsl("
	             + degree
				 + ", 100%, 50%)"
				 : "black";
	var colorHands = changeColor ? "hsl("
	             + (180 + degree) % 360
				 + ", 100%, 50%)"
				 : "white";
	drawFace(colorOutside, ctx, r);
	drawNumbers(ctx, r);
	drawHands(now, colorOutside, ctx, r);
	
	var interval = document.getElementById("analogSmoothTicks").checked ? 10 : 1000;
	setTimeout(drawClock, interval, ctx, r);
}

function drawFace(color, ctx, r) {
	canvas.style.backgroundColor = color;
	var grad;
	
	ctx.beginPath();
	ctx.arc(0, 0, r, 0, 2*Math.PI);
	ctx.fillStyle = "white";
	ctx.fill();
	
	grad = ctx.createRadialGradient(0, 0, r*0.95, 0, 0, r*1.05);
	grad.addColorStop(0, "white");
	grad.addColorStop(1, "black");
	ctx.strokeStyle = grad;
	ctx.lineWidth = r * 0.1;
	ctx.stroke();
	
	ctx.beginPath();
	ctx.arc(0, 0, r*0.1, 0, 2*Math.PI);
	ctx.fillStyle = "black";
	ctx.fill();
}

function drawNumbers(ctx, r) {
	var ang;
	var num;
	
	ctx.font = r * 0.19 + "px arial";
	ctx.textBaseline = "middle";
	ctx.textAlign = "center";
	
	for(n = 1; n <= 12; n++) {
		angle = n * Math.PI / 6;
		ctx.rotate(angle);
		ctx.translate(0, -r*0.85);
		ctx.rotate(-angle);
		ctx.fillText(n.toString(), 0, 0);
		ctx.rotate(angle);
		ctx.translate(0, r*0.85);
		ctx.rotate(-angle);
	}
}

function drawHands(now, color, ctx, r) {
	// time --> angle
	var h = now.getHours();
	var m = now.getMinutes();
	var s = now.getSeconds() + now.getMilliseconds() / 1000;
	var hour = h % 12 * Math.PI / 6
	           + m * Math.PI / 3600
			   + s * Math.PI / 21600;
	var minute = m * Math.PI / 30
	             + s * Math.PI / 1800;
	var second = (now.getSeconds() + now.getMilliseconds()/1000) * Math.PI / 30;
	
	drawHand(color, ctx, hour, r*0.5, r*0.07);
	drawHand(color, ctx, minute, r*0.8, r*0.04);
	drawHand(color, ctx, second, r*0.9, r*0.02);
}

function drawHand(color, ctx, angle, length, width) {
	ctx.strokeStyle = color;
	ctx.beginPath();
	ctx.lineWidth = width;
	ctx.lineCap = "round";
	ctx.moveTo(0, 0);
	ctx.rotate(angle);
	ctx.lineTo(0, -length);
	ctx.stroke();
	ctx.rotate(-angle);
}
