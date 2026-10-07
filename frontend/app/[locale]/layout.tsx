import { notFound } from "next/navigation";

import { DayWeather } from "@/components/DayWeather";
import { Footer } from "@/components/Footer";
import { Header } from "@/components/Header";
import { SectionSwap } from "@/components/SectionSwap";
import { isLocale } from "@/lib/i18n";

export const dynamic = "force-dynamic";

export default async function LocaleLayout({
  children,
  params,
}: {
  children: React.ReactNode;
  params: Promise<{ locale: string }>;
}) {
  const { locale } = await params;
  if (!isLocale(locale)) {
    notFound();
  }

  return (
    <>
      <DayWeather />
      <Header locale={locale} />
      <main className="page">
        <div className="shell">
          <SectionSwap>{children}</SectionSwap>
        </div>
      </main>
      <Footer />
    </>
  );
}
