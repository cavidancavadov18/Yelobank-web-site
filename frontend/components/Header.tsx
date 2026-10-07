"use client";

import Link from "next/link";
import { usePathname } from "next/navigation";
import { useState } from "react";

import { ThemeToggle } from "@/components/ThemeToggle";
import { copy, locales, type Locale } from "@/lib/i18n";

export function Header({ locale }: { locale: Locale }) {
  const t = copy(locale);
  const pathname = usePathname();
  const [open, setOpen] = useState(false);
  const links = [
    { href: `/${locale}`, label: t.home, exact: true },
    { href: `/${locale}/cards`, label: t.cards },
    { href: `/${locale}/loans`, label: t.loans },
    { href: `/${locale}/deposits`, label: t.deposits },
    { href: `/${locale}/cashback`, label: t.cashback },
    { href: `/${locale}/news`, label: t.news },
    { href: `/${locale}/branches`, label: t.branches },
    { href: `/${locale}/apply`, label: t.apply },
  ];

  function swap(next: Locale) {
    const parts = pathname.split("/");
    parts[1] = next;
    return parts.join("/") || `/${next}`;
  }

  const biz = pathname.includes("/business");
  const bankSection = ["/cards", "/loans", "/deposits", "/cashback", "/business", "/queue"].some((part) => pathname.includes(part));
  if (pathname === `/${locale}` || bankSection) {
    const top = biz
      ? [
          { href: `/${locale}`, label: t.personal },
          { href: `/${locale}/business`, label: t.business },
          { href: `/${locale}/news`, label: t.news },
        ]
      : [
          { href: `/${locale}`, label: t.personal },
          { href: `/${locale}/business`, label: t.business },
          { href: `/${locale}/news`, label: t.news },
        ];
    const main = biz
      ? [
          { href: `/${locale}/loans`, label: t.business + " " + t.loans.toLowerCase() },
          { href: `/${locale}/cards`, label: t.cards },
          { href: `/${locale}/apply`, label: locale === "ru" ? "Услуги" : locale === "en" ? "Services" : "Xidmətlər" },
        ]
      : [
          { href: `/${locale}/loans`, label: t.loans },
          { href: `/${locale}/cards`, label: t.cards },
          { href: `/${locale}/deposits`, label: t.deposits },
          { href: `/${locale}/cashback`, label: t.cashback },
          { href: `/${locale}/branches`, label: t.branches },
          { href: `/${locale}/apply`, label: t.apply },
          { href: `/${locale}`, label: t.home },
        ];
    return (
      <header className={biz ? "bank-header biz" : "bank-header"}>
        <div className="bank-top">
          <div className="bank-wrap bank-top-row">
            <nav>
              {top.map((item, index) => (
                <Link
                  key={item.label}
                  href={item.href}
                  className={(biz ? item.href.endsWith("/business") : index === 0) ? "is-current" : ""}
                >
                  {item.label}
                </Link>
              ))}
            </nav>
            <div className="bank-tools">
              <Link href={`/${locale}/queue`}>{t.queue}</Link>
              <Link href={`/${locale}/apply`}>{t.apply}</Link>
              <Link href={`/${locale}/branches`}>{t.branches}</Link>
              <a className="hotline" href="tel:982">
                <svg viewBox="0 0 24 24" width="15" height="15" aria-hidden="true">
                  <path
                    fill="currentColor"
                    d="M6.6 10.8a15 15 0 0 0 6.6 6.6l2.2-2.2a1 1 0 0 1 1-.25 11.4 11.4 0 0 0 3.5.56 1 1 0 0 1 1 1V20a1 1 0 0 1-1 1A17 17 0 0 1 3 7a1 1 0 0 1 1-1h3.5a1 1 0 0 1 1 1 11.4 11.4 0 0 0 .56 3.5 1 1 0 0 1-.25 1L6.6 10.8z"
                  />
                </svg>
                982
              </a>
              <button type="button" aria-label="Search">
                <svg viewBox="0 0 24 24" width="16" height="16" aria-hidden="true">
                  <circle cx="10" cy="10" r="6" fill="none" stroke="currentColor" strokeWidth="2" />
                  <path d="M15 15l5 5" stroke="currentColor" strokeWidth="2" />
                </svg>
              </button>
              <div className="bank-lang">
                {locales.map((item) => (
                  <Link key={item} href={swap(item)} className={item === locale ? "is-current" : ""}>
                    {item.toUpperCase()}
                  </Link>
                ))}
              </div>
              <ThemeToggle />
            </div>
          </div>
        </div>
        <div className="bank-wrap bank-main">
          <Link href={`/${locale}`} className="bank-logo">
            <span className="logo-fallback"><span>Yelo Bank2</span></span>
          </Link>
          <nav className="bank-nav">
            {main.map((item) => (
              <Link
                key={item.label}
                href={item.href}
                className={
                  pathname.startsWith(item.href) &&
                  ["/cards", "/loans", "/deposits", "/cashback", "/business"].some((part) => item.href.endsWith(part))
                    ? "is-current"
                    : ""
                }
              >
                {item.label}
              </Link>
            ))}
          </nav>
          <button className="bank-burger" type="button" aria-label="Menu">
            <span />
            <span />
            <span />
          </button>
        </div>
      </header>
    );
  }

  return (
    <header className="site-header">
      <div className={`shell header-row ${open ? "open" : ""}`}>
        <Link href={`/${locale}`} className="logo" onClick={() => setOpen(false)}>
          <span className="logo-mark">Y</span>
          Yelo Study
        </Link>
        <button className="menu-button" type="button" onClick={() => setOpen((value) => !value)}>
          Menu
        </button>
        <div className="header-tools">
          <nav className="nav">
            {links.map((link) => {
              const active = link.exact ? pathname === link.href : pathname.startsWith(link.href);
              return (
                <Link key={link.href} href={link.href} className={active ? "active" : ""} onClick={() => setOpen(false)}>
                  {link.label}
                </Link>
              );
            })}
          </nav>
          <div className="lang">
            {locales.map((item) => (
              <Link key={item} href={swap(item)} className={item === locale ? "active" : ""}>
                {item.toUpperCase()}
              </Link>
            ))}
          </div>
          <ThemeToggle />
        </div>
      </div>
    </header>
  );
}
