"use client";

import Link from "next/link";
import { useState } from "react";

import type { Locale } from "@/lib/i18n";
import type { CashbackCopy } from "@/lib/types";

export function CashbackView({ locale, copy }: { locale: Locale; copy: CashbackCopy }) {
  const [active, setActive] = useState(copy.packs[0]?.id ?? "");
  const [open, setOpen] = useState<Record<string, boolean>>({});
  const pack = copy.packs.find((item) => item.id === active) ?? copy.packs[0];
  if (!pack) return null;

  function reveal(id: string) {
    setOpen((current) => ({ ...current, [id]: true }));
  }

  return (
    <section className="cash-view">
      <div className="cash-hero">
        <div>
          <h1>{copy.title}</h1>
          <Link className="cash-order" href={`/${locale}/apply`}>
            {copy.button}
          </Link>
        </div>
        <div className="cash-art">
          {(["back", "mid", "front"] as const).map((id) => (
            <button
              key={id}
              type="button"
              className={`cash-card ${id}${open[id] ? " open" : ""}`}
              onClick={() => reveal(id)}
            >
              {(id === "front" || open[id]) && (
                <>
                  <div className="card-brand">
                    <strong>Yelo Bank</strong>
                    <span className="card-wave" />
                  </div>
                  <span className="card-chip" />
                  <span className="pct-logo">2%</span>
                  {open[id] && <small className="card-pan">0000 0000 0000 0000</small>}
                  <div className="card-foot">
                    {open[id] ? <b>Cavidan Cavadov</b> : <b />}
                    <em>Visa</em>
                  </div>
                </>
              )}
            </button>
          ))}
          <i className="orb o1" />
          <i className="orb o2" />
          <i className="orb o3" />
          <i className="orb o4" />
          <i className="orb o5" />
        </div>
      </div>
      <div className="cash-body">
        <div className="cash-tabs">
          {copy.packs.map((item) => (
            <button
              key={item.id}
              type="button"
              className={item.id === pack.id ? "on" : ""}
              onClick={() => setActive(item.id)}
            >
              {item.label}
            </button>
          ))}
        </div>
        <p className="cash-note">{pack.note}</p>
        <div className="cash-grid">
          {pack.items.map((item) => (
            <article key={item.title}>
              <h2>{item.title}</h2>
              <p>{item.text}</p>
            </article>
          ))}
        </div>
      </div>
    </section>
  );
}
