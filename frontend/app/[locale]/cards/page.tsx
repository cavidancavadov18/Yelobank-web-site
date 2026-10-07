import type { Metadata } from "next";
import Link from "next/link";
import { notFound } from "next/navigation";

import { apiGet } from "@/lib/api";
import { isLocale } from "@/lib/i18n";
import type { CardsPageCopy, Product } from "@/lib/types";

export const metadata: Metadata = { title: "Kartlar" };

export default async function CardsPage({ params }: { params: Promise<{ locale: string }> }) {
  const { locale } = await params;
  if (!isLocale(locale)) notFound();
  const [page, products] = await Promise.all([
    apiGet<CardsPageCopy>(`/api/cards-page/?lang=${locale}`),
    apiGet<Product[]>(`/api/products/?type=card&lang=${locale}`),
  ]);
  if (!page || !products) notFound();

  return (
    <section className="cards-view">
      <h1>{page.heading}</h1>
      <p className="cards-lead">{page.lead}</p>
      <div className="offer-list">
        {products.map((product) => (
          <article key={product.slug} className="offer">
            <div className="offer-copy">
              <h2>{product.title}</h2>
              <p>{product.summary}</p>
              <div className="offer-specs">
                {[1, 2, 3].map((index) => {
                  const label = product[`spec_${index}_label` as "spec_1_label"];
                  const value = product[`spec_${index}_value` as "spec_1_value"];
                  if (!label && !value) return null;
                  return (
                    <div key={index}>
                      <span>{label}</span>
                      <strong>{value}</strong>
                    </div>
                  );
                })}
              </div>
              <div className="offer-actions">
                {product.order_label ? (
                  <Link className="skew-btn" href={`/${locale}/apply?product=${product.slug}`}>
                    <span>{product.order_label}</span>
                  </Link>
                ) : null}
                {product.more_label ? (
                  <Link className="more-link" href={`/${locale}/cards/${product.slug}`}>
                    {product.more_label}
                    <span aria-hidden="true"> →</span>
                  </Link>
                ) : null}
              </div>
            </div>
            <div className="offer-art" aria-hidden="true">
              <div className="yellow-panel" />
              <div className={`card-stage${product.slug.includes("cash") ? " cash" : " debit"}`}>
                <div className="card-spin3d">
                  <div className="section-card">
                    <div className="card-brand">
                      <strong>Yelo Bank</strong>
                      <span className="card-wave" />
                    </div>
                    <span className="card-chip" />
                    {product.slug.includes("cash") ? <span className="pct-logo">2%</span> : null}
                    <span className="card-pan">0000 0000 0000 0000</span>
                    <div className="card-foot">
                      <b>Cavidan Cavadov</b>
                      <em>Visa</em>
                    </div>
                  </div>
                  <i className="card-side back" />
                  <i className="card-side left" />
                  <i className="card-side right" />
                  <i className="card-side top" />
                  <i className="card-side bottom" />
                </div>
              </div>
            </div>
          </article>
        ))}
      </div>
    </section>
  );
}
