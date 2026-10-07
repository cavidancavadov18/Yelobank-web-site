import type { Metadata } from "next";
import Link from "next/link";
import { notFound } from "next/navigation";

import { apiGet } from "@/lib/api";
import { isLocale } from "@/lib/i18n";
import type { CardsPageCopy, Product } from "@/lib/types";

export const metadata: Metadata = { title: "Əmanətlər" };

const SPEC_KEYS = [1, 2, 3, 4] as const;

export default async function DepositsPage({ params }: { params: Promise<{ locale: string }> }) {
  const { locale } = await params;
  if (!isLocale(locale)) notFound();
  const [page, products] = await Promise.all([
    apiGet<CardsPageCopy>(`/api/deposits-page/?lang=${locale}`),
    apiGet<Product[]>(`/api/products/?type=deposit&lang=${locale}`),
  ]);
  if (!page || !products) notFound();

  return (
    <section className="loans-view">
      <h1>{page.heading}</h1>
      <p className="loans-lead">{page.lead}</p>
      <div className="loan-list">
        {products.map((product) => (
          <article key={product.slug} className="deposit-offer">
            <div className="deposit-copy">
              <h2>
                <Link href={`/${locale}/deposits/${product.slug}`}>{product.title}</Link>
              </h2>
              <p>{product.summary}</p>
              <div className="deposit-specs">
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
              <div className="deposit-actions">
                {product.order_label ? (
                  <Link className="skew-btn" href={`/${locale}/apply?product=${product.slug}`}>
                    <span>{product.order_label}</span>
                  </Link>
                ) : null}
                {product.more_label ? (
                  <Link className="more-link" href={`/${locale}/deposits/${product.slug}`}>
                    {product.more_label}
                    <span aria-hidden="true"> →</span>
                  </Link>
                ) : null}
              </div>
            </div>
            <DepositArt />
          </article>
        ))}
      </div>
    </section>
  );
}

function DepositArt() {
  return (
    <div className="deposit-art" aria-hidden="true">
      <svg viewBox="0 0 320 280">
        <rect x="150" y="36" width="150" height="220" rx="18" fill="#f5c400" />
        <ellipse cx="214" cy="228" rx="62" ry="16" fill="#8d98a3" />
        <rect x="152" y="132" width="124" height="96" fill="#c5ced6" />
        <ellipse cx="214" cy="132" rx="62" ry="16" fill="#e7eef3" />
        <ellipse cx="214" cy="228" rx="62" ry="16" fill="#b7c2cb" />
        <ellipse cx="132" cy="236" rx="46" ry="13" fill="#c49600" />
        <rect x="86" y="168" width="92" height="68" fill="#f5c400" />
        <ellipse cx="132" cy="168" rx="46" ry="13" fill="#ffe14a" />
        <rect x="108" y="186" width="54" height="22" rx="3" fill="#1f7a4d" />
        <rect x="112" y="190" width="46" height="14" rx="2" fill="none" stroke="#d8ffe8" />
        <ellipse cx="104" cy="196" rx="16" ry="8" fill="#d7a800" />
        <ellipse cx="104" cy="190" rx="16" ry="8" fill="#ffe14a" />
        <ellipse cx="128" cy="198" rx="16" ry="8" fill="#d7a800" />
        <ellipse cx="128" cy="192" rx="16" ry="8" fill="#fff6c2" />
        <rect x="156" y="48" width="96" height="84" rx="10" fill="#d5dde4" />
        <rect x="164" y="56" width="80" height="68" rx="8" fill="#eef3f6" />
        <circle cx="204" cy="90" r="18" fill="#f7fafc" stroke="#9aa6b2" strokeWidth="3" />
        <circle cx="204" cy="90" r="4" fill="#9aa6b2" />
        <text x="232" y="78" fill="#f5c400" fontSize="28" fontFamily="Arial" fontWeight="700">
          %
        </text>
      </svg>
    </div>
  );
}
