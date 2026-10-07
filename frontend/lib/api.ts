export async function apiGet<T>(path: string): Promise<T | null> {
  const base = process.env.API_URL || "http://backend:8000";
  const response = await fetch(`${base}${path}`, { cache: "no-store" });
  if (response.status === 404) {
    return null;
  }
  if (!response.ok) {
    throw new Error(`API ${response.status} for ${path}`);
  }
  return response.json() as Promise<T>;
}
