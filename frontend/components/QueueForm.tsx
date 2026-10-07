"use client";

import { FormEvent, useState } from "react";

import { copy, type Locale } from "@/lib/i18n";

const TIMES = ["10:00", "11:00", "12:00", "14:00", "15:00", "16:00"];

const SERVICES: Record<Locale, string[]> = {
  az: ["Kart", "Kredit", "Əmanət", "Digər"],
  en: ["Card", "Loan", "Deposit", "Other"],
  ru: ["Карта", "Кредит", "Вклад", "Другое"],
};

export function QueueForm({
  locale,
  branches,
}: {
  locale: Locale;
  branches: string[];
}) {
  const t = copy(locale);
  const places = branches.length ? branches : locale === "ru" ? ["Учебный филиал"] : locale === "en" ? ["Sample branch"] : ["Nümunə filial"];
  const [fullName, setFullName] = useState("");
  const [phone, setPhone] = useState("");
  const [branch, setBranch] = useState(places[0]);
  const [service, setService] = useState(SERVICES[locale][0]);
  const [day, setDay] = useState("");
  const [time, setTime] = useState(TIMES[0]);
  const [status, setStatus] = useState<"idle" | "sending" | "success" | "error">("idle");
  const [code, setCode] = useState("");

  async function onSubmit(event: FormEvent) {
    event.preventDefault();
    setStatus("sending");
    const response = await fetch("/api/queues/", {
      method: "POST",
      headers: { "Content-Type": "application/json" },
      body: JSON.stringify({
        full_name: fullName,
        phone,
        branch_name: branch,
        service,
        visit_date: day,
        visit_time: time,
      }),
    });
    if (!response.ok) {
      setStatus("error");
      return;
    }
    const data = (await response.json()) as { code?: string };
    setCode(data.code ?? "");
    setStatus("success");
  }

  if (status === "success") {
    return (
      <div className="queue-done">
        <p>{locale === "ru" ? "Учебная очередь записана." : locale === "en" ? "Sample queue saved." : "Nümunə növbə yazıldı."}</p>
        <strong>{code}</strong>
        <span>
          {branch} · {service} · {day} · {time}
        </span>
      </div>
    );
  }

  return (
    <form className="form" onSubmit={onSubmit}>
      <label>
        {t.branch}
        <select value={branch} onChange={(event) => setBranch(event.target.value)}>
          {places.map((name) => (
            <option key={name}>{name}</option>
          ))}
        </select>
      </label>
      <label>
        {locale === "ru" ? "Услуга" : locale === "en" ? "Service" : "Xidmət"}
        <select value={service} onChange={(event) => setService(event.target.value)}>
          {SERVICES[locale].map((name) => (
            <option key={name}>{name}</option>
          ))}
        </select>
      </label>
      <label>
        {locale === "ru" ? "День" : locale === "en" ? "Day" : "Gün"}
        <input type="date" value={day} onChange={(event) => setDay(event.target.value)} required />
      </label>
      <label>
        {locale === "ru" ? "Время" : locale === "en" ? "Time" : "Saat"}
        <select value={time} onChange={(event) => setTime(event.target.value)}>
          {TIMES.map((slot) => (
            <option key={slot}>{slot}</option>
          ))}
        </select>
      </label>
      <label>
        {t.name}
        <input value={fullName} onChange={(event) => setFullName(event.target.value)} required minLength={2} />
      </label>
      <label>
        {t.phone}
        <input value={phone} onChange={(event) => setPhone(event.target.value)} required placeholder="+994501112233" />
      </label>
      <button className="button yellow" type="submit" disabled={status === "sending"}>
        {status === "sending" ? t.sending : t.queue}
      </button>
      {status === "error" ? <p className="error">{t.error}</p> : null}
    </form>
  );
}
