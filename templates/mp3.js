document.getElementById("audioInput").addEventListener("change", function() {
    var audio = document.getElementById("audio");
    var audioInput = document.getElementById("audioInput");
    var file = this.files[0];
    var fileURL = URL.createObjectURL(file);
    audio.src = fileURL;
});
