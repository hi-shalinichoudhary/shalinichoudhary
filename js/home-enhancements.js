/* Homepage enhancements: count-up stats. */
(function () {
  'use strict';

  var figures = document.querySelectorAll('.stat-figure');
  if (!figures.length) return;

  var reduce = window.matchMedia('(prefers-reduced-motion: reduce)').matches;
  var numberRe = /\d+(\.\d+)?/g;

  function animate(el) {
    var original = el.getAttribute('data-original');
    var targets = original.match(numberRe) || [];
    var parts = original.split(numberRe);
    var duration = 1600;
    var start = null;

    function ease(t) { return 1 - Math.pow(1 - t, 3); }

    function frame(ts) {
      if (start === null) start = ts;
      var p = Math.min((ts - start) / duration, 1);
      var out = parts[0];
      for (var i = 0; i < targets.length; i++) {
        var target = parseFloat(targets[i]);
        var decimals = (targets[i].split('.')[1] || '').length;
        out += (target * ease(p)).toFixed(decimals) + (parts[i + 1] || '');
      }
      el.textContent = out;
      if (p < 1) requestAnimationFrame(frame);
      else el.textContent = original;
    }
    requestAnimationFrame(frame);
  }

  figures.forEach(function (el) {
    el.setAttribute('data-original', el.textContent.trim());
  });

  if (reduce || !('IntersectionObserver' in window)) return;

  var io = new IntersectionObserver(function (entries) {
    entries.forEach(function (entry) {
      if (entry.isIntersecting) {
        animate(entry.target);
        io.unobserve(entry.target);
      }
    });
  }, { threshold: 0.6 });

  figures.forEach(function (el) { io.observe(el); });
})();
