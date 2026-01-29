// Prototype-only enhancements (safe, minimal)
(function () {
  // Smooth scroll for same-page anchor links
  document.querySelectorAll('a[href^="#"]').forEach((a) => {
    a.addEventListener("click", (e) => {
      const href = a.getAttribute("href");
      if (!href || href === "#") return;

      const target = document.querySelector(href);
      if (!target) return;

      e.preventDefault();
      target.scrollIntoView({ behavior: "smooth", block: "start" });
    });
  });

  // Reveal-on-scroll (subtle)
  const revealEls = document.querySelectorAll(
    ".growth-card, .portfolio-card, .service-item-details, .resume-item, .skill-item, .blog-card"
  );

  revealEls.forEach((el) => el.classList.add("reveal"));

  const io = new IntersectionObserver(
    (entries) => {
      entries.forEach((entry) => {
        if (entry.isIntersecting) {
          entry.target.classList.add("reveal-in");
          io.unobserve(entry.target);
        }
      });
    },
    { threshold: 0.12 }
  );

  revealEls.forEach((el) => io.observe(el));
})();

(function () {
  const cards = document.querySelectorAll(".services-accordions .acc-card");
  if (!cards.length) return;

  cards.forEach((card) => {
    card.addEventListener("toggle", () => {
      if (!card.open) return;
      cards.forEach((other) => {
        if (other !== card) other.removeAttribute("open");
      });
    });
  });
})();
