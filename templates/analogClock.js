var canvas = document.getElementById("canvas");
var ctx = canvas.getContext("2d");
var RADIUS = canvas.height / 2;
ctx.translate(RADIUS, RADIUS);

// draw everything just a little bit inside the canvas
RADIUS = RADIUS * 0.90;

drawClock(ctx, RADIUS);
setInterval(drawClock, 1000, ctx, RADIUS);

function drawClock(ctx, r) {
    var now = new Date();
	drawFace(now, ctx, r);
	drawNumbers(ctx, r);
	drawTime(now, ctx, r);
}

function drawFace(now, ctx, r) {
	var grad;
	
	ctx.beginPath();
	ctx.arc(0, 0, r, 0, 2*Math.PI);
	ctx.fillStyle = "white";
	ctx.fill();
	
	grad = ctx.createRadialGradient(0, 0, r*0.95, 0, 0, r*1.05);
	grad.addColorStop(0, '#063');
	grad.addColorStop(0.5, '#00264d');
	grad.addColorStop(1, '#603');
	ctx.strokeStyle = grad;
	ctx.lineWidth = r * 0.1;
	ctx.stroke();
	
	ctx.beginPath();
	ctx.arc(0, 0, r*0.1, 0, 2*Math.PI);
	ctx.fillStyle = '#333';
	ctx.fill();
}

function drawNumbers(ctx, r) {
	var ang;
	var num;
	
	ctx.font = r * 0.15 + "px times new roman";
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

function drawTime(now, ctx, r) {
	// time --> angle
	// and gotta make sure those angles are exact!
	var second = now.getSeconds() * Math.PI / 30;
	var minute = now.getMinutes() * Math.PI / 30
					+ second / 60;
	var hour = now.getHours() % 12
					+ minute / 60
					+ second / 60 / 60;
	
	drawHand(ctx, hour, r*0.5, r*0.07);
	drawHand(ctx, minute, r*0.8, r*0.04);
	drawHand(ctx, second, r*0.9, r*0.02);
}

function drawHand(ctx, angle, length, width) {
	ctx.strokeStyle = "#333";
	ctx.beginPath();
	ctx.lineWidth = width;
	ctx.lineCap = "round";
	ctx.moveTo(0, 0);
	ctx.rotate(angle);
	ctx.lineTo(0, -length);
	ctx.stroke();
	ctx.rotate(-angle);
}
