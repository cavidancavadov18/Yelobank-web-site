"use client";

import { useState, type ReactNode } from "react";

export function ImageSlot({
  src,
  alt,
  className,
  fallback,
}: {
  src: string;
  alt: string;
  className?: string;
  fallback: ReactNode;
}) {
  const [failed, setFailed] = useState(false);
  if (!src || failed) {
    return <>{fallback}</>;
  }
  return <img src={src} alt={alt} className={className} onError={() => setFailed(true)} />;
}
