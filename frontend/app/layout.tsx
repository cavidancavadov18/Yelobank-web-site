import type { Metadata } from "next";
import Script from "next/script";

import "./globals.css";

export const metadata: Metadata = {
  title: {
    default: "Yelo Study",
    template: "%s · Yelo Study",
  },
  description: "Local study site",
};

export default function RootLayout({ children }: { children: React.ReactNode }) {
  return (
    <html lang="az" translate="no" suppressHydrationWarning>
      <body>
        <Script id="yelo-theme" strategy="beforeInteractive">
          {`try{if(localStorage.getItem("yelo-theme")==="night")document.documentElement.dataset.theme="night"}catch(e){}`}
        </Script>
        {children}
      </body>
    </html>
  );
}
