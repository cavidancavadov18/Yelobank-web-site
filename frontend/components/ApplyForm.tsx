"use client";

import { FormEvent, useState } from "react";

import { copy, type Locale } from "@/lib/i18n";
import type { Product } from "@/lib/types";

export function ApplyForm({
  locale,
  products,
  initialSlug,
}: {
  locale: Locale;
  products: Product[];
  initialSlug?: string;
}) {
  const t = copy(locale);
  const [fullName, setFullName] = useState("");
  const [phone, setPhone] = useState("");
  const [product, setProduct] = useState(initialSlug ?? "");
  const [note, setNote] = useState("");
  const [status, setStatus] = useState<"idle" | "sending" | "success" | "error">("idle");

  async function onSubmit(event: FormEvent) {
    event.preventDefault();
    setStatus("sending");
    const selected = products.find((item) => item.slug === product);
    const response = await fetch("/api/applications/", {
      method: "POST",
      headers: { "Content-Type": "application/json" },
      body: JSON.stringify({
        full_name: fullName,
        phone,
        product: selected ? selected.id : null,
        note,
      }),
    });
    if (!response.ok) {
      setStatus("error");
      return;
    }
    setStatus("success");
    setFullName("");
    setPhone("");
    setNote("");
  }

  return (
    <form className="form" onSubmit={onSubmit}>
      <label>
        {t.name}
        <input value={fullName} onChange={(event) => setFullName(event.target.value)} required minLength={2} />
      </label>
      <label>
        {t.phone}
        <input value={phone} onChange={(event) => setPhone(event.target.value)} required placeholder="+994501112233" />
      </label>
      <label>
        {t.product}
        <select value={product} onChange={(event) => setProduct(event.target.value)}>
          <option value="">{t.none}</option>
          {products.map((item) => (
            <option key={item.slug} value={item.slug}>
              {item.title}
            </option>
          ))}
        </select>
      </label>
      <label>
        {t.note}
        <textarea value={note} onChange={(event) => setNote(event.target.value)} rows={4} />
      </label>
      <button className="button yellow" type="submit" disabled={status === "sending"}>
        {status === "sending" ? t.sending : t.send}
      </button>
      {status === "success" ? <p className="success">{t.success}</p> : null}
      {status === "error" ? <p className="error">{t.error}</p> : null}
    </form>
  );
}
