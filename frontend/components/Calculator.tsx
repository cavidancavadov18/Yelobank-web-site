"use client";

import { useMemo, useState } from "react";

import { copy, type Locale } from "@/lib/i18n";

type Props = {
  locale: Locale;
  annualRate: string;
  currency: string;
  minAmount: string;
  maxAmount: string;
  minMonths: number;
  maxMonths: number;
};

export function Calculator({ locale, annualRate, currency, minAmount, maxAmount, minMonths, maxMonths }: Props) {
  const t = copy(locale);
  const [amount, setAmount] = useState(Number(minAmount) || 1000);
  const [months, setMonths] = useState(minMonths || 12);

  const monthly = useMemo(() => {
    const principal = Number(amount);
    const term = Number(months);
    const annual = Number(annualRate);
    if (!principal || !term) return 0;
    const monthlyRate = annual / 100 / 12;
    if (monthlyRate === 0) return principal / term;
    const factor = (1 + monthlyRate) ** term;
    return (principal * monthlyRate * factor) / (factor - 1);
  }, [amount, months, annualRate]);

  return (
    <section className="panel">
      <h2>{t.calculator}</h2>
      <div className="form">
        <label>
          {t.amount} ({currency})
          <input
            type="number"
            min={minAmount}
            max={maxAmount}
            value={amount}
            onChange={(event) => setAmount(Number(event.target.value))}
          />
        </label>
        <label>
          {t.term}
          <input
            type="number"
            min={minMonths}
            max={maxMonths}
            value={months}
            onChange={(event) => setMonths(Number(event.target.value))}
          />
        </label>
        <p className="meta">
          {t.rate}: {annualRate}%
        </p>
        <div className="calc-result">
          {t.monthly}
          <strong>
            {monthly.toFixed(2)} {currency}
          </strong>
        </div>
      </div>
    </section>
  );
}
