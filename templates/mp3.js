document.getElementById("audioInput").addEventListener("change", function() {
	console.log("Something changed!");
	
    var audio = document.getElementById("audio");
	var audioInput = document.getElementById("audioInput")
	var filename = audioInput.value;
	
	console.log("Audio filename = " + filename);
	
	audio.setAttribute("src", filename);
	
	if(filename.slice(-3) === "mp3") {
		audio.setAttribute("type", "audio/mpeg");
	}
	else if(filename.slice(-3) === "ogg") {
	    audio.setAttribute("type", "audio/ogg");
	}
	else if(filename.slice(-3) === "wav") {
	    audio.setAttribute("type", "audio/wav");
	}
});
