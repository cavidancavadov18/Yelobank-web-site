export type Product = {
  id: number;
  slug: string;
  kind: "card" | "loan" | "deposit";
  title: string;
  summary: string;
  image: string;
  spec_1_label: string;
  spec_1_value: string;
  spec_2_label: string;
  spec_2_value: string;
  spec_3_label: string;
  spec_3_value: string;
  spec_4_label: string;
  spec_4_value: string;
  order_label: string;
  more_label: string;
  body?: string;
  interest_rate: string;
  currency: string;
  min_amount: string;
  max_amount: string;
  min_months: number;
  max_months: number;
};

export type NewsItem = {
  slug: string;
  title: string;
  summary: string;
  body?: string;
  published_at: string;
};

export type Branch = {
  id: number;
  kind: "branch" | "atm";
  name: string;
  address: string;
  hours: string;
  map_url: string;
};

export type Banner = {
  id: number;
  title: string;
  subtitle: string;
  href: string;
};

export type Rate = {
  currency: string;
  buy: string;
  sell: string;
};

export type CashbackCopy = {
  title: string;
  button: string;
  packs: { id: string; label: string; note: string; items: { title: string; text: string }[] }[];
};

export type CardsPageCopy = {
  heading: string;
  lead: string;
};

export type HomePayload = {
  banners: Banner[];
  cards: Product[];
  loans: Product[];
  deposits: Product[];
  rates: Rate[];
};
