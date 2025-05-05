document.addEventListener("DOMContentLoaded", function () {
    const animatedSection = document.querySelector(".animated-section");

    function checkVisibility() {
        if (!animatedSection) return; // Prevent errors if the section isn't found

        const sectionPos = animatedSection.getBoundingClientRect().top;
        const screenPos = window.innerHeight / 1.3;

        if (sectionPos < screenPos) {
            animatedSection.classList.add("visible");
        }
    }

    // Ensure the animation triggers after page load
    setTimeout(checkVisibility, 100); // Small delay to ensure elements are rendered

    // Check visibility on scroll
    window.addEventListener("scroll", checkVisibility);

    // Tab system functionality
    const tabs = document.querySelectorAll(".tab-link");
    const tabItems = document.querySelectorAll(".tab-item");

    tabs.forEach(tab => {
        tab.addEventListener("click", function () {
            tabs.forEach(t => t.classList.remove("active"));
            tab.classList.add("active");

            tabItems.forEach(item => item.classList.remove("active"));
            document.getElementById(tab.dataset.tab + "-content").classList.add("active");
        });
    });
});

// Open the "Learn More" Tab
function openTab() {
    document.getElementById("popup-modal").style.display = "flex";
}

// Close the "Learn More" Tab
function closeTab() {
    document.getElementById("popup-modal").style.display = "none";
}
document.addEventListener("DOMContentLoaded", function () {
    const popup = document.getElementById("popup");
    const closeBtn = document.querySelector(".close-btn");
    const learnMoreBtn = document.querySelector(".learn-more-btn");

    // Ensure popup is hidden initially
    popup.style.display = "none";

    // Show Pop-Up on Button Click
    learnMoreBtn.addEventListener("click", function () {
        popup.style.display = "flex"; // Show popup only when clicked
    });

    // Close Pop-Up when clicking the Close Button
    closeBtn.addEventListener("click", function () {
        popup.style.display = "none"; // Hide popup when clicking close
    });

    // Close Pop-Up when clicking outside the modal content
    window.addEventListener("click", function (event) {
        if (event.target === popup) {
            popup.style.display = "none"; // Hide popup
        }
    });
});

function redirectTo(topic) {
    window.location.href = topic + ".html";
}

document.addEventListener("DOMContentLoaded", function () {
    const integrationsSection = document.querySelector(".integrations-section");

    function fadeInOnScroll() {
        const sectionTop = integrationsSection.getBoundingClientRect().top;
        const windowHeight = window.innerHeight;

        if (sectionTop < windowHeight - 100) {
            integrationsSection.classList.add("fade-in");
        }
    }

    window.addEventListener("scroll", fadeInOnScroll);
    fadeInOnScroll(); // Run on page load
});
