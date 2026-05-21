// Welcome popup
window.onload = function () {
    alert("Welcome to the Waste Management System!");
};

// Show recycling tips
function showTip() {

    let tips = [
        "Recycle plastic bottles properly.",
        "Keep the environment clean.",
        "Separate biodegradable waste.",
        "Do not dump garbage in water.",
        "Reuse paper and bags."
    ];

    let randomTip = tips[Math.floor(Math.random() * tips.length)];

    document.getElementById("tip").innerHTML = randomTip;
}

// Dark mode
function toggleDarkMode() {
    document.body.classList.toggle("dark-mode");
}

// Contact form message
function submitForm() {
    alert("Your report has been submitted successfully!");
}