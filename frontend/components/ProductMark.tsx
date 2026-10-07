export function ProductMark({ kind, slug, detail }: { kind: string; slug?: string; detail?: boolean }) {
  const cash = (slug ?? "").includes("cash");
  if (kind === "card" && detail) {
    return (
      <svg viewBox="0 0 160 100" aria-hidden="true">
        <defs>
          <linearGradient id="mark-face" x1="0" y1="0" x2="1" y2="1">
            <stop offset="0" stopColor={cash ? "#2c2c2c" : "#ffe56a"} />
            <stop offset="1" stopColor={cash ? "#0d0d0d" : "#e2aa00"} />
          </linearGradient>
          <linearGradient id="mark-chip" x1="0" y1="0" x2="0" y2="1">
            <stop offset="0" stopColor="#f6e7b0" />
            <stop offset="1" stopColor="#8d6a22" />
          </linearGradient>
        </defs>
        <rect width="160" height="100" rx="8" fill="url(#mark-face)" />
        <rect x="12" y="28" width="22" height="16" rx="3" fill="url(#mark-chip)" />
        <path d="M12 36h22M23 28v16" stroke="#8a6420" strokeWidth="0.6" />
        <path d="M128 22c5 3 5 10 0 13M134 18c8 5 8 16 0 21" fill="none" stroke={cash ? "#f5c400" : "#161616"} strokeWidth="1.3" strokeLinecap="round" />
        <text x="12" y="78" fill={cash ? "#fff" : "#161616"} fontSize="11" fontFamily="Arial">
          0000 0000 0000 0000
        </text>
        <text x="12" y="92" fill={cash ? "#f5c400" : "#161616"} fontSize="10" fontFamily="Arial">
          Cavidan Cavadov
        </text>
      </svg>
    );
  }
  if (kind === "card") {
    return (
      <svg viewBox="0 0 88 56" aria-hidden="true">
        <rect width="88" height="56" rx="6" fill={cash ? "#1a1a1a" : "#f0c200"} />
        <rect x="8" y="16" width="14" height="10" rx="2" fill="#d4b15a" />
        <rect x="26" y="34" width="28" height="2" rx="1" fill={cash ? "rgba(255,255,255,.7)" : "rgba(22,22,22,.7)"} />
        {cash ? (
          <text x="58" y="22" fill="#f5c400" fontSize="11" fontFamily="Arial" fontWeight="700">
            2%
          </text>
        ) : null}
      </svg>
    );
  }
  if (kind === "deposit") {
    return (
      <svg viewBox="0 0 88 56" aria-hidden="true">
        <rect x="18" y="20" width="52" height="28" rx="6" fill="#f5c400" />
        <rect x="30" y="8" width="28" height="16" rx="8" fill="#161616" />
        <circle cx="44" cy="34" r="6" fill="#161616" />
      </svg>
    );
  }
  return (
    <svg viewBox="0 0 88 56" aria-hidden="true">
      <rect x="8" y="8" width="40" height="40" rx="6" fill="#161616" />
      <circle cx="62" cy="34" r="14" fill="#f5c400" />
      <text x="56" y="39" fill="#161616" fontSize="14" fontFamily="Arial" fontWeight="700">
        ₼
      </text>
    </svg>
  );
}
