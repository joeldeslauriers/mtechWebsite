/* ============================================================
   GROUPE MTECH INC. — Global JS
   ============================================================ */

(function () {
  'use strict';

  /* ── Bloquer le rebond horizontal iOS Safari ──────────────── */
  let _tx = 0, _ty = 0;
  document.addEventListener('touchstart', e => {
    _tx = e.touches[0].clientX;
    _ty = e.touches[0].clientY;
  }, { passive: true });
  document.addEventListener('touchmove', e => {
    const dx = Math.abs(e.touches[0].clientX - _tx);
    const dy = Math.abs(e.touches[0].clientY - _ty);
    if (dx > dy) e.preventDefault();
  }, { passive: false });

  /* ── Navbar scroll behaviour ──────────────────────────────── */
  const navbar = document.getElementById('navbar');
  if (navbar) {
    const onScroll = () => {
      navbar.classList.toggle('scrolled', window.scrollY > 80);
    };
    window.addEventListener('scroll', onScroll, { passive: true });
    onScroll();
  }

  /* ── Mobile hamburger menu ────────────────────────────────── */
  const hamburger = document.querySelector('.hamburger');
  const mobileOverlay = document.querySelector('.nav-mobile-overlay');

  if (hamburger && mobileOverlay) {
    const openMenu = () => {
      hamburger.classList.add('open');
      mobileOverlay.classList.add('open');
      document.body.style.overflow = 'hidden';
    };
    const closeMenu = () => {
      hamburger.classList.remove('open');
      mobileOverlay.classList.remove('open');
      document.body.style.overflow = '';
    };
    hamburger.addEventListener('click', () => {
      hamburger.classList.contains('open') ? closeMenu() : openMenu();
    });
    mobileOverlay.querySelectorAll('a').forEach(link => {
      link.addEventListener('click', closeMenu);
    });
    document.addEventListener('keydown', e => {
      if (e.key === 'Escape') closeMenu();
    });
  }

  /* ── Active nav link ──────────────────────────────────────── */
  const path = window.location.pathname.split('/').pop() || 'index.html';
  document.querySelectorAll('a[data-nav]').forEach(link => {
    const href = link.getAttribute('href');
    if (href === path || (path === '' && href === 'index.html')) {
      link.classList.add('active');
    }
  });

  /* ── Smooth scroll for anchor links ──────────────────────── */
  document.querySelectorAll('a[href^="#"]').forEach(anchor => {
    anchor.addEventListener('click', function (e) {
      const target = document.querySelector(this.getAttribute('href'));
      if (target) {
        e.preventDefault();
        const offset = 90;
        const top = target.getBoundingClientRect().top + window.scrollY - offset;
        window.scrollTo({ top, behavior: 'smooth' });
      }
    });
  });

  /* ── IntersectionObserver — fade/slide animations ─────────── */
  const animObserver = new IntersectionObserver((entries) => {
    entries.forEach(entry => {
      if (entry.isIntersecting) {
        entry.target.classList.add('visible');
        animObserver.unobserve(entry.target);
      }
    });
  }, { threshold: 0.12, rootMargin: '0px 0px -40px 0px' });

  document.querySelectorAll('.animate-in').forEach(el => animObserver.observe(el));

  /* ── Animated counters (index.html only) ──────────────────── */
  function animateCounter(el) {
    const raw = el.getAttribute('data-counter');
    const isFloat = raw.includes('.');
    const target = parseFloat(raw);
    const suffix = el.getAttribute('data-suffix') || '';
    const prefix = el.getAttribute('data-prefix') || '';
    const duration = 1800;
    const start = performance.now();

    const tick = (now) => {
      const elapsed = now - start;
      const progress = Math.min(elapsed / duration, 1);
      const eased = 1 - Math.pow(1 - progress, 3); // ease-out cubic
      const current = eased * target;
      el.textContent = prefix + (isFloat ? current.toFixed(1) : Math.floor(current)) + suffix;
      if (progress < 1) requestAnimationFrame(tick);
    };
    requestAnimationFrame(tick);
  }

  const counterEls = document.querySelectorAll('[data-counter]');
  if (counterEls.length) {
    const counterObserver = new IntersectionObserver((entries) => {
      entries.forEach(entry => {
        if (entry.isIntersecting) {
          animateCounter(entry.target);
          counterObserver.unobserve(entry.target);
        }
      });
    }, { threshold: 0.5 });
    counterEls.forEach(el => counterObserver.observe(el));
  }

  /* ── Active section highlight in nav (scroll spy) ─────────── */
  const sections = document.querySelectorAll('section[id]');
  const navAnchors = document.querySelectorAll('.nav-links a[href^="#"]');
  if (sections.length && navAnchors.length) {
    const spyObserver = new IntersectionObserver((entries) => {
      entries.forEach(entry => {
        if (entry.isIntersecting) {
          const id = entry.target.id;
          navAnchors.forEach(a => {
            a.classList.toggle('active', a.getAttribute('href') === '#' + id);
          });
        }
      });
    }, { threshold: 0.4 });
    sections.forEach(s => spyObserver.observe(s));
  }

})();
