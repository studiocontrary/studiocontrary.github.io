/* Shannon Craver — portfolio interactions. Vanilla, no dependencies. */
(function () {
  "use strict";
  var header = document.querySelector(".site-header");
  var hero = document.querySelector("[data-hero]");
  var body = document.body;

  /* ---- header state (solid on scroll, light over dark hero) ---- */
  function onScroll() {
    var y = window.scrollY || window.pageYOffset;
    if (header) header.classList.toggle("scrolled", y > 24);
    if (header && hero) {
      var past = y > hero.offsetHeight - 80;
      header.classList.toggle("over-hero", !past);
    }
  }
  if (header && hero) header.classList.add("over-hero");
  onScroll();
  window.addEventListener("scroll", onScroll, { passive: true });
  window.addEventListener("resize", onScroll, { passive: true });

  /* ---- mobile menu ---- */
  var toggle = document.querySelector(".menu-toggle");
  if (toggle) {
    toggle.addEventListener("click", function () {
      body.classList.toggle("menu-open");
      toggle.setAttribute("aria-expanded", body.classList.contains("menu-open"));
    });
    document.querySelectorAll(".nav a").forEach(function (a) {
      a.addEventListener("click", function () { body.classList.remove("menu-open"); });
    });
  }

  /* ---- reveal on scroll ---- */
  var reveals = document.querySelectorAll(".reveal");
  if ("IntersectionObserver" in window && reveals.length) {
    var io = new IntersectionObserver(function (entries) {
      entries.forEach(function (e) {
        if (e.isIntersecting) { e.target.classList.add("in-view"); io.unobserve(e.target); }
      });
    }, { rootMargin: "0px 0px -8% 0px", threshold: 0.06 });
    reveals.forEach(function (el) { io.observe(el); });
  } else {
    reveals.forEach(function (el) { el.classList.add("in-view"); });
  }

  /* ---- lightbox (project spreads) ---- */
  var frames = Array.prototype.slice.call(document.querySelectorAll("[data-full]"));
  if (frames.length) {
    var lb = document.createElement("div");
    lb.className = "lb";
    lb.setAttribute("role", "dialog");
    lb.setAttribute("aria-modal", "true");
    lb.innerHTML =
      '<div class="lb-backdrop" data-close></div>' +
      '<div class="lb-count" aria-hidden="true"></div>' +
      '<button class="lb-close" aria-label="Close (Esc)">' + svg("M6 6l12 12M18 6L6 18") + "</button>" +
      '<button class="lb-nav lb-prev" aria-label="Previous">' + svg("M15 6l-6 6 6 6") + "</button>" +
      '<button class="lb-nav lb-next" aria-label="Next">' + svg("M9 6l6 6-6 6") + "</button>" +
      '<div class="lb-stage" data-close><img class="lb-img" alt=""></div>' +
      '<div class="lb-cap" aria-live="polite"></div>';
    document.body.appendChild(lb);

    var img = lb.querySelector(".lb-img");
    var cap = lb.querySelector(".lb-cap");
    var counter = lb.querySelector(".lb-count");
    var idx = 0, lastFocus = null;

    function svg(d) {
      return '<svg width="22" height="22" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.6" stroke-linecap="round"><path d="' + d + '"/></svg>';
    }
    function show(i) {
      idx = (i + frames.length) % frames.length;
      var f = frames[idx];
      img.src = f.getAttribute("data-full");
      img.alt = f.getAttribute("data-cap") || "";
      cap.textContent = f.getAttribute("data-cap") || "";
      counter.textContent = (idx + 1) + " / " + frames.length;
    }
    function open(i) {
      lastFocus = document.activeElement;
      show(i);
      lb.classList.add("open");
      body.style.overflow = "hidden";
      lb.querySelector(".lb-close").focus();
    }
    function close() {
      lb.classList.remove("open");
      body.style.overflow = "";
      img.src = "";
      if (lastFocus) lastFocus.focus();
    }
    frames.forEach(function (f, i) {
      f.addEventListener("click", function () { open(i); });
    });
    lb.querySelectorAll("[data-close]").forEach(function (el) {
      el.addEventListener("click", function (e) { if (e.target === el) close(); });
    });
    lb.querySelector(".lb-close").addEventListener("click", close);
    lb.querySelector(".lb-prev").addEventListener("click", function () { show(idx - 1); });
    lb.querySelector(".lb-next").addEventListener("click", function () { show(idx + 1); });
    document.addEventListener("keydown", function (e) {
      if (!lb.classList.contains("open")) return;
      if (e.key === "Escape") close();
      else if (e.key === "ArrowLeft") show(idx - 1);
      else if (e.key === "ArrowRight") show(idx + 1);
    });
  }

  /* ---- year ---- */
  var yr = document.querySelector("[data-year]");
  if (yr) yr.textContent = new Date().getFullYear();
})();
