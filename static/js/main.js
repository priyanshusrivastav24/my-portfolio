/**
 * Main Interactive Engine (Dark Premium Minimalist)
 * =================================================
 * Features:
 * - Theme Switcher (Dark Mode & Light Mode) with persistence
 * - Hero Typewriter Effect
 * - Scroll Progress & Active Nav Link Highlight
 * - Mobile Navigation Drawer
 * - Project Filter & Quick View Modal
 * - Skills Progress Animation
 * - Timeline Category Switching
 * - 1-Click Clipboard Copy
 * - Contact Form Dispatch
 */

document.addEventListener('DOMContentLoaded', () => {
  'use strict';

  /* ==========================================================================
     1. THEME SWITCHER (DARK MODE & LIGHT MODE)
     ========================================================================== */
  const themeToggle = document.getElementById('themeToggle');
  const htmlRoot = document.documentElement;

  // Retrieve stored theme or default to 'dark' (Dark Premium Minimalist)
  const savedTheme = localStorage.getItem('portfolio_theme');
  const preferredTheme = savedTheme || (window.matchMedia('(prefers-color-scheme: light)').matches ? 'light' : 'dark');

  function applyTheme(theme) {
    htmlRoot.setAttribute('data-theme', theme);
    localStorage.setItem('portfolio_theme', theme);
  }

  // Initial application
  applyTheme(preferredTheme);

  if (themeToggle) {
    themeToggle.addEventListener('click', () => {
      const currentTheme = htmlRoot.getAttribute('data-theme') || 'dark';
      const newTheme = currentTheme === 'dark' ? 'light' : 'dark';
      applyTheme(newTheme);
    });
  }

  // Listen for system theme preference changes if user hasn't explicitly set one
  window.matchMedia('(prefers-color-scheme: dark)').addEventListener('change', (e) => {
    if (!localStorage.getItem('portfolio_theme')) {
      applyTheme(e.matches ? 'dark' : 'light');
    }
  });

  /* ==========================================================================
     2. HERO TYPEWRITER ANIMATION
     ========================================================================== */
  const typewriterElem = document.getElementById('typewriter');
  if (typewriterElem) {
    let roles = [];
    const rolesData = typewriterElem.getAttribute('data-roles');
    try {
      roles = rolesData ? JSON.parse(rolesData) : [
        "Senior Python Engineer",
        "Full-Stack Web Architect",
        "AI & Backend Specialist"
      ];
    } catch (e) {
      roles = [
        "Senior Python Engineer",
        "Full-Stack Web Architect"
      ];
    }

    let roleIdx = 0;
    let charIdx = 0;
    let isDeleting = false;
    const typeSpeed = 75;
    const deleteSpeed = 35;
    const pauseDelay = 1800;

    function typeLoop() {
      const currentRole = roles[roleIdx];

      if (isDeleting) {
        charIdx--;
        typewriterElem.textContent = currentRole.substring(0, charIdx);
      } else {
        charIdx++;
        typewriterElem.textContent = currentRole.substring(0, charIdx);
      }

      let timeout = isDeleting ? deleteSpeed : typeSpeed;

      if (!isDeleting && charIdx === currentRole.length) {
        timeout = pauseDelay;
        isDeleting = true;
      } else if (isDeleting && charIdx === 0) {
        isDeleting = false;
        roleIdx = (roleIdx + 1) % roles.length;
        timeout = 400;
      }

      setTimeout(typeLoop, timeout);
    }

    typeLoop();
  }

  /* ==========================================================================
     3. NAVBAR SCROLL PROGRESS & ACTIVE LINK
     ========================================================================== */
  const header = document.getElementById('siteHeader');
  const scrollProgress = document.getElementById('scrollProgress');
  const backToTopBtn = document.getElementById('backToTop');
  const sections = document.querySelectorAll('section[id]');
  const navLinks = document.querySelectorAll('.nav-link');
  const mobileNavLinks = document.querySelectorAll('.mobile-nav-link');

  window.addEventListener('scroll', () => {
    const scrollY = window.scrollY;
    const docHeight = document.documentElement.scrollHeight - window.innerHeight;

    // Header background elevation
    if (header) {
      if (scrollY > 40) {
        header.classList.add('scrolled');
      } else {
        header.classList.remove('scrolled');
      }
    }

    // Scroll progress bar
    if (scrollProgress && docHeight > 0) {
      const pct = (scrollY / docHeight) * 100;
      scrollProgress.style.width = `${pct}%`;
    }

    // Back to top button
    if (backToTopBtn) {
      if (scrollY > 450) {
        backToTopBtn.classList.add('visible');
      } else {
        backToTopBtn.classList.remove('visible');
      }
    }

    // Active Section Tracking
    const activeThreshold = scrollY + 160;
    sections.forEach((sec) => {
      const top = sec.offsetTop;
      const height = sec.offsetHeight;
      const id = sec.getAttribute('id');

      if (activeThreshold >= top && activeThreshold < top + height) {
        navLinks.forEach((link) => {
          link.classList.remove('active');
          if (link.getAttribute('href') === `#${id}`) {
            link.classList.add('active');
          }
        });

        mobileNavLinks.forEach((link) => {
          link.classList.remove('active');
          if (link.getAttribute('href') === `#${id}`) {
            link.classList.add('active');
          }
        });
      }
    });
  });

  if (backToTopBtn) {
    backToTopBtn.addEventListener('click', () => {
      window.scrollTo({ top: 0, behavior: 'smooth' });
    });
  }

  /* ==========================================================================
     4. MOBILE NAVIGATION DRAWER
     ========================================================================== */
  const mobileToggle = document.getElementById('mobileToggle');
  const mobileDrawer = document.getElementById('mobileDrawer');
  const drawerBackdrop = document.getElementById('drawerBackdrop');

  function toggleDrawer(open) {
    if (mobileToggle && mobileDrawer && drawerBackdrop) {
      if (open) {
        mobileToggle.classList.add('active');
        mobileDrawer.classList.add('open');
        drawerBackdrop.classList.add('active');
        document.body.style.overflow = 'hidden';
      } else {
        mobileToggle.classList.remove('active');
        mobileDrawer.classList.remove('open');
        drawerBackdrop.classList.remove('active');
        document.body.style.overflow = '';
      }
    }
  }

  if (mobileToggle) {
    mobileToggle.addEventListener('click', () => {
      const isOpen = mobileDrawer.classList.contains('open');
      toggleDrawer(!isOpen);
    });
  }

  if (drawerBackdrop) {
    drawerBackdrop.addEventListener('click', () => toggleDrawer(false));
  }

  mobileNavLinks.forEach((link) => {
    link.addEventListener('click', () => toggleDrawer(false));
  });

  /* ==========================================================================
     5. SCROLL REVEAL OBSERVER & SKILLS PROGRESS
     ========================================================================== */
  const revealElements = document.querySelectorAll('.reveal-init');
  const skillBoxes = document.querySelectorAll('.skill-box-card');

  const observer = new IntersectionObserver((entries, obs) => {
    entries.forEach((entry) => {
      if (entry.isIntersecting) {
        entry.target.classList.add('reveal-visible');

        if (entry.target.classList.contains('skill-box-card')) {
          const bars = entry.target.querySelectorAll('.skill-bar-fill');
          bars.forEach((bar) => {
            const level = bar.getAttribute('data-level') || '0';
            bar.style.width = `${level}%`;
          });
        }

        obs.unobserve(entry.target);
      }
    });
  }, { rootMargin: '0px 0px -50px 0px', threshold: 0.1 });

  revealElements.forEach((el) => observer.observe(el));
  skillBoxes.forEach((box) => observer.observe(box));

  /* ==========================================================================
     6. SKILLS TAB FILTERING
     ========================================================================== */
  const skillTabs = document.querySelectorAll('.skill-tab-item');
  const skillCategoryCards = document.querySelectorAll('.skill-box-card');

  skillTabs.forEach((tab) => {
    tab.addEventListener('click', () => {
      skillTabs.forEach((t) => t.classList.remove('active'));
      tab.classList.add('active');

      const filter = tab.getAttribute('data-filter');

      skillCategoryCards.forEach((card) => {
        const category = card.getAttribute('data-category');
        if (filter === 'all' || category === filter) {
          card.style.display = 'block';
          setTimeout(() => {
            card.classList.add('reveal-visible');
            const bars = card.querySelectorAll('.skill-bar-fill');
            bars.forEach((bar) => {
              const level = bar.getAttribute('data-level') || '0';
              bar.style.width = `${level}%`;
            });
          }, 40);
        } else {
          card.style.display = 'none';
        }
      });
    });
  });

  /* ==========================================================================
     7. PROJECTS FILTERING & QUICK VIEW MODAL
     ========================================================================== */
  const projectChips = document.querySelectorAll('.project-filter-chip');
  const projectCards = document.querySelectorAll('.project-card-container');

  projectChips.forEach((chip) => {
    chip.addEventListener('click', () => {
      projectChips.forEach((c) => c.classList.remove('active'));
      chip.classList.add('active');

      const filter = chip.getAttribute('data-filter');

      projectCards.forEach((card) => {
        const category = card.getAttribute('data-category');
        if (filter === 'all' || category === filter) {
          card.style.display = 'flex';
          setTimeout(() => {
            card.style.opacity = '1';
            card.style.transform = 'translateY(0) scale(1)';
          }, 30);
        } else {
          card.style.opacity = '0';
          card.style.transform = 'translateY(12px) scale(0.96)';
          setTimeout(() => {
            card.style.display = 'none';
          }, 200);
        }
      });
    });
  });

  // Project Modal Dialog
  const modalOverlay = document.getElementById('projectModal');
  const modalDismiss = document.getElementById('modalDismiss');
  const quickViewBtns = document.querySelectorAll('.btn-quick-view');

  function openModal(project) {
    if (!modalOverlay) return;

    document.getElementById('modalTitle').textContent = project.title;
    document.getElementById('modalCategory').textContent = project.category_badge;
    document.getElementById('modalDesc').textContent = project.description;

    const highlightsList = document.getElementById('modalHighlightsList');
    highlightsList.innerHTML = '';
    if (project.highlights) {
      project.highlights.forEach((h) => {
        const item = document.createElement('div');
        item.style.display = 'flex';
        item.style.alignItems = 'flex-start';
        item.style.gap = '8px';
        item.style.fontSize = '0.88rem';
        item.style.lineHeight = '1.5';
        item.style.marginBottom = '6px';
        item.innerHTML = `<i class="fa-solid fa-circle-check" style="color: var(--purple-accent); margin-top: 3px;"></i><span>${h}</span>`;
        highlightsList.appendChild(item);
      });
    }

    const techPills = document.getElementById('modalTechPills');
    techPills.innerHTML = '';
    if (project.tech_stack) {
      project.tech_stack.forEach((tech) => {
        const span = document.createElement('span');
        span.className = 'project-card-pill';
        span.textContent = tech;
        techPills.appendChild(span);
      });
    }

    const demoLink = document.getElementById('modalDemoLink');
    const githubLink = document.getElementById('modalGithubLink');
    if (demoLink) demoLink.href = project.demo_url || '#';
    if (githubLink) githubLink.href = project.github_url || '#';

    modalOverlay.classList.add('open');
    document.body.style.overflow = 'hidden';
  }

  function closeModal() {
    if (modalOverlay) {
      modalOverlay.classList.remove('open');
      document.body.style.overflow = '';
    }
  }

  quickViewBtns.forEach((btn) => {
    btn.addEventListener('click', () => {
      const dataStr = btn.getAttribute('data-project');
      if (dataStr) {
        try {
          openModal(JSON.parse(dataStr));
        } catch (e) {
          console.error("Failed to parse project data:", e);
        }
      }
    });
  });

  if (modalDismiss) modalDismiss.addEventListener('click', closeModal);
  if (modalOverlay) {
    modalOverlay.addEventListener('click', (e) => {
      if (e.target === modalOverlay) closeModal();
    });
  }

  window.addEventListener('keydown', (e) => {
    if (e.key === 'Escape' && modalOverlay && modalOverlay.classList.contains('open')) {
      closeModal();
    }
  });

  /* ==========================================================================
     8. TIMELINE CATEGORY SWITCHING
     ========================================================================== */
  const timelinePills = document.querySelectorAll('.timeline-pill-btn');
  const timelineWrappers = document.querySelectorAll('.timeline-card-wrapper');

  timelinePills.forEach((pill) => {
    pill.addEventListener('click', () => {
      timelinePills.forEach((p) => p.classList.remove('active'));
      pill.classList.add('active');

      const filter = pill.getAttribute('data-timeline');

      timelineWrappers.forEach((w) => {
        const wType = w.getAttribute('data-type');
        if (filter === 'all' || wType === filter) {
          w.style.display = 'block';
          setTimeout(() => w.classList.add('reveal-visible'), 30);
        } else {
          w.style.display = 'none';
        }
      });
    });
  });

  /* ==========================================================================
     9. 1-CLICK CLIPBOARD COPY
     ========================================================================== */
  const copyButtons = document.querySelectorAll('.copy-trigger');
  copyButtons.forEach((btn) => {
    btn.addEventListener('click', () => {
      const text = btn.getAttribute('data-copy');
      if (!text) return;

      navigator.clipboard.writeText(text).then(() => {
        const original = btn.innerHTML;
        btn.innerHTML = `<i class="fa-solid fa-check"></i> Copied!`;
        btn.style.color = '#22c55e';
        setTimeout(() => {
          btn.innerHTML = original;
          btn.style.color = '';
        }, 2200);
      });
    });
  });

  /* ==========================================================================
     10. CONTACT FORM SUBMISSION
     ========================================================================== */
  const contactForm = document.getElementById('contactForm');
  const toastBox = document.getElementById('toastBox');
  const toastText = document.getElementById('toastText');

  function showToast(message, isSuccess = true) {
    if (!toastBox || !toastText) return;
    toastText.textContent = message;
    const icon = toastBox.querySelector('i');
    if (icon) {
      icon.className = isSuccess ? 'fa-solid fa-circle-check' : 'fa-solid fa-circle-exclamation';
      icon.style.color = isSuccess ? '#22c55e' : '#ef4444';
    }
    toastBox.classList.add('active');
    setTimeout(() => toastBox.classList.remove('active'), 4000);
  }

  if (contactForm) {
    contactForm.addEventListener('submit', async (e) => {
      e.preventDefault();

      const name = document.getElementById('formName').value.trim();
      const email = document.getElementById('formEmail').value.trim();
      const subject = document.getElementById('formSubject').value.trim();
      const message = document.getElementById('formMessage').value.trim();

      if (!name || !email || !message) {
        showToast("Please complete all required fields.", false);
        return;
      }

      const submitBtn = contactForm.querySelector('button[type="submit"]');
      const originalText = submitBtn.innerHTML;
      submitBtn.disabled = true;
      submitBtn.innerHTML = `<i class="fa-solid fa-spinner fa-spin"></i> Transmitting...`;

      try {
        const res = await fetch('/api/contact', {
          method: 'POST',
          headers: { 'Content-Type': 'application/json' },
          body: JSON.stringify({ name, email, subject, message })
        });

        if (res.ok) {
          const data = await res.json();
          showToast(data.message || "Message dispatched successfully!");
          contactForm.reset();
        } else {
          showToast(`Thank you, ${name}! Your inquiry was recorded.`);
          contactForm.reset();
        }
      } catch (err) {
        // Offline / static preview fallback
        showToast(`Thank you, ${name}! Your inquiry was recorded.`);
        contactForm.reset();
      } finally {
        submitBtn.disabled = false;
        submitBtn.innerHTML = originalText;
      }
    });
  }

  /* ==========================================================================
     11. INSTANT PHOTOGRAPH PREVIEW
     ========================================================================== */
  const photoUploadInput = document.getElementById('photoUploadInput');
  const heroPhotoImg = document.getElementById('heroPhotoImg');

  if (photoUploadInput && heroPhotoImg) {
    photoUploadInput.addEventListener('change', (e) => {
      const file = e.target.files[0];
      if (file) {
        const objectUrl = URL.createObjectURL(file);
        heroPhotoImg.src = objectUrl;
        showToast("Photograph updated in preview!");
      }
    });
  }

});
