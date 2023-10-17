// Function to enable navigation bar movement and appearance
const navSlide = () => {
    // Get the menu navigation element
    const menu_nav = document.querySelector('.menu_nav');
    // Get the entire navigation bar
    const nav = document.querySelector('.nav-links');
    // Get all navigation links (e.g., Home, About, etc.)
    const navLinks = document.querySelectorAll('.nav-links li');

    // Toggle Navigation Menu
    menu_nav.addEventListener('click', () => {
        // Toggle the 'nav-active' class to show/hide the navigation menu
        nav.classList.toggle('nav-active');

        // Iterate through each individual navigation link with index
        navLinks.forEach((link, index) => {
            // Capability to reset the animation
            // Check if the link already has an animation
            if (link.style.animation) {
                link.style.animation = '';
            } else {
                // Enable animation with custom timing
                // The 'navLinkFade' animation lasts for 0.5 seconds with a delay based on its index
                link.style.animation = `navLinkFade 0.5s ease forwards ${(index / 7 + 0.2)}s`;
            }
        });

        // Toggle the 'toggle' class to handle 'X' animation (e.g., open/close icon)
        menu_nav.classList.toggle('toggle')
    });
}

// Call the 'navSlide' function to enable navigation bar functionality
navSlide();
