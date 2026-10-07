LANGUAGES = {"az", "en", "ru"}


def clean_lang(value):
    if value in LANGUAGES:
        return value
    return "az"


def pick(translations, lang):
    by_language = {item.language: item for item in translations}
    return by_language.get(lang) or by_language.get("az")


def media_url(image):
    if not image:
        return ""
    from django.conf import settings

    base = getattr(settings, "PUBLIC_BASE_URL", "http://localhost:8000").rstrip("/")
    return f"{base}{image.url}"


def product_payload(product, lang, detail=False):
    translation = pick(product.translations.all(), lang)
    data = {
        "id": product.id,
        "slug": product.slug,
        "kind": product.kind,
        "title": translation.title if translation else product.slug,
        "summary": translation.summary if translation else "",
        "image": media_url(product.image),
        "spec_1_label": translation.spec_1_label if translation else "",
        "spec_1_value": translation.spec_1_value if translation else "",
        "spec_2_label": translation.spec_2_label if translation else "",
        "spec_2_value": translation.spec_2_value if translation else "",
        "spec_3_label": translation.spec_3_label if translation else "",
        "spec_3_value": translation.spec_3_value if translation else "",
        "spec_4_label": translation.spec_4_label if translation else "",
        "spec_4_value": translation.spec_4_value if translation else "",
        "order_label": translation.order_label if translation else "",
        "more_label": translation.more_label if translation else "",
        "interest_rate": product.interest_rate,
        "currency": product.currency,
        "min_amount": product.min_amount,
        "max_amount": product.max_amount,
        "min_months": product.min_months,
        "max_months": product.max_months,
    }
    if detail:
        data["body"] = translation.body if translation else ""
    return data


def news_payload(post, lang, detail=False):
    translation = pick(post.translations.all(), lang)
    data = {
        "slug": post.slug,
        "title": translation.title if translation else post.slug,
        "summary": translation.summary if translation else "",
        "published_at": post.published_at,
    }
    if detail:
        data["body"] = translation.body if translation else ""
    return data


def branch_payload(branch, lang):
    translation = pick(branch.translations.all(), lang)
    return {
        "id": branch.id,
        "kind": branch.kind,
        "name": translation.name if translation else "",
        "address": translation.address if translation else "",
        "hours": translation.hours if translation else "",
        "map_url": branch.map_url,
    }


def banner_payload(banner, lang):
    translation = pick(banner.translations.all(), lang)
    return {
        "id": banner.id,
        "title": translation.title if translation else "",
        "subtitle": translation.subtitle if translation else "",
        "href": banner.href,
    }


def cashback_payload(page, packs, lang):
    translation = pick(page.translations.all(), lang) if page is not None else None
    pack_rows = []
    for pack in packs:
        row = pick(pack.translations.all(), lang)
        if row is None:
            continue
        items = []
        for index in (1, 2, 3):
            title = getattr(row, f"item_{index}_title")
            text = getattr(row, f"item_{index}_text")
            if title or text:
                items.append({"title": title, "text": text})
        pack_rows.append(
            {
                "id": pack.slug,
                "label": row.label,
                "note": row.note,
                "items": items,
            }
        )
    return {
        "title": translation.heading if translation else "",
        "button": translation.button_label if translation else "",
        "packs": pack_rows,
    }


def cards_page_payload(page, lang):
    if page is None:
        return {"heading": "", "lead": ""}
    translation = pick(page.translations.all(), lang)
    return {
        "heading": translation.heading if translation else "",
        "lead": translation.lead if translation else "",
    }


def rate_payload(rate):
    return {
        "currency": rate.currency,
        "buy": rate.buy,
        "sell": rate.sell,
    }
