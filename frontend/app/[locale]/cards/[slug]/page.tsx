import type { Metadata } from "next";
import Link from "next/link";
import { notFound } from "next/navigation";

import { apiGet } from "@/lib/api";
import { copy, isLocale } from "@/lib/i18n";
import type { Product } from "@/lib/types";

export const metadata: Metadata = { title: "Card" };

export default async function CardDetailPage({
  params,
}: {
  params: Promise<{ locale: string; slug: string }>;
}) {
  const { locale, slug } = await params;
  if (!isLocale(locale)) notFound();
  const t = copy(locale);
  const product = await apiGet<Product>(`/api/products/${slug}/?lang=${locale}`);
  if (!product || product.kind !== "card") notFound();

  return (
    <article className="section">
      <h1>{product.title}</h1>
      <p className="lead">{product.summary}</p>
      <div className="specs">
        <div className="spec">
          <span>{t.currency}</span>
          {product.currency}
        </div>
        <div className="spec">
          <span>{t.term}</span>
          {product.min_months}–{product.max_months} {t.months}
        </div>
      </div>
      <p>{product.body}</p>
      <Link className="button yellow" href={`/${locale}/apply?product=${product.slug}`}>
        {t.applyNow}
      </Link>
    </article>
  );
}
