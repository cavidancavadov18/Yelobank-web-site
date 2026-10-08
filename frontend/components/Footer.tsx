"use client";

import { usePathname } from "next/navigation";

import { copy, isLocale } from "@/lib/i18n";

export function Footer() {
  const pathname = usePathname();
  const locale = pathname.split("/")[1];
  if (
    !isLocale(locale) ||
    pathname === `/${locale}` ||
    ["/cards", "/loans", "/deposits", "/invest", "/cashback", "/business", "/queue"].some((part) => pathname.includes(part))
  ) {
    return null;
  }
  return (
    <footer className="site-footer">
      <div className="shell">{copy(locale).studyNote}</div>
    </footer>
  );
}
