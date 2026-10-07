import type { Metadata } from "next";
import { notFound } from "next/navigation";

import { apiGet } from "@/lib/api";
import { copy, isLocale } from "@/lib/i18n";
import type { Branch } from "@/lib/types";

export const metadata: Metadata = { title: "Branches" };

export default async function BranchesPage({ params }: { params: Promise<{ locale: string }> }) {
  const { locale } = await params;
  if (!isLocale(locale)) notFound();
  const t = copy(locale);
  const branches = await apiGet<Branch[]>(`/api/branches/?lang=${locale}`);
  if (!branches) notFound();

  return (
    <section className="section">
      <h1>{t.branches}</h1>
      <p className="lead">{t.branchesLead}</p>
      <div className="places" style={{ marginTop: 16 }}>
        {branches.map((place) => (
          <article key={place.id} className="place">
            <span className="kind">{place.kind === "atm" ? t.atm : t.branch}</span>
            <h3>{place.name}</h3>
            <p>{place.address}</p>
            <p className="meta">
              {t.hours}: {place.hours}
            </p>
            {place.map_url ? (
              <a className="button" href={place.map_url} target="_blank" rel="noreferrer">
                {t.map}
              </a>
            ) : null}
          </article>
        ))}
      </div>
    </section>
  );
}
