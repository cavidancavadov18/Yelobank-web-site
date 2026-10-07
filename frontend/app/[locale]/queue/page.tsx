import type { Metadata } from "next";
import { notFound } from "next/navigation";

import { QueueForm } from "@/components/QueueForm";
import { apiGet } from "@/lib/api";
import { copy, isLocale } from "@/lib/i18n";
import type { Branch } from "@/lib/types";

export const metadata: Metadata = { title: "Onlayn növbə" };

export default async function QueuePage({ params }: { params: Promise<{ locale: string }> }) {
  const { locale } = await params;
  if (!isLocale(locale)) notFound();
  const t = copy(locale);
  const branches = await apiGet<Branch[]>(`/api/branches/?lang=${locale}`);
  const names = (branches ?? []).filter((item) => item.kind === "branch").map((item) => item.name);

  return (
    <section className="section queue-view">
      <h1>{t.queue}</h1>
      <p className="lead">
        {locale === "ru"
          ? "Учебная очередь. Выбираются филиал, услуга и время. В реальный терминал не отправляется."
          : locale === "en"
            ? "A sample queue. Pick a branch, a service, and a time. Nothing is sent to a real terminal."
            : "Nümunə növbə. Filial, xidmət və saat seçilir. Real terminala getmir."}
      </p>
      <QueueForm locale={locale} branches={names} />
    </section>
  );
}
