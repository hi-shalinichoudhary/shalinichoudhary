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
        const plusSign = element.querySelector('.plus-sign');

        const updateCount = (timestamp) => {
            const elapsedTime = timestamp - startTime;
            const progress = Math.min(elapsedTime / duration, 1); 
            currentCount = Math.floor(progress * finalCount);

            // CRITICAL FIX: Simplified update logic to avoid firstChild errors
            let displayValue = currentCount.toLocaleString();
            
            if (plusSign) {
                // If plus sign exists, update the text node *before* the plus sign element
                element.innerHTML = displayValue + '<span class="plus-sign">+</span>';
            } else {
                // Otherwise, update the entire text content
                element.textContent = displayValue;
            }

            if (progress < 1) {
                requestAnimationFrame(updateCount);
            } else {
                // Ensure it stops precisely at the final count
                if (plusSign) {
                    element.innerHTML = finalCount.toLocaleString() + '<span class="plus-sign">+</span>';
                } else {
                    element.textContent = finalCount.toLocaleString();
                }
            }
        };

        // Set an attribute to prevent double animation attempts
        element.setAttribute('data-animated', 'true');
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
            // CRITICAL CHECK: Only animate if intersecting AND hasn't been animated before
            if (entry.isIntersecting && !entry.target.hasAttribute('data-animated')) {
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


    // --- 3. Initialize Blog Swiper Carousel ---
    // The Swiper init is now correctly inside the DOMContentLoaded handler
    if (document.querySelector('.blog-slider-container')) {
        // Find the specific container element
        const swiperContainer = document.querySelector('.blog-slider-container');
        
        // CRITICAL CHECK: Swiper initialization requires the 'swiper' class on the container
        // Ensure the 'swiper' class is present before initializing (as requested in the last fix)
        if (!swiperContainer.classList.contains('swiper')) {
            swiperContainer.classList.add('swiper');
        }


        new Swiper('.blog-slider-container', {
            loop: true,
            spaceBetween: 30, 
            slidesPerView: 1, 

            autoplay: {
                delay: 5000, 
                disableOnInteraction: false, 
            },

            pagination: {
                el: '.swiper-pagination',
                clickable: true,
            },

            navigation: {
                nextEl: '.swiper-button-next',
                prevEl: '.swiper-button-prev',
            },

            breakpoints: {
                768: {
                    slidesPerView: 2,
                    spaceBetween: 30,
                },
                1200: {
                    slidesPerView: 3, 
                    spaceBetween: 30,
                }
            }
        });
    }
});
