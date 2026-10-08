import type { Metadata } from "next";
import Link from "next/link";
import { notFound } from "next/navigation";

import { isLocale, type Locale } from "@/lib/i18n";

export const metadata: Metadata = { title: "Yelo Invest" };

const copy = {
  az: {
    lead: "Nümunə investisiya səhifəsi. Səhm alınmır və pul köçürülmür.",
    cta: "Müraciət et",
    screen: "Nümunə siyahı",
    facts: ["Nümunə siyahı", "Lokal müraciət", "Nümunə saat", "Pul köçürülmür"],
    portfolio: "Nümunə portfel",
    portfolioText: "Rəqəmlər uydurmadır. Bazardakı qiymət deyil.",
    orders: "Nümunə sifariş növləri",
    market: "Bazar sifarişi",
    marketText: "Səhifədə yazılan rəqəm nümunədir. Alış getmir.",
    limit: "Limit sifarişi",
    limitText: "Öz rəqəmini yazmaq olar, amma əməliyyat açılmır.",
    chart: "Nümunə qrafik",
    chartText: "Xətt təsadüfi çəkilib. Bazar hərəkəti deyil.",
    stepsTitle: "Necə baxılır",
    steps: ["Menyudan Yelo Invest aç", "Nümunə siyahıya bax", "İstəsən lokal müraciət göndər"],
    faq: "Suallar",
    faqs: [
      ["Bu real investisiyadır?", "Xeyr. Öyrənmə səhifəsidir."],
      ["Səhm nədir?", "Nümunə izah: şirkətin kiçik bir payı."],
      ["Saat neçədir?", "Nümunə saat 10:00–16:00. Real bazar saatı deyil."],
    ],
    rows: [
      ["Nümunə A", "12.40"],
      ["Nümunə B", "48.10"],
      ["Nümunə C", "7.25"],
    ],
  },
  en: {
    lead: "A sample investment page. No shares are bought and no money moves.",
    cta: "Apply",
    screen: "Sample list",
    facts: ["Sample list", "Local request", "Sample hours", "No money moves"],
    portfolio: "Sample portfolio",
    portfolioText: "The numbers are made up. They are not market prices.",
    orders: "Sample order types",
    market: "Market order",
    marketText: "The figure on the page is a sample. Nothing is bought.",
    limit: "Limit order",
    limitText: "You can type a figure, but no order is placed.",
    chart: "Sample chart",
    chartText: "The line is drawn at random. It is not a market move.",
    stepsTitle: "How to look",
    steps: ["Open Yelo Invest in the menu", "Read the sample list", "Send a local request if you want"],
    faq: "Questions",
    faqs: [
      ["Is this a real investment?", "No. It is a study page."],
      ["What is a share?", "A sample explanation: a small piece of a company."],
      ["What are the hours?", "Sample hours 10:00–16:00. Not a real market session."],
    ],
    rows: [
      ["Sample A", "12.40"],
      ["Sample B", "48.10"],
      ["Sample C", "7.25"],
    ],
  },
  ru: {
    lead: "Учебная страница инвестиций. Акции не покупаются и деньги не переводятся.",
    cta: "Оставить заявку",
    screen: "Учебный список",
    facts: ["Учебный список", "Локальная заявка", "Учебные часы", "Деньги не идут"],
    portfolio: "Учебный портфель",
    portfolioText: "Цифры выдуманы. Это не рыночная цена.",
    orders: "Учебные виды заявок",
    market: "Рыночная заявка",
    marketText: "Цифра на странице учебная. Покупки нет.",
    limit: "Лимитная заявка",
    limitText: "Свою цифру написать можно, но заявка не уходит.",
    chart: "Учебный график",
    chartText: "Линия нарисована произвольно. Это не движение рынка.",
    stepsTitle: "Как смотреть",
    steps: ["Открой Yelo Invest в меню", "Посмотри учебный список", "При желании отправь локальную заявку"],
    faq: "Вопросы",
    faqs: [
      ["Это реальная инвестиция?", "Нет. Это учебная страница."],
      ["Что такое акция?", "Учебное объяснение: маленькая доля компании."],
      ["Какие часы?", "Учебные часы 10:00–16:00. Это не сессия настоящего рынка."],
    ],
    rows: [
      ["Пример A", "12.40"],
      ["Пример B", "48.10"],
      ["Пример C", "7.25"],
    ],
  },
} as const;

export default async function InvestPage({ params }: { params: Promise<{ locale: string }> }) {
  const { locale } = await params;
  if (!isLocale(locale)) notFound();
  const text = copy[locale as Locale];

  return (
    <section className="invest-view">
      <div className="invest-hero">
        <div className="invest-copy">
          <h1>Yelo Invest</h1>
          <p>{text.lead}</p>
          <Link className="invest-cta" href={`/${locale}/apply?product=invest`}>
            {text.cta}
          </Link>
        </div>
        <div className="invest-stage" aria-hidden="true">
          <div className="invest-phone">
            <strong>{text.screen}</strong>
            {text.rows.map(([name, price]) => (
              <span key={name}>
                <b>{name}</b>
                <em>{price}</em>
              </span>
            ))}
          </div>
        </div>
      </div>
      <ul className="invest-facts">
        {text.facts.map((fact) => (
          <li key={fact}>{fact}</li>
        ))}
      </ul>
      <div className="invest-grid">
        <article>
          <h2>{text.portfolio}</h2>
          <p>{text.portfolioText}</p>
          <div className="invest-bars">
            <i style={{ width: "72%" }} />
            <i style={{ width: "46%" }} />
            <i style={{ width: "28%" }} />
          </div>
        </article>
        <article>
          <h2>{text.orders}</h2>
          <h3>{text.market}</h3>
          <p>{text.marketText}</p>
          <h3>{text.limit}</h3>
          <p>{text.limitText}</p>
        </article>
        <article>
          <h2>{text.chart}</h2>
          <p>{text.chartText}</p>
          <svg viewBox="0 0 240 80">
            <polyline points="0,60 40,48 80,52 120,30 160,36 200,18 240,24" fill="none" stroke="#161616" strokeWidth="3" />
          </svg>
        </article>
      </div>
      <div className="invest-steps">
        <h2>{text.stepsTitle}</h2>
        <ol>
          {text.steps.map((step) => (
            <li key={step}>{step}</li>
          ))}
        </ol>
      </div>
      <div className="invest-faq">
        <h2>{text.faq}</h2>
        {text.faqs.map(([question, answer]) => (
          <details key={question}>
            <summary>{question}</summary>
            <p>{answer}</p>
          </details>
        ))}
      </div>
    </section>
  );
}
