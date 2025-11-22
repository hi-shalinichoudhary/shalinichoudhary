document.addEventListener('DOMContentLoaded', function() {
    const toggleButton = document.querySelector('.menu-toggle');
    const navMenu = document.getElementById('main-navigation');

    if (toggleButton && navMenu) {
        toggleButton.addEventListener('click', function() {
            // Toggles the 'active' class on the navigation menu
            navMenu.classList.toggle('active'); 
            
            // Toggle accessibility attributes
            const isExpanded = toggleButton.getAttribute('aria-expanded') === 'true' || false;
            toggleButton.setAttribute('aria-expanded', !isExpanded);
        });
    }
});
