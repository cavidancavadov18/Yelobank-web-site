"use client";

import { ViewTransition } from "react";
import { usePathname } from "next/navigation";

export function SectionSwap({ children }: { children: React.ReactNode }) {
  const pathname = usePathname();

  return (
    <ViewTransition key={pathname} name="section" enter="section-in" exit="section-out" default="none">
      <div className="section-swap">{children}</div>
    </ViewTransition>
  );
}
