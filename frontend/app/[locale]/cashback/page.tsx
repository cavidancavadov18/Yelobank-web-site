import type { Metadata } from "next";
import { notFound } from "next/navigation";

import { CashbackView } from "@/components/CashbackView";
import { apiGet } from "@/lib/api";
import { isLocale } from "@/lib/i18n";
import type { CashbackCopy } from "@/lib/types";

export const metadata: Metadata = { title: "Keşbek" };

export default async function CashbackPage({ params }: { params: Promise<{ locale: string }> }) {
  const { locale } = await params;
  if (!isLocale(locale)) notFound();
  const copy = await apiGet<CashbackCopy>(`/api/cashback/?lang=${locale}`);
  if (!copy) notFound();
  return <CashbackView locale={locale} copy={copy} />;
}
