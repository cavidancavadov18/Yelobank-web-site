import Link from "next/link";
import { notFound } from "next/navigation";

import { HomeCalc } from "@/components/HomeCalc";
import { HomeSlider } from "@/components/HomeSlider";
import { ImageSlot } from "@/components/ImageSlot";
import { ProductMark } from "@/components/ProductMark";
import { apiGet } from "@/lib/api";
import { copy, formatDate, isLocale, type Locale } from "@/lib/i18n";
import type { HomePayload, NewsItem, Product } from "@/lib/types";

export default async function HomePage({ params }: { params: Promise<{ locale: string }> }) {
  const { locale } = await params;
  if (!isLocale(locale)) notFound();
  const t = copy(locale);
  const [home, news] = await Promise.all([
    apiGet<HomePayload>(`/api/home/?lang=${locale}`),
    apiGet<NewsItem[]>(`/api/news/?lang=${locale}`),
  ]);
  if (!home || !news) notFound();

  const stories = [...home.cards, ...home.loans, ...(home.deposits ?? [])];
  const featured = home.cards[0];
  const loan = home.loans[0];
  const offers = suggestions[locale];

  return (
    <section className="home-view">
      <HomeSlider banners={home.banners} locale={locale} orderLabel={t.applyNow} moreLabel={t.readMore} />

      <div className="home-offers">
        <h2 className="home-heading">{offers.title}</h2>
        <div className="offer-row">
          {offers.items.map((item) => (
            <Link key={item.href} className="offer-card" href={`/${locale}${item.href}`}>
              <span className={`offer-mark ${item.href === "/cards" ? "mark-card" : ""}`}>
                <ProductMark
                  kind={item.href === "/loans" ? "loan" : "card"}
                  slug={item.href === "/cashback" ? "cashback" : item.href}
                />
              </span>
              <span>
                <strong>{item.title}</strong>
                <span>{item.text}</span>
              </span>
            </Link>
          ))}
        </div>
      </div>

      <div className="home-stories">
        <div className="home-wrap">
          <h2 className="home-heading">{t.cards}</h2>
        </div>
        <div className="story-row">
          {stories.map((product) => (
            <Story key={product.slug} product={product} locale={locale} />
          ))}
        </div>
      </div>

      <div className="home-main">
        <div className="home-split">
          {featured ? (
            <article className="promo-card">
              <div>
                <h3>{featured.title}</h3>
                <p>{featured.summary}</p>
                <Link className="skew-btn" href={`/${locale}/cards/${featured.slug}`}>
                  <span>{t.readMore}</span>
                </Link>
              </div>
              {featured.kind === "card" ? (
                <div className="promo-fallback">
                  <ProductMark kind="card" slug={featured.slug} detail />
                </div>
              ) : (
                <ImageSlot
                  src={featured.image}
                  alt=""
                  className="promo-photo"
                  fallback={<div className="promo-fallback" />}
                />
              )}
            </article>
          ) : (
            <div />
          )}
          {loan ? (
            <HomeCalc
              locale={locale}
              annualRate={String(loan.interest_rate)}
              currency={loan.currency}
              minAmount={String(loan.min_amount)}
              maxAmount={String(loan.max_amount)}
              minMonths={loan.min_months}
              maxMonths={loan.max_months}
            />
          ) : null}
        </div>

        <div>
          <h2 className="home-heading">{t.rates}</h2>
          <div className="home-split app">
            <article className="app-card">
              <h3>{t.appTitle}</h3>
              <p>{t.appText}</p>
              <Link className="skew-btn" href={`/${locale}/apply`}>
                <span>{t.apply}</span>
              </Link>
            </article>
            <article className="rate-card">
              <table>
                <thead>
                  <tr>
                    <th>{t.currency}</th>
                    <th>{t.buy}</th>
                    <th>{t.sell}</th>
                  </tr>
                </thead>
                <tbody>
                  {home.rates.map((rate) => (
                    <tr key={rate.currency}>
                      <td>{rate.currency}</td>
                      <td>{rate.buy}</td>
                      <td>{rate.sell}</td>
                    </tr>
                  ))}
                </tbody>
              </table>
            </article>
          </div>
        </div>

        <div>
          <h2 className="home-heading">{t.latestNews}</h2>
          <div className="news-row">
            {news.slice(0, 3).map((item) => (
              <article key={item.slug} className="news-card">
                <p>{formatDate(item.published_at, locale)}</p>
                <h3>{item.title}</h3>
                <Link href={`/${locale}/news/${item.slug}`}>{t.readMore}</Link>
              </article>
            ))}
          </div>
          <Link className="news-all" href={`/${locale}/news`}>
            {t.allNews}
            <span aria-hidden="true"> →</span>
          </Link>
        </div>
      </div>

      <footer className="bank-foot">
        <div className="bank-foot-grid">
          <div>
            <h3>{t.home}</h3>
            <Link href={`/${locale}/loans`}>{t.loans}</Link>
            <Link href={`/${locale}/cards`}>{t.cards}</Link>
            <Link href={`/${locale}/deposits`}>{t.deposits}</Link>
            <Link href={`/${locale}/cashback`}>{t.cashback}</Link>
            <Link href={`/${locale}/apply`}>{t.apply}</Link>
          </div>
          <div>
            <h3>{t.news}</h3>
            <Link href={`/${locale}/news`}>{t.allNews}</Link>
            <Link href={`/${locale}/branches`}>{t.branches}</Link>
          </div>
          <div>
            <h3>{t.apply}</h3>
            <Link href={`/${locale}/apply`}>{t.applyNow}</Link>
            <p>000</p>
          </div>
          <div>
            <h3>Yelo Bank2</h3>
            <p>{t.studyNote}</p>
          </div>
        </div>
      </footer>
    </section>
  );
}

