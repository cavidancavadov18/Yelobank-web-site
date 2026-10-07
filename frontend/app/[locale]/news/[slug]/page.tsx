import type { Metadata } from "next";
import { notFound } from "next/navigation";

import { apiGet } from "@/lib/api";
import { formatDate, isLocale } from "@/lib/i18n";
import type { NewsItem } from "@/lib/types";

export const metadata: Metadata = { title: "News" };

export default async function NewsDetailPage({
  params,
}: {
  params: Promise<{ locale: string; slug: string }>;
}) {
  const { locale, slug } = await params;
  if (!isLocale(locale)) notFound();
  const item = await apiGet<NewsItem>(`/api/news/${slug}/?lang=${locale}`);
  if (!item) notFound();

  return (
    <article className="section">
      <p className="meta">{formatDate(item.published_at, locale)}</p>
      <h1>{item.title}</h1>
      <p className="lead">{item.summary}</p>
      <p>{item.body}</p>
    </article>
  );
}
