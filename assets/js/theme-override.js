(function () {
  const btn = document.getElementById("theme-toggle");
  const icon = document.getElementById("theme-icon");
  if (!btn) return;

  function apply(theme) {
    document.documentElement.setAttribute("data-theme", theme);
    if (icon) {
      icon.classList.toggle("fa-sun", theme === "dark"); // in dark mostra "sun" per tornare a light
      icon.classList.toggle("fa-moon", theme !== "dark");
    }
  }

  // Ensure icon is consistent on load
  const current = document.documentElement.getAttribute("data-theme") || "light";
  apply(current);

  btn.addEventListener("click", (e) => {
    e.preventDefault();
    const now = document.documentElement.getAttribute("data-theme") === "dark" ? "light" : "dark";
    localStorage.setItem("theme", now);
    apply(now);
  });
})();