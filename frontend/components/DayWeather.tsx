const drops = [
  { left: "3%", delay: "0s", duration: "1.4s" },
  { left: "9%", delay: "0.4s", duration: "1.7s" },
  { left: "16%", delay: "0.9s", duration: "1.3s" },
  { left: "23%", delay: "0.2s", duration: "1.8s" },
  { left: "31%", delay: "1.1s", duration: "1.5s" },
  { left: "38%", delay: "0.6s", duration: "1.2s" },
  { left: "46%", delay: "0.1s", duration: "1.6s" },
  { left: "53%", delay: "0.8s", duration: "1.4s" },
  { left: "61%", delay: "1.3s", duration: "1.7s" },
  { left: "69%", delay: "0.3s", duration: "1.3s" },
  { left: "76%", delay: "0.7s", duration: "1.5s" },
  { left: "84%", delay: "1s", duration: "1.2s" },
  { left: "92%", delay: "0.5s", duration: "1.8s" },
  { left: "14%", delay: "1.5s", duration: "1.6s" },
  { left: "57%", delay: "1.6s", duration: "1.4s" },
];

const leaves = [
  { left: "4%", size: 22, delay: "0s", duration: "11s", color: "#e25b2a" },
  { left: "12%", size: 16, delay: "1.2s", duration: "9s", color: "#f0a202" },
  { left: "19%", size: 26, delay: "2.8s", duration: "13s", color: "#c2410c" },
  { left: "27%", size: 18, delay: "0.5s", duration: "10s", color: "#ca8a04" },
  { left: "35%", size: 24, delay: "3.4s", duration: "12s", color: "#b45309" },
  { left: "43%", size: 16, delay: "1.8s", duration: "8s", color: "#ea580c" },
  { left: "51%", size: 28, delay: "4.2s", duration: "14s", color: "#d97706" },
  { left: "58%", size: 18, delay: "0.8s", duration: "9s", color: "#9a3412" },
  { left: "66%", size: 22, delay: "2.2s", duration: "11s", color: "#eab308" },
  { left: "74%", size: 16, delay: "5s", duration: "10s", color: "#c2410c" },
  { left: "82%", size: 26, delay: "1.6s", duration: "13s", color: "#f59e0b" },
  { left: "90%", size: 18, delay: "3.8s", duration: "9s", color: "#b45309" },
  { left: "8%", size: 20, delay: "6s", duration: "15s", color: "#ea580c" },
  { left: "47%", size: 20, delay: "5.4s", duration: "12s", color: "#e25b2a" },
];

export function DayWeather() {
  return (
    <div className="day-fall" aria-hidden="true">
      {drops.map((drop) => (
        <i
          key={drop.left}
          className="rain"
          style={{ left: drop.left, animationDelay: drop.delay, animationDuration: drop.duration }}
        />
      ))}
      {leaves.map((leaf) => (
        <span
          key={leaf.left}
          className="leaf"
          style={{
            left: leaf.left,
            color: leaf.color,
            width: leaf.size,
            height: leaf.size,
            animationDelay: leaf.delay,
            animationDuration: leaf.duration,
          }}
        >
          <svg viewBox="0 0 32 32">
            <path d="M16 3c-1 7-8 11-12 12 5 2 9 8 10 15 1-7 5-13 10-15-4-1-11-5-8-12z" />
            <path d="M16 10v16" fill="none" stroke="currentColor" strokeWidth="1.4" />
          </svg>
        </span>
      ))}
    </div>
  );
}
