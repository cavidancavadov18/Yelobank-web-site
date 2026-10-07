import type { Metadata } from "next";
import Link from "next/link";
import { notFound } from "next/navigation";

import { apiGet } from "@/lib/api";
import { copy, formatDate, isLocale } from "@/lib/i18n";
import type { NewsItem } from "@/lib/types";

export const metadata: Metadata = { title: "News" };

export default async function NewsPage({ params }: { params: Promise<{ locale: string }> }) {
  const { locale } = await params;
  if (!isLocale(locale)) notFound();
  const t = copy(locale);
  const news = await apiGet<NewsItem[]>(`/api/news/?lang=${locale}`);
  if (!news) notFound();

  return (
    <section className="section">
      <h1>{t.news}</h1>
      <p className="lead">{t.newsLead}</p>
      <div className="grid" style={{ marginTop: 16 }}>
        {news.map((item) => (
          <article key={item.slug} className="card">
            <p className="meta">{formatDate(item.published_at, locale)}</p>
            <h3>{item.title}</h3>
            <p className="meta">{item.summary}</p>
            <Link className="button" href={`/${locale}/news/${item.slug}`}>
              {t.readMore}
            </Link>
          </article>
        ))}
      </div>
    </section>
  );
}
