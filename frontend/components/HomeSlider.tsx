"use client";

import Link from "next/link";
import { useEffect, useState } from "react";

import type { Banner } from "@/lib/types";

export function HomeSlider({
  banners,
  locale,
  orderLabel,
  moreLabel,
}: {
  banners: Banner[];
  locale: string;
  orderLabel: string;
  moreLabel: string;
}) {
  const [index, setIndex] = useState(0);
  const [showCvv, setShowCvv] = useState(false);

  useEffect(() => {
    if (banners.length < 2) return;
    const timer = window.setInterval(() => {
      setIndex((current) => (current + 1) % banners.length);
    }, 6000);
    return () => window.clearInterval(timer);
  }, [banners.length]);

  const item = banners[index];
  if (!item) return null;
  const href = item.href.startsWith("/") ? `/${locale}${item.href}` : `/${locale}/apply`;

  return (
    <section className={`home-slider tone-${index % 2}`}>
      <div className="home-wrap">
        <div className="slide-content">
          <h2>{item.title}</h2>
          <p>{item.subtitle}</p>
          <div className="slide-actions">
            <Link className="skew-btn" href={href}>
              <span>{orderLabel}</span>
            </Link>
            <Link className="more-link" href={href}>
              {moreLabel}
              <span aria-hidden="true"> →</span>
            </Link>
          </div>
        </div>
      </div>
      <div className="slide-art">
        <svg className="note note-a" viewBox="0 0 120 64">
          <defs>
            <linearGradient id="note-green" x1="0" y1="0" x2="1" y2="1">
              <stop offset="0" stopColor="#2f8f5b" />
              <stop offset="1" stopColor="#145c38" />
            </linearGradient>
          </defs>
          <rect width="120" height="64" rx="4" fill="url(#note-green)" />
          <rect x="6" y="6" width="108" height="52" rx="2" fill="none" stroke="rgba(216,255,232,.45)" strokeWidth="0.6" />
          <circle cx="86" cy="32" r="10" fill="none" stroke="rgba(216,255,232,.7)" strokeWidth="0.8" />
          <text x="10" y="22" fill="rgba(216,255,232,.9)" fontSize="9" fontFamily="Arial">100</text>
          <text x="78" y="36" fill="#d8ffe8" fontSize="11" fontFamily="Arial">₼</text>
        </svg>
        <svg className="note note-b" viewBox="0 0 120 64">
          <defs>
            <linearGradient id="note-gold" x1="0" y1="0" x2="1" y2="1">
              <stop offset="0" stopColor="#ffe56a" />
              <stop offset="1" stopColor="#e2aa00" />
            </linearGradient>
          </defs>
          <rect width="120" height="64" rx="4" fill="url(#note-gold)" />
          <rect x="6" y="6" width="108" height="52" rx="2" fill="none" stroke="rgba(22,22,22,.35)" strokeWidth="0.6" />
          <circle cx="86" cy="32" r="10" fill="none" stroke="rgba(22,22,22,.45)" strokeWidth="0.8" />
          <text x="10" y="22" fill="#161616" fontSize="9" fontFamily="Arial">50</text>
          <text x="78" y="36" fill="#161616" fontSize="11" fontFamily="Arial">₼</text>
        </svg>
        <div className="pay-card">
          <div className={`card-spin ${index % 2 === 0 ? "front" : "back"}`}>
          <div className="pay-face card-face front">
            <strong>Yelo Bank</strong>
            <span className="pay-chip" />
            <span className="pay-pan">0000 0000 0000 0000</span>
            <div className="pay-meta">
              <b>Cavidan Cavadov</b>
              <span>04/27</span>
            </div>
            <div className="pay-foot">
              <span className="pay-cvv">
                <em>{showCvv ? "991" : "•••"}</em>
                <button
                  type="button"
                  className="cvv-eye"
                  aria-label={showCvv ? "CVV gizlət" : "CVV göstər"}
                  onClick={() => setShowCvv((open) => !open)}
                >
                  <svg viewBox="0 0 24 24" aria-hidden="true">
                    <path d="M2 12s4-6 10-6 10 6 10 6-4 6-10 6S2 12 2 12z" fill="none" stroke="currentColor" strokeWidth="1.8" />
                    <circle cx="12" cy="12" r="2.4" fill="currentColor" />
                    {showCvv ? <path d="M5 5l14 14" fill="none" stroke="currentColor" strokeWidth="1.8" /> : null}
                  </svg>
                </button>
              </span>
              <i>Visa</i>
            </div>
          </div>
          <div className="pay-back card-face back">
            <span className="pay-stripe" />
            <div className="pay-sign">
              <span />
              <em>{showCvv ? "991" : "•••"}</em>
            </div>
          </div>
          </div>
        </div>
        <svg className="coin coin-a" viewBox="0 0 48 48">
          <defs>
            <radialGradient id="coin-gold" cx="35%" cy="35%" r="65%">
              <stop offset="0" stopColor="#fff1a8" />
              <stop offset="0.55" stopColor="#f0c200" />
              <stop offset="1" stopColor="#b8860b" />
            </radialGradient>
          </defs>
          <circle cx="24" cy="24" r="22" fill="url(#coin-gold)" />
          <circle cx="24" cy="24" r="17" fill="none" stroke="rgba(90,60,10,.45)" strokeWidth="0.8" />
          <text x="17" y="29" fill="#5c4308" fontSize="14" fontFamily="Arial">₼</text>
        </svg>
        <svg className="coin coin-b" viewBox="0 0 48 48">
          <defs>
            <radialGradient id="coin-silver" cx="35%" cy="35%" r="65%">
              <stop offset="0" stopColor="#ffffff" />
              <stop offset="0.5" stopColor="#d5d5d5" />
              <stop offset="1" stopColor="#8e8e8e" />
            </radialGradient>
          </defs>
          <circle cx="24" cy="24" r="22" fill="url(#coin-silver)" />
          <circle cx="24" cy="24" r="17" fill="none" stroke="rgba(40,40,40,.35)" strokeWidth="0.8" />
          <text x="17" y="29" fill="#3a3a3a" fontSize="14" fontFamily="Arial">₼</text>
        </svg>
      </div>
      <div className="slide-dots">
        {banners.map((banner, dot) => (
          <button
            key={banner.id}
            type="button"
            className={dot === index ? "on" : ""}
            aria-label={`${dot + 1}`}
            onClick={() => setIndex(dot)}
          />
        ))}
      </div>
    </section>
  );
}
