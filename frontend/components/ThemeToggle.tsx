"use client";

export function ThemeToggle() {
  function toggle() {
    const night = document.documentElement.dataset.theme !== "night";
    document.documentElement.dataset.theme = night ? "night" : "day";
    localStorage.setItem("yelo-theme", night ? "night" : "day");
  }

  return (
    <button type="button" className="theme-toggle" onClick={toggle} aria-label="Gecə / Gündüz">
      <svg className="theme-mark" viewBox="0 0 100 100" aria-hidden="true">
        <defs>
          <radialGradient id="daySky" cx="35%" cy="30%" r="70%">
            <stop offset="0%" stopColor="#7ad7ff" />
            <stop offset="100%" stopColor="#1d4ed8" />
          </radialGradient>
          <clipPath id="themeDisk">
            <circle cx="50" cy="50" r="49" />
          </clipPath>
        </defs>
        <g clipPath="url(#themeDisk)">
          <rect width="100" height="100" fill="#071433" />
          <g className="theme-stars" fill="#fff">
            <circle cx="78" cy="18" r="1.2" />
            <circle cx="88" cy="32" r="0.8" />
            <circle cx="70" cy="36" r="1" />
            <circle cx="84" cy="48" r="0.7" />
            <circle cx="62" cy="22" r="0.8" />
            <circle cx="22" cy="78" r="1" />
            <circle cx="14" cy="62" r="0.7" />
            <circle cx="30" cy="88" r="0.8" />
          </g>
          <path fill="url(#daySky)" d="M50 1a49 49 0 0 1 0 98 24.5 24.5 0 0 1 0-49 24.5 24.5 0 0 0 0-49" />
          <g className="theme-sun">
            <circle cx="32" cy="28" r="7" fill="#fff6c2" />
            <circle cx="32" cy="28" r="4" fill="#fff" />
            <g stroke="#fff6c2" strokeWidth="1.4" strokeLinecap="round">
              <path d="M32 16v4M32 36v4M20 28h4M40 28h4M23.5 19.5l2.8 2.8M37.7 33.7l2.8 2.8M40.5 19.5l-2.8 2.8M26.3 33.7l-2.8 2.8" />
            </g>
          </g>
          <path
            className="theme-moon"
            fill="#e8f4ff"
            d="M68 62a9 9 0 1 0 8 13 7 7 0 1 1-8-13z"
          />
        </g>
        <circle cx="50" cy="50" r="49" fill="none" stroke="rgba(255,255,255,.35)" strokeWidth="1" />
      </svg>
    </button>
  );
}
