/**
 * Antigravity Effect (Cursor Swarm)
 * 
 * Creates a "bubble-like" swarm of particles that follows the cursor
 * and 'breathes' (expands/contracts) when static.
 */

document.addEventListener('DOMContentLoaded', () => {
    const heroSection = document.querySelector('.hero');
    if (!heroSection) return;

    // 1. Setup Canvas
    const canvas = document.createElement('canvas');
    canvas.id = 'hero-particles';

    canvas.style.position = 'absolute';
    canvas.style.top = '0';
    canvas.style.left = '0';
    canvas.style.width = '100%';
    canvas.style.height = '100%';
    canvas.style.pointerEvents = 'none';
    canvas.style.zIndex = '0';

    if (getComputedStyle(heroSection).position === 'static') {
        heroSection.style.position = 'relative';
    }

    heroSection.insertBefore(canvas, heroSection.firstChild);

    const ctx = canvas.getContext('2d');
    let width, height;

    // Mouse State
    let mouse = { x: -1000, y: -1000 };
    let isMouseActive = false;

    // Configuration
    const config = {
        particleCount: 200,        // Significantly more dots
        baseRadius: 250,           // Much wider (covers more width)
        breathingSpeed: 0.002,     // Slower pulse for large size
        breathingRange: 30,        // Larger pulse range
        color: 'rgba(60, 60, 60, 0.8)' // Dark Grey
    };

    let particles = [];
    let time = 0;

    // 2. Resize Handler
    function resize() {
        width = canvas.width = heroSection.offsetWidth;
        height = canvas.height = heroSection.offsetHeight;

        // Center mouse initially if not active
        if (!isMouseActive) {
            mouse.x = width / 2;
            mouse.y = height / 2;
        }

        // Adjust config for mobile if needed
        if (width < 768) {
            config.particleCount = 100;
            config.baseRadius = 150;
        } else {
            config.particleCount = 200;
            config.baseRadius = 250;
        }

        initParticles();
    }
    window.addEventListener('resize', resize);

    // 3. Mouse Handlers
    function updateMouse(x, y) {
        const rect = canvas.getBoundingClientRect();
        mouse.x = x - rect.left;
        mouse.y = y - rect.top;
        isMouseActive = true;
    }

    document.addEventListener('mousemove', e => updateMouse(e.clientX, e.clientY));

    document.addEventListener('touchmove', e => {
        if (e.touches.length > 0) {
            updateMouse(e.touches[0].clientX, e.touches[0].clientY);
        }
    });

    // 4. Particle Class
    class Particle {
        constructor() {
            // Random angle and radius offset for "bubble" shape
            this.angle = Math.random() * Math.PI * 2;
            // Square root distribution for uniform circle fill? 
            // Or simple linear for dense center? Let's use simple for now.
            this.radiusOffset = Math.random();
            this.speed = 0.01 + Math.random() * 0.02; // Slower orbit for large swarm
            this.size = Math.random() * 3 + 2;

            // Current position (starts at mouse)
            this.x = mouse.x;
            this.y = mouse.y;

            // For smooth following
            this.vx = 0;
            this.vy = 0;
            this.friction = 0.92;
            this.ease = 0.04 + Math.random() * 0.04; // Slightly looser follow
        }

        update(breathingOffset) {
            // 1. Calculate Target Position based on Mouse + Orbit/Swarm
            // The "Bubble" is defined by dynamic radius
            const currentRadius = (config.baseRadius + breathingOffset) * this.radiusOffset;

            // Rotate the particle slightly for "alive" feel
            this.angle += this.speed;

            // WIDER THAN TALL (Ellipse) to cover width better?
            // Let's multiply X by 1.5 to make it an ellipse.
            const targetX = mouse.x + (Math.cos(this.angle) * currentRadius * 1.5);
            const targetY = mouse.y + (Math.sin(this.angle) * currentRadius);

            // 2. Move towards target (Easing)
            this.x += (targetX - this.x) * this.ease;
            this.y += (targetY - this.y) * this.ease;
        }

        draw() {
            ctx.fillStyle = config.color;
            ctx.beginPath();
            ctx.arc(this.x, this.y, this.size, 0, Math.PI * 2);
            ctx.fill();
        }
    }

    function initParticles() {
        particles = [];
        for (let i = 0; i < config.particleCount; i++) {
            particles.push(new Particle());
        }
    }

    // 5. Animation Loop
    function animate() {
        ctx.clearRect(0, 0, width, height);
        time += 1;

        // Breathing Calculation
        // Sine wave between -1 and 1, scaled by range
        const breathingOffset = Math.sin(time * config.breathingSpeed * 10) * config.breathingRange;

        particles.forEach(p => {
            p.update(breathingOffset);
            p.draw();
        });

        requestAnimationFrame(animate);
    }

    // Start
    resize();
    animate();
});
