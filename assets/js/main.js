// AuditingAI - Main JavaScript
// Mobile Navigation Toggle
document.addEventListener('DOMContentLoaded', () => {
  const mobileToggle = document.getElementById('mobileToggle');
  const navLinks = document.getElementById('navLinks');

  if (mobileToggle && navLinks) {
    mobileToggle.addEventListener('click', () => {
      const isExpanded = navLinks.classList.toggle('active');
      mobileToggle.classList.toggle('active');
      mobileToggle.setAttribute('aria-expanded', isExpanded);
    });

    // Close menu when clicking a link
    navLinks.querySelectorAll('a').forEach(link => {
      link.addEventListener('click', () => {
        navLinks.classList.remove('active');
        mobileToggle.classList.remove('active');
        mobileToggle.setAttribute('aria-expanded', 'false');
      });
    });
  }

  // Navbar scroll effect
  const navbar = document.getElementById('navbar');

  if (navbar) {
    window.addEventListener('scroll', () => {
      if (window.pageYOffset > 100) {
        navbar.classList.add('scrolled');
      } else {
        navbar.classList.remove('scrolled');
      }
    });
  }

  // Reveal on scroll animation
  const revealElements = document.querySelectorAll('.reveal');

  const revealOnScroll = () => {
    revealElements.forEach(element => {
      const elementTop = element.getBoundingClientRect().top;
      const windowHeight = window.innerHeight;

      if (elementTop < windowHeight - 100) {
        element.classList.add('active');
      }
    });
  };

  window.addEventListener('scroll', revealOnScroll);
  revealOnScroll(); // Initial check

  // Smooth scroll for anchor links
  document.querySelectorAll('a[href^="#"]').forEach(anchor => {
    anchor.addEventListener('click', function(e) {
      const href = this.getAttribute('href');
      if (href !== '#' && document.querySelector(href)) {
        e.preventDefault();
        document.querySelector(href).scrollIntoView({
          behavior: 'smooth',
          block: 'start'
        });
      }
    });
  });

  // Form validation feedback
  const contactForm = document.querySelector('.contact-form');
  if (contactForm) {
    contactForm.addEventListener('submit', function(e) {
      const email = this.querySelector('input[type="email"]');
      const message = this.querySelector('textarea');

      if (email && !email.value.includes('@')) {
        e.preventDefault();
        alert('Please enter a valid email address.');
        return;
      }

      if (message && message.value.length < 10) {
        e.preventDefault();
        alert('Please provide more details about your inquiry.');
        return;
      }
    });
  }
});

// Console branding
console.log('%cAudit the Algorithm', 'color: #B8860B; font-size: 24px; font-weight: bold;');
console.log('%cAI Governance Consulting for Financial Services', 'color: #CED4DA; font-size: 14px;');
console.log('%chttps://auditingai.github.io', 'color: #4A90A4; font-size: 12px;');
