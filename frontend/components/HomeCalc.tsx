"use client";

import Link from "next/link";
import { useMemo, useState } from "react";

import { copy, type Locale } from "@/lib/i18n";

export function HomeCalc({
  locale,
  annualRate,
  currency,
  minAmount,
  maxAmount,
  minMonths,
  maxMonths,
}: {
  locale: Locale;
  annualRate: string;
  currency: string;
  minAmount: string;
  maxAmount: string;
  minMonths: number;
  maxMonths: number;
}) {
  const t = copy(locale);
  const lowAmount = Number(minAmount) || 500;
  const highAmount = Number(maxAmount) || 15000;
  const lowMonths = minMonths || 6;
  const highMonths = maxMonths || 36;
  const [amount, setAmount] = useState(Math.round((lowAmount + highAmount) / 2 / 100) * 100);
  const [months, setMonths] = useState(Math.round((lowMonths + highMonths) / 2));

  const monthly = useMemo(() => {
    const annual = Number(annualRate);
    if (!amount || !months) return 0;
    const monthlyRate = annual / 100 / 12;
    if (monthlyRate === 0) return amount / months;
    const factor = (1 + monthlyRate) ** months;
    return (amount * monthlyRate * factor) / (factor - 1);
  }, [amount, months, annualRate]);

  return (
    <div className="home-calc">
      <h3>{t.calculator}</h3>
      <label>
        <span>{t.amount}</span>
        <strong>
          {amount.toString().replace(/\B(?=(\d{3})+(?!\d))/g, " ")} {currency}
        </strong>
        <input
          type="range"
          min={lowAmount}
          max={highAmount}
          step={100}
          value={amount}
          onChange={(event) => setAmount(Number(event.target.value))}
        />
      </label>
      <label>
        <span>{t.term}</span>
        <strong>
          {months} {t.months}
        </strong>
        <input
          type="range"
          min={lowMonths}
          max={highMonths}
          value={months}
          onChange={(event) => setMonths(Number(event.target.value))}
        />
      </label>
      <p className="calc-line">
        <span>{t.rate}</span>
        <strong>{annualRate}%</strong>
      </p>
      <p className="calc-pay">
        <span>{t.monthly}</span>
        <strong>
          {monthly.toFixed(2)} {currency}
        </strong>
      </p>
      <Link className="skew-btn" href={`/${locale}/apply`}>
        <span>{t.applyNow}</span>
      </Link>
    </div>
  );
}