const suggestions = {
  az: {
    title: "Təkliflər",
    items: [
      { href: "/loans", title: "Nümunə kredit", text: "Məbləği və müddəti səhifədə yoxla." },
      { href: "/cards", title: "Nümunə kart", text: "Gündəlik ödəniş üçün nümunə kart." },
      { href: "/cashback", title: "Nümunə keşbek", text: "Seçilmiş kateqoriyada nümunə geri ödəmə." },
    ],
  },
  en: {
    title: "Suggestions",
    items: [
      { href: "/loans", title: "Sample loan", text: "Check the amount and term on the page." },
      { href: "/cards", title: "Sample card", text: "A sample card for everyday payments." },
      { href: "/cashback", title: "Sample cashback", text: "Sample cashback in a chosen category." },
    ],
  },
  ru: {
    title: "Предложения",
    items: [
      { href: "/loans", title: "Учебный кредит", text: "Сумму и срок можно проверить на странице." },
      { href: "/cards", title: "Учебная карта", text: "Учебная карта для ежедневных платежей." },
      { href: "/cashback", title: "Учебный кешбэк", text: "Учебный кешбэк в выбранной категории." },
    ],
  },
} as const;

function Story({ product, locale }: { product: Product; locale: Locale }) {
  const section = product.kind === "card" ? "cards" : product.kind === "deposit" ? "deposits" : "loans";
  return (
    <Link className="story-item" href={`/${locale}/${section}/${product.slug}`}>
      {product.kind === "card" ? (
        <div className={`story-fallback ${product.slug.includes("cash") ? "" : "mark-card"}`}>
          <ProductMark kind="card" slug={product.slug} />
        </div>
      ) : (
        <ImageSlot
          src={product.image}
          alt=""
          className="story-photo"
          fallback={
            <div className="story-fallback">
              <ProductMark kind={product.kind} slug={product.slug} />
            </div>
          }
        />
      )}
      <span>
        <strong>{product.title}</strong>
        {product.summary}
      </span>
    </Link>
  );
}
