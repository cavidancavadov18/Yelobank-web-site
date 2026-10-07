"use client";

export default function LocaleError({ reset }: { error: Error; reset: () => void }) {
  return (
    <section className="section">
      <h1>Yelo Study</h1>
      <p className="error">Məlumat yüklənmədi.</p>
      <button className="button" type="button" onClick={reset}>
        Yenidən
      </button>
    </section>
  );
}
