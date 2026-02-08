/**
 * Scroll Reveal Animations
 * 
 * Applies 'is-visible' class to elements when they enter the viewport.
 * Supports staggered animations via data attributes or CSS delays.
 */

document.addEventListener('DOMContentLoaded', () => {
    console.log('Scroll Reveal: Script loaded');

    // Elements to reveal
    const revealElements = document.querySelectorAll('.reveal');
    console.log(`Scroll Reveal: Found ${revealElements.length} elements to reveal`);

    if (!revealElements.length) return;

    const revealObserver = new IntersectionObserver((entries, observer) => {
        entries.forEach(entry => {
            if (entry.isIntersecting) {
                const target = entry.target;
                console.log('Scroll Reveal: Revealing element', target);

                // Add class to trigger CSS transition
                target.classList.add('is-visible');

                // Stop observing once revealed (run once)
                observer.unobserve(target);
            }
        });
    }, {
        root: null,
        rootMargin: '0px',
        threshold: 0.1
    });

    revealElements.forEach(el => revealObserver.observe(el));

    // SAFETY FALLBACK: If observer doesn't fire (e.g. initial load glitch), 
    // force reveal visible elements after a short delay
    setTimeout(() => {
        revealElements.forEach(el => {
            const rect = el.getBoundingClientRect();
            if (rect.top < window.innerHeight) {
                el.classList.add('is-visible');
            }
        });
    }, 500);
});
