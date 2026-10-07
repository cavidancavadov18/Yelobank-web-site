import type { Metadata } from "next";
import { notFound } from "next/navigation";

import { ApplyForm } from "@/components/ApplyForm";
import { apiGet } from "@/lib/api";
import { copy, isLocale } from "@/lib/i18n";
import type { Product } from "@/lib/types";

export const metadata: Metadata = { title: "Apply" };

export default async function ApplyPage({
  params,
  searchParams,
}: {
  params: Promise<{ locale: string }>;
  searchParams: Promise<{ product?: string }>;
}) {
  const { locale } = await params;
  const { product } = await searchParams;
  if (!isLocale(locale)) notFound();
  const t = copy(locale);
  const products = await apiGet<Product[]>(`/api/products/?lang=${locale}`);
  if (!products) notFound();

  return (
    <section className="section">
      <h1>{t.apply}</h1>
      <p className="lead">{t.applyLead}</p>
      <div style={{ marginTop: 16 }}>
        <ApplyForm locale={locale} products={products} initialSlug={product} />
      </div>
    </section>
  );
}
