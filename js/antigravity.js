/**
 * Antigravity Effect (Particles)
 * 
 * Creates a canvas overlay on the hero section with interactive particles
 * that follow/react to the mouse cursor.
 * 
 * Optimized for mobile and responsiveness.
 */

document.addEventListener('DOMContentLoaded', () => {
    const heroSection = document.querySelector('.hero');
    if (!heroSection) return;

    // 1. Setup Canvas
    const canvas = document.createElement('canvas');
    canvas.id = 'hero-particles';

    // Style
    canvas.style.position = 'absolute';
    canvas.style.top = '0';
    canvas.style.left = '0';
    canvas.style.width = '100%';
    canvas.style.height = '100%';
    canvas.style.pointerEvents = 'none'; // Critical for clicking links
    canvas.style.zIndex = '0';

    if (getComputedStyle(heroSection).position === 'static') {
        heroSection.style.position = 'relative';
    }

    heroSection.insertBefore(canvas, heroSection.firstChild);

    const ctx = canvas.getContext('2d');
    let width, height;
    let particles = [];

    // Configuration
    let config = {
        particleCount: 80,
        connectionDist: 100,
        baseSpeed: 0.5
    };

    // 2. Resize Handler & Responsive Config
    function resize() {
        width = canvas.width = heroSection.offsetWidth;
        height = canvas.height = heroSection.offsetHeight;

        // Responsive adjustments
        if (width < 768) {
            // Mobile
            config.particleCount = 40; // Fewer particles
            config.connectionDist = 80; // Shorter connection range
        } else {
            // Desktop
            config.particleCount = 80;
            config.connectionDist = 120;
        }

        initParticles();
    }
    window.addEventListener('resize', resize);

    // 3. Mouse/Touch State
    const mouse = { x: -1000, y: -1000 };

    function updateMouse(e) {
        const rect = canvas.getBoundingClientRect();
        mouse.x = e.clientX - rect.left;
        mouse.y = e.clientY - rect.top;
    }

    document.addEventListener('mousemove', updateMouse);

    // Touch support - ensure smooth interaction without blocking scroll
    // We only track the position; pointer-events:none allows scroll to pass through to underlying elements
    function handleTouch(e) {
        if (e.touches.length > 0) {
            updateMouse(e.touches[0]);
        }
    }

    document.addEventListener('touchmove', handleTouch);
    document.addEventListener('touchstart', handleTouch);


    // 4. Particle System
    class Particle {
        constructor() {
            this.x = Math.random() * width;
            this.y = Math.random() * height;
            this.vx = (Math.random() - 0.5) * config.baseSpeed;
            this.vy = (Math.random() - 0.5) * config.baseSpeed;
            this.size = Math.random() * 2 + 1;
            this.color = `rgba(0, 0, 0, ${Math.random() * 0.2 + 0.1})`;
        }

        draw() {
            ctx.fillStyle = this.color;
            ctx.beginPath();
            ctx.arc(this.x, this.y, this.size, 0, Math.PI * 2);
            ctx.fill();
        }

        update() {
            // Mouse Interaction
            let dx = mouse.x - this.x;
            let dy = mouse.y - this.y;
            let distance = Math.sqrt(dx * dx + dy * dy);

            const maxDistance = 150;

            if (distance < maxDistance) {
                const forceDirectionX = dx / distance;
                const forceDirectionY = dy / distance;
                const force = (maxDistance - distance) / maxDistance;
                const attractionStrength = 2; // Strength

                this.vx += forceDirectionX * force * attractionStrength * 0.1;
                this.vy += forceDirectionY * force * attractionStrength * 0.1;
            }

            // Damping
            this.vx *= 0.95;
            this.vy *= 0.95;

            // Velocity limits to prevent getting stuck
            // Add a tiny bit of random movement if stopped
            if (Math.abs(this.vx) < 0.01) this.vx += (Math.random() - 0.5) * 0.1;
            if (Math.abs(this.vy) < 0.01) this.vy += (Math.random() - 0.5) * 0.1;

            this.x += this.vx;
            this.y += this.vy;

            // Wrap around
            if (this.x < 0) this.x = width;
            if (this.x > width) this.x = 0;
            if (this.y < 0) this.y = height;
            if (this.y > height) this.y = 0;
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

        // Update and draw particles
        for (let i = 0; i < particles.length; i++) {
            particles[i].update();
            particles[i].draw();
        }

        // Draw connections
        connectParticles();

        requestAnimationFrame(animate);
    }

    function connectParticles() {
        // Optimization: Use squared distance to avoid Math.sqrt in loop
        const maxDistSq = config.connectionDist * config.connectionDist;

        ctx.lineWidth = 1;

        for (let a = 0; a < particles.length; a++) {
            for (let b = a + 1; b < particles.length; b++) {
                const dx = particles[a].x - particles[b].x;
                const dy = particles[a].y - particles[b].y;
                const distSq = dx * dx + dy * dy;

                if (distSq < maxDistSq) {
                    const opacityValue = 1 - (distSq / maxDistSq);
                    ctx.strokeStyle = `rgba(0, 0, 0, ${opacityValue * 0.08})`; // Slight increase in visibility
                    ctx.beginPath();
                    ctx.moveTo(particles[a].x, particles[a].y);
                    ctx.lineTo(particles[b].x, particles[b].y);
                    ctx.stroke();
                }
            }
        }
    }

    // Initialize
    resize();
    animate();
});
