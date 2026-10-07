import { NextResponse } from "next/server";
import type { NextRequest } from "next/server";

const locales = ["az", "en", "ru"];

export function proxy(request: NextRequest) {
  const { pathname } = request.nextUrl;
  if (pathname === "/") {
    return NextResponse.redirect(new URL("/az", request.url));
  }
  const segment = pathname.split("/")[1];
  if (segment && !locales.includes(segment)) {
    return NextResponse.redirect(new URL("/az", request.url));
  }
  return NextResponse.next();
}

export const config = {
  matcher: ["/((?!_next|api|favicon.ico).*)"],
};
