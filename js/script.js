document.addEventListener('DOMContentLoaded', function () {
    // --- 1. Hamburger Menu Toggle Logic ---
    const toggleButton = document.querySelector('.menu-toggle');
    const navMenu = document.getElementById('main-navigation');

    if (toggleButton && navMenu) {
        const setMenuState = (isOpen) => {
            navMenu.classList.toggle('active', isOpen);
            navMenu.setAttribute('aria-hidden', (!isOpen).toString());
            toggleButton.setAttribute('aria-expanded', isOpen.toString());
        };

        setMenuState(false);

        toggleButton.addEventListener('click', () => {
            const isOpen = navMenu.classList.contains('active');
            setMenuState(!isOpen);
        });

        navMenu.querySelectorAll('a').forEach((link) => {
            link.addEventListener('click', () => setMenuState(false));
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
    const swiperContainers = document.querySelectorAll('.blog-slider-container');

    if (swiperContainers.length) {
        swiperContainers.forEach((swiperContainer) => {
            if (!swiperContainer.classList.contains('swiper')) {
                swiperContainer.classList.add('swiper');
            }

            const paginationEl = swiperContainer.querySelector('.swiper-pagination');
            const nextEl = swiperContainer.querySelector('.swiper-button-next');
            const prevEl = swiperContainer.querySelector('.swiper-button-prev');

            new Swiper(swiperContainer, {
                loop: true,
                spaceBetween: 30,
                slidesPerView: 1,

                autoplay: {
                    delay: 3000,
                    disableOnInteraction: false,
                },

                pagination: paginationEl
                    ? {
                        el: paginationEl,
                        clickable: true,
                    }
                    : undefined,

                navigation: nextEl && prevEl
                    ? {
                        nextEl,
                        prevEl,
                    }
                    : undefined,

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
        });
    }

    // --- 4. Portfolio Lightbox ---
    const portfolioLinks = document.querySelectorAll('.portfolio-popup');
    const lightbox = document.getElementById('portfolio-lightbox');
    const lightboxImage = lightbox ? lightbox.querySelector('.portfolio-lightbox-image') : null;
    const lightboxClose = lightbox ? lightbox.querySelector('.portfolio-lightbox-close') : null;

    const closeLightbox = () => {
        if (!lightbox || !lightboxImage) {
            return;
        }
        lightbox.classList.remove('is-open');
        lightbox.setAttribute('aria-hidden', 'true');
        lightboxImage.src = '';
        lightboxImage.alt = '';
        document.body.classList.remove('lightbox-open');
    };

    const openLightbox = (imageSrc, imageAlt) => {
        if (!lightbox || !lightboxImage) {
            return;
        }
        lightboxImage.src = imageSrc;
        lightboxImage.alt = imageAlt;
        lightbox.classList.add('is-open');
        lightbox.setAttribute('aria-hidden', 'false');
        document.body.classList.add('lightbox-open');
    };

    if (portfolioLinks.length && lightbox && lightboxImage && lightboxClose) {
        portfolioLinks.forEach(link => {
            link.addEventListener('click', event => {
                event.preventDefault();
                const image = link.querySelector('img');
                const imageSrc = link.getAttribute('href') || (image ? image.src : '');
                const imageAlt = image ? image.alt : 'Portfolio image';
                if (imageSrc) {
                    openLightbox(imageSrc, imageAlt);
                }
            });
        });

        lightboxClose.addEventListener('click', closeLightbox);
        lightbox.addEventListener('click', event => {
            if (event.target === lightbox) {
                closeLightbox();
            }
        });

        document.addEventListener('keydown', event => {
            if (event.key === 'Escape' && lightbox.classList.contains('is-open')) {
                closeLightbox();
            }
        });
    }

    // --- 5. Scroll Reveal Animations (MOVED TO js/scroll-reveal.js) ---
    /*
    const revealTargets = document.querySelectorAll(
        '.section-wrapper, .portfolio-card, .service-item-details, .skill-item, .blog-card, .resume-item, .contact-detail-item'
    );

    if (revealTargets.length) {
        revealTargets.forEach(target => target.classList.add('reveal-on-scroll'));

        const revealObserver = new IntersectionObserver(
            entries => {
                entries.forEach(entry => {
                    if (entry.isIntersecting) {
                        entry.target.classList.add('is-visible');
                        revealObserver.unobserve(entry.target);
                    }
                });
            },
            { threshold: 0.15 }
        );

        revealTargets.forEach(target => revealObserver.observe(target));
    }
    */

    // --- 6. Latest Posts Filter + Toggle ---
    const blogToggleButton = document.querySelector('[data-blog-toggle]');
    const latestGrid = document.querySelector('[data-latest-grid]');
    const blogFilterButtons = document.querySelectorAll('[data-blog-filter]');

    if (latestGrid) {
        const latestCards = Array.from(latestGrid.querySelectorAll('.blog-card'));
        const INITIAL_SHOW_COUNT = 6;

        const updateVisibility = () => {
            const isCollapsed = latestGrid.classList.contains('is-collapsed');
            // If collapsed, show only first 6. If expanded, show all.
            // BUT we must also respect the current category filter.

            const activeFilterBtn = document.querySelector('[data-blog-filter].is-active');
            const activeCategory = activeFilterBtn ? activeFilterBtn.dataset.blogFilter : 'all';

            let visibleCount = 0;

            latestCards.forEach(card => {
                const cardCategory = card.dataset.category || '';
                const matchesFilter = activeCategory === 'all' || cardCategory === activeCategory;

                if (matchesFilter) {
                    // FIX logic: if collapsed, limit to 6. If NOT collapsed, show ALL.
                    if (isCollapsed && visibleCount >= INITIAL_SHOW_COUNT) {
                        card.classList.add('is-hidden');
                    } else {
                        card.classList.remove('is-hidden');
                        visibleCount++;
                    }
                } else {
                    card.classList.add('is-hidden');
                }
            });

            // Update toggle button text
            if (blogToggleButton) {
                if (activeCategory !== 'all') {
                    blogToggleButton.style.display = 'none'; // Hide "View All" when filtering
                } else {
                    blogToggleButton.style.display = 'inline-block';
                    blogToggleButton.textContent = isCollapsed ? 'View all blogs' : 'Show fewer blogs';
                    blogToggleButton.setAttribute('aria-expanded', (!isCollapsed).toString());
                }
            }
        };

        // Initial State
        latestGrid.classList.add('is-collapsed');
        updateVisibility();

        if (blogToggleButton) {
            blogToggleButton.addEventListener('click', () => {
                latestGrid.classList.toggle('is-collapsed');
                updateVisibility();
            });
        }

        blogFilterButtons.forEach(button => {
            button.addEventListener('click', () => {
                blogFilterButtons.forEach(item => item.classList.remove('is-active'));
                button.classList.add('is-active');
                // When filtering, we usually want to show all results for that category, 
                // or reset to collapsed. User said "All blog pages card should appear if user is on the all filter tab"
                // Let's keep existing collapse state but re-run visibility logic.
                // Actually, often filters reset "View All". Let's keep it simple.
                updateVisibility();
            });
        });
    }

    // --- 7. Back to Top Button ---
    const backToTopButton = document.querySelector('.back-to-top');

    if (backToTopButton) {
        const toggleBackToTop = () => {
            if (window.scrollY > 400) {
                backToTopButton.classList.add('is-visible');
            } else {
                backToTopButton.classList.remove('is-visible');
            }
        };

        toggleBackToTop();
        window.addEventListener('scroll', toggleBackToTop, { passive: true });

        backToTopButton.addEventListener('click', () => {
            window.scrollTo({ top: 0, behavior: 'smooth' });
        });
    }

    // --- 8. Navbar Scroll Effect ---
    const siteHeader = document.querySelector('.site-header');
    if (siteHeader) {
        const handleScroll = () => {
            if (window.scrollY > 50) {
                siteHeader.classList.add('scrolled');
            } else {
                siteHeader.classList.remove('scrolled');
            }
        };

        window.addEventListener('scroll', handleScroll, { passive: true });
        handleScroll(); // Initial check
    }
    // --- 9. Social Sidebar Interactions ---
    const interactionButtons = document.querySelectorAll('.interaction-btn');

    if (interactionButtons.length) {
        // Helper: Get unique ID for this post (slug)
        const getPostSlug = () => {
            const path = window.location.pathname;
            return path.split('/').pop().replace('.html', '');
        };
        const postSlug = getPostSlug();

        interactionButtons.forEach(btn => {
            // Load types
            const label = btn.getAttribute('aria-label');

            // 1. LIKE BUTTON
            if (label === 'Like this post') {
                const storageKey = `blog_like_${postSlug}`;
                const isLiked = localStorage.getItem(storageKey) === 'true';

                if (isLiked) {
                    btn.classList.add('active');
                    btn.querySelector('i').classList.replace('far', 'fas'); // Solid icon
                }

                btn.addEventListener('click', () => {
                    const currentlyLiked = btn.classList.contains('active');
                    if (currentlyLiked) {
                        btn.classList.remove('active');
                        btn.querySelector('i').classList.replace('fas', 'far');
                        localStorage.removeItem(storageKey);
                    } else {
                        btn.classList.add('active');
                        btn.querySelector('i').classList.replace('far', 'fas');
                        localStorage.setItem(storageKey, 'true');

                        // Optional: Add a subtle pop animation
                        btn.style.transform = 'scale(1.2)';
                        setTimeout(() => btn.style.transform = '', 200);
                    }
                });
            }

            // 2. BOOKMARK BUTTON
            else if (label === 'Bookmark this post') {
                const storageKey = `blog_bookmark_${postSlug}`;
                const isBookmarked = localStorage.getItem(storageKey) === 'true';

                if (isBookmarked) {
                    btn.classList.add('active');
                    btn.querySelector('i').classList.replace('far', 'fas');
                }

                btn.addEventListener('click', () => {
                    const currentlyBookmarked = btn.classList.contains('active');
                    if (currentlyBookmarked) {
                        btn.classList.remove('active');
                        btn.querySelector('i').classList.replace('fas', 'far');
                        localStorage.removeItem(storageKey);
                    } else {
                        btn.classList.add('active');
                        btn.querySelector('i').classList.replace('far', 'fas');
                        localStorage.setItem(storageKey, 'true');
                    }
                });
            }

            // 3. COPY LINK
            else if (label === 'Copy Link') {
                btn.addEventListener('click', () => {
                    navigator.clipboard.writeText(window.location.href).then(() => {
                        // visuals
                        const originalIcon = btn.innerHTML;
                        btn.innerHTML = '<i class="fas fa-check"></i>';
                        btn.classList.add('active');

                        setTimeout(() => {
                            btn.innerHTML = originalIcon;
                            btn.classList.remove('active');
                        }, 2000);
                    }).catch(err => {
                        console.error('Failed to copy: ', err);
                    });
                });
            }

            // 4. TWITTER SHARE
            else if (label === 'Share on Twitter') {
                btn.addEventListener('click', (e) => {
                    e.preventDefault();
                    const url = encodeURIComponent(window.location.href);
                    const text = encodeURIComponent(document.title);
                    window.open(`https://twitter.com/intent/tweet?text=${text}&url=${url}`, '_blank', 'width=600,height=400');
                });
            }

            // 5. LINKEDIN SHARE
            else if (label === 'Share on LinkedIn') {
                btn.addEventListener('click', (e) => {
                    e.preventDefault();
                    const url = encodeURIComponent(window.location.href);
                    window.open(`https://www.linkedin.com/sharing/share-offsite/?url=${url}`, '_blank', 'width=600,height=400');
                });
            }
        });
    }
});
