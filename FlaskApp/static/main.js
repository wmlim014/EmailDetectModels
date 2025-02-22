if (window.history.replaceState) {
    window.history.replaceState(null, null, window.location.href);
}

document.addEventListener("DOMContentLoaded", function () {
    const form = document.getElementById("inputTextForm");
    const resetButton = document.getElementById("resetButton");
    const senderInput = document.getElementById("senderInput");
    const emailTextarea = document.getElementById("emailTextarea");
    const outputSection = document.getElementById("outputSection");

    // Prevent form submission and handle "Run" button click
    form.addEventListener("submit", function (event) {
        event.preventDefault(); // Prevent page refresh

        // Submit the form data to the server
        fetch("/", {
            method: "POST",
            body: new FormData(form),
            headers: {
                "X-Requested-With": "XMLHttpRequest", // Indicates AJAX request
            },
        })
        .then(response => response.text())
        .then(html => {
            // Parse the response HTML
            const parser = new DOMParser();
            const newDocument = parser.parseFromString(html, "text/html");

            // Update the output section with the new content
            const newOutputSection = newDocument.getElementById("outputSection");
            if (newOutputSection) {
                outputSection.innerHTML = newOutputSection.innerHTML; // Update the content
                outputSection.style.display = "block"; // Make the output section visible
            }
        })
        .catch(error => console.error("Error:", error));
    });

    // Reset button functionality
    resetButton.addEventListener("click", function () {
        // Clear input and textarea
        senderInput.value = "";
        emailTextarea.value = "";

        // Hide the output section
        outputSection.style.display = "none";
    });
});