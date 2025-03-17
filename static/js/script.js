document.querySelector("form").addEventListener("submit", function(event) {
    event.preventDefault();  // Prevents immediate form submission

    let progressContainer = document.getElementById("progress-container");
    let progressBar = document.getElementById("progress-bar");
    let progressText = document.getElementById("progress-text");
    let downloadBtn = document.getElementById("download-btn");

    progressContainer.style.display = "block";
    downloadBtn.textContent = "Downloading...";
    downloadBtn.disabled = true;  // Prevent multiple clicks

    let width = 0;
    let interval = setInterval(function() {
        if (width >= 100) {
            clearInterval(interval);
            downloadBtn.textContent = "Download Complete";
            document.querySelector("form").submit();  // Submit after progress reaches 100%
        } else {
            width += 5; 
            progressBar.style.width = width + "%";
            progressText.textContent = width + "%";
        }
    }, 300);
});
