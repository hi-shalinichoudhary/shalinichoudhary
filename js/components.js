/* Shared component script: count-up for .sc-stat numbers.
   Markup: <span data-count="65" data-prefix="+" data-suffix="%" data-decimals="0" aria-hidden="true">+65%</span>
   The final value is always in the HTML. Under prefers-reduced-motion, or without
   IntersectionObserver, nothing is animated and the final value simply stays. */
(function () {
  'use strict';

  var nodes = document.querySelectorAll('[data-count]');
  if (!nodes.length) return;

  var reduce = window.matchMedia('(prefers-reduced-motion: reduce)').matches;
  if (reduce || !('IntersectionObserver' in window)) return;

  function run(el) {
    var target = parseFloat(el.getAttribute('data-count'));
    var prefix = el.getAttribute('data-prefix') || '';
    var suffix = el.getAttribute('data-suffix') || '';
    var decimals = parseInt(el.getAttribute('data-decimals') || '0', 10);
    var final = el.textContent;
    var start = null;
    var duration = 1400;

    // Lock the width so the changing digits cannot shift the layout.
    el.style.display = 'inline-block';
    el.style.minWidth = el.getBoundingClientRect().width + 'px';

    function frame(ts) {
      if (start === null) start = ts;
      var p = Math.min((ts - start) / duration, 1);
      var eased = 1 - Math.pow(1 - p, 3);
      el.textContent = prefix + (target * eased).toFixed(decimals) + suffix;
      if (p < 1) {
        requestAnimationFrame(frame);
      } else {
        el.textContent = final;
      }
    }
    requestAnimationFrame(frame);
  }

  var io = new IntersectionObserver(function (entries) {
    entries.forEach(function (entry) {
      if (entry.isIntersecting) {
        io.unobserve(entry.target);
        run(entry.target);
      }
    });
  }, { threshold: 0.6 });

  nodes.forEach(function (el) { io.observe(el); });
})();

(function () {
  'use strict';
  var portraits = document.querySelectorAll('.hero-editorial-portrait');
  portraits.forEach(function (frame) {
    if (!frame.querySelector('.portrait-alt')) return;
    frame.addEventListener('click', function () {
      frame.classList.toggle('is-alt');
    });
    frame.addEventListener('keydown', function (e) {
      if (e.key === 'Enter' || e.key === ' ') {
        e.preventDefault();
        frame.classList.toggle('is-alt');
      }
    });
  });
})();

/* Accessible keyboard-operable tabs for [role="tablist"] */
(function () {
  'use strict';
  var tablists = document.querySelectorAll('[role="tablist"]');
  tablists.forEach(function (tablist) {
    var tabs = Array.prototype.slice.call(tablist.querySelectorAll('[role="tab"]'));
    if (!tabs.length) return;

    function activateTab(nextTab, moveFocus) {
      tabs.forEach(function (tab) {
        var selected = tab === nextTab;
        tab.setAttribute('aria-selected', selected ? 'true' : 'false');
        tab.setAttribute('tabindex', selected ? '0' : '-1');
        var panelId = tab.getAttribute('aria-controls');
        var panel = panelId ? document.getElementById(panelId) : null;
        if (panel) {
          if (selected) {
            panel.removeAttribute('hidden');
          } else {
            panel.setAttribute('hidden', '');
          }
        }
      });
      if (moveFocus) {
        nextTab.focus();
      }
    }

    tabs.forEach(function (tab, idx) {
      tab.addEventListener('click', function () {
        activateTab(tab, false);
      });

      tab.addEventListener('keydown', function (e) {
        var targetIdx = null;
        if (e.key === 'ArrowRight' || e.key === 'ArrowDown') {
          targetIdx = (idx + 1) % tabs.length;
        } else if (e.key === 'ArrowLeft' || e.key === 'ArrowUp') {
          targetIdx = (idx - 1 + tabs.length) % tabs.length;
        } else if (e.key === 'Home') {
          targetIdx = 0;
        } else if (e.key === 'End') {
          targetIdx = tabs.length - 1;
        }
        if (targetIdx !== null) {
          e.preventDefault();
          activateTab(tabs[targetIdx], true);
        }
      });
    });
  });
})();
