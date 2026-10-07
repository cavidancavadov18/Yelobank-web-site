import type { Metadata } from "next";
import Link from "next/link";
import { notFound } from "next/navigation";

import { isLocale, type Locale } from "@/lib/i18n";

export const metadata: Metadata = { title: "Biznes" };

const copy = {
  az: {
    title: "Nümunə biznes krediti, onlayn müraciət",
    lead: "Nümunə faiz 18%-dən. Bu, real təklif deyil.",
    more: "Ətraflı",
    stories: "Storilər",
    cards: [
      { href: "/loans", title: "Nümunə kredit", text: "Biznes üçün nümunə kredit səhifəsi." },
      { href: "/cashback", title: "Nümunə keşbek", text: "Keşbek bölməsinə keçid." },
      { href: "/apply", title: "Nümunə müraciət", text: "Forma lokal bazaya yazılır." },
    ],
  },
  en: {
    title: "Sample business loan, online request",
    lead: "Sample rate from 18%. This is not a real offer.",
    more: "Details",
    stories: "Stories",
    cards: [
      { href: "/loans", title: "Sample loan", text: "A sample page for a business loan." },
      { href: "/cashback", title: "Sample cashback", text: "Open the cashback section." },
      { href: "/apply", title: "Sample request", text: "The form is stored locally." },
    ],
  },
  ru: {
    title: "Учебный бизнес-кредит, онлайн-заявка",
    lead: "Учебная ставка от 18%. Это не реальное предложение.",
    more: "Подробнее",
    stories: "Истории",
    cards: [
      { href: "/loans", title: "Учебный кредит", text: "Страница учебного бизнес-кредита." },
      { href: "/cashback", title: "Учебный кешбэк", text: "Переход в раздел кешбэка." },
      { href: "/apply", title: "Учебная заявка", text: "Форма пишется в локальную базу." },
    ],
  },
} as const;

export default async function BusinessPage({ params }: { params: Promise<{ locale: string }> }) {
  const { locale } = await params;
  if (!isLocale(locale)) notFound();
  const text = copy[locale as Locale];

  return (
    <section className="biz-view">
      <div className="biz-hero">
        <div>
          <h1>{text.title}</h1>
          <p>{text.lead}</p>
          <Link href={`/${locale}/loans`}>
            {text.more}
            <span aria-hidden="true"> →</span>
          </Link>
        </div>
        <div className="biz-art" aria-hidden="true">
          <strong>18%</strong>
          <span>nümunə</span>
          <i />
        </div>
      </div>
      <div className="biz-stories">
        <div className="biz-wrap">
          <h2>
            {text.stories} <b>3</b>
          </h2>
          <div className="biz-row">
            {text.cards.map((card) => (
              <Link key={card.href} href={`/${locale}${card.href}`}>
                <strong>{card.title}</strong>
                <span>{card.text}</span>
              </Link>
            ))}
          </div>
        </div>
      </div>
    </section>
  );
}
