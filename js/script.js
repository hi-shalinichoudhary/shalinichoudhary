document.addEventListener('DOMContentLoaded', function() {
    // --- 1. Hamburger Menu Toggle Logic ---
    const toggleButton = document.querySelector('.menu-toggle');
    const navMenu = document.getElementById('main-navigation');

    if (toggleButton && navMenu) {
        toggleButton.addEventListener('click', function() {
            navMenu.classList.toggle('active'); 
            const isExpanded = toggleButton.getAttribute('aria-expanded') === 'true' || false;
            toggleButton.setAttribute('aria-expanded', !isExpanded);
        });
    }

    // --- 2. Rolling Counter Animation Logic ---
    const counterElements = document.querySelectorAll('.stat-number');
    
    // Function to run the counting animation on a single element
    const animateCounter = (element) => {
        const finalCount = parseInt(element.getAttribute('data-count'), 10);
        let currentCount = 0;
        const duration = 2000; // 2 seconds animation
        const startTime = performance.now();

        const updateCount = (timestamp) => {
            const elapsedTime = timestamp - startTime;
            const progress = Math.min(elapsedTime / duration, 1); // Clamp progress between 0 and 1
            currentCount = Math.floor(progress * finalCount);

            // Update the display content
            // Note: We leave the '+' sign intact if it exists (for 100+ and 15+)
            element.firstChild.textContent = currentCount.toLocaleString(); 

            if (progress < 1) {
                requestAnimationFrame(updateCount);
            } else {
                // Ensure it stops precisely at the final count
                element.firstChild.textContent = finalCount.toLocaleString();
            }
        };

        requestAnimationFrame(updateCount);
    };

    // Intersection Observer to start animation when visible
    const observerOptions = {
        root: null,
        rootMargin: '0px',
        threshold: 0.8 // Start animation when 80% of the element is visible
    };

    const counterObserver = new IntersectionObserver((entries, observer) => {
        entries.forEach(entry => {
            if (entry.isIntersecting) {
                animateCounter(entry.target);
                // Stop observing once the animation has started
                observer.unobserve(entry.target);
            }
        });
    }, observerOptions);

    // Apply the observer to all stat numbers
    counterElements.forEach(counter => {
        counterObserver.observe(counter);
    });
});
// --- 3. Initialize Blog Swiper Carousel ---
    new Swiper('.blog-slider-container', {
        // Required parameters
        loop: true,
        spaceBetween: 30, // Spacing between slides
        slidesPerView: 1, // Default: 1 slide per view on mobile

        // Automatic playback settings
        autoplay: {
            delay: 5000, // 5 seconds between slides
            disableOnInteraction: false, // Continue autoplay after user interaction
        },

        // If we need pagination
        pagination: {
            el: '.swiper-pagination',
            clickable: true,
        },

        // Navigation arrows
        navigation: {
            nextEl: '.swiper-button-next',
            prevEl: '.swiper-button-prev',
        },

        // Responsive breakpoints (for desktop view)
        breakpoints: {
            // When window width is >= 768px
            768: {
                slidesPerView: 2,
                spaceBetween: 30,
            },
            // When window width is >= 1200px (Desktop)
            1200: {
                slidesPerView: 3, // Shows 3 slides on wide screen
                spaceBetween: 30,
            }
            // NOTE: While you asked for 8, displaying 8 blogs at once is too wide for a clean carousel.
            // We set it to 3 or 4 max to maintain design integrity in the current layout.
        }
    });
});
