import type { Metadata } from "next";
import Link from "next/link";
import { notFound } from "next/navigation";

import { ImageSlot } from "@/components/ImageSlot";
import { apiGet } from "@/lib/api";
import { isLocale } from "@/lib/i18n";
import type { CardsPageCopy, Product } from "@/lib/types";

export const metadata: Metadata = { title: "Kreditlər" };

const SPEC_KEYS = [1, 2, 3, 4] as const;

export default async function LoansPage({ params }: { params: Promise<{ locale: string }> }) {
  const { locale } = await params;
  if (!isLocale(locale)) notFound();
  const [page, products] = await Promise.all([
    apiGet<CardsPageCopy>(`/api/loans-page/?lang=${locale}`),
    apiGet<Product[]>(`/api/products/?type=loan&lang=${locale}`),
  ]);
  if (!page || !products) notFound();

  return (
    <section className="loans-view">
      <h1>{page.heading}</h1>
      <p className="loans-lead">{page.lead}</p>
      <div className="loan-list">
        {products.map((product) => (
          <article key={product.slug} className="loan-offer">
            <div className="loan-copy">
              <h2>
                <Link href={`/${locale}/loans/${product.slug}`}>{product.title}</Link>
              </h2>
              <p>{product.summary}</p>
              <div className="loan-specs">
                {SPEC_KEYS.map((index) => {
                  const label = product[`spec_${index}_label`];
                  const value = product[`spec_${index}_value`];
                  if (!label && !value) return null;
                  return (
                    <div key={index}>
                      <span>{label}</span>
                      <strong>{value}</strong>
                    </div>
                  );
                })}
              </div>
              <div className="loan-actions">
                {product.order_label ? (
                  <Link className="skew-btn" href={`/${locale}/apply?product=${product.slug}`}>
                    <span>{product.order_label}</span>
                  </Link>
                ) : null}
                {product.more_label ? (
                  <Link className="more-link" href={`/${locale}/loans/${product.slug}`}>
                    {product.more_label}
                    <span aria-hidden="true"> →</span>
                  </Link>
                ) : null}
              </div>
            </div>
            <div className="loan-art" aria-hidden={!product.image}>
              <ImageSlot
                src={product.image}
                alt=""
                className={product.slug === "study-consumer" || product.slug === "study-cash" ? "loan-photo loan-cover" : "loan-photo"}
                fallback={<div className="loan-fallback" />}
              />
            </div>
          </article>
        ))}
      </div>
    </section>
  );
}
