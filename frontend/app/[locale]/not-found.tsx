import Link from "next/link";

export default function NotFound() {
  return (
    <section className="section">
      <h1>404</h1>
      <Link className="button" href="/az">
        Yelo Study
      </Link>
    </section>
  );
}
