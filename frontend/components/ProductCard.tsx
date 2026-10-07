import Link from "next/link";

import { copy, type Locale } from "@/lib/i18n";
import type { Product } from "@/lib/types";

export function ProductCard({ product, locale }: { product: Product; locale: Locale }) {
  const t = copy(locale);
  const section = product.kind === "card" ? "cards" : product.kind === "deposit" ? "deposits" : "loans";
  return (
    <article className="card">
      <h3>{product.title}</h3>
      <p className="meta">{product.summary}</p>
      {product.kind === "loan" ? (
        <p className="meta">
          {t.rate}: {product.interest_rate}% · {t.upTo} {product.max_amount} {product.currency}
        </p>
      ) : null}
      <Link className="button" href={`/${locale}/${section}/${product.slug}`}>
        {t.readMore}
      </Link>
    </article>
  );
}
