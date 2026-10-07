from datetime import datetime
from zoneinfo import ZoneInfo

from django.core.management.base import BaseCommand
from django.db import transaction

from content.models import (
    Banner,
    BannerTranslation,
    Branch,
    BranchTranslation,
    ExchangeRate,
    NewsPost,
    NewsTranslation,
    Product,
    ProductTranslation,
)

BAKU = ZoneInfo("Asia/Baku")


def translations(rows):
    return [{"language": lang, **fields} for lang, fields in rows]


class Command(BaseCommand):
    help = "Load short original sample content once."

    def handle(self, *args, **options):
        if Product.objects.exists():
            self.stdout.write("Sample content already loaded.")
            return

        with transaction.atomic():
            self.load()
        self.stdout.write("Sample content loaded.")

    def load(self):
        products = [
            {
                "kind": "card",
                "slug": "study-debit",
                "interest_rate": "0.00",
                "currency": "AZN",
                "min_amount": "0",
                "max_amount": "0",
                "min_months": 12,
                "max_months": 36,
                "sort_order": 1,
                "translations": translations(
                    [
                        (
                            "az",
                            {
                                "title": "Study Debit",
                                "summary": "Gündəlik ödənişlər üçün nümunə debet kartı.",
                                "body": "Bu kart lokal dərs layihəsinin nümunəsidir. Balans, PIN və real ödəniş yoxdur. Admin paneldən mətnini dəyişib saytda necə göründüyünü yoxlaya bilərsən.",
                            },
                        ),
                        (
                            "en",
                            {
                                "title": "Study Debit",
                                "summary": "A sample debit card for everyday payments.",
                                "body": "This card is sample copy for a local study project. There is no balance, PIN, or real payment. Change the text in the admin and see it on the site.",
                            },
                        ),
                        (
                            "ru",
                            {
                                "title": "Study Debit",
                                "summary": "Учебная дебетовая карта для повседневных платежей.",
                                "body": "Это учебный текст локального проекта. Баланса, PIN и реальных платежей нет. Измени текст в админке и посмотри его на сайте.",
                            },
                        ),
                    ]
                ),
            },
            {
                "kind": "card",
                "slug": "study-cashback",
                "interest_rate": "0.00",
                "currency": "AZN",
                "min_amount": "0",
                "max_amount": "0",
                "min_months": 12,
                "max_months": 24,
                "sort_order": 2,
                "translations": translations(
                    [
                        (
                            "az",
                            {
                                "title": "Study Cashback",
                                "summary": "Seçilmiş kateqoriyada nümunə geri ödəmə.",
                                "body": "Nümunə şərt: ərzaqda 5 faizə qədər geri ödəmə. Rəqəm real kampaniya deyil, admin-də dəyişmək üçündür.",
                            },
                        ),
                        (
                            "en",
                            {
                                "title": "Study Cashback",
                                "summary": "Sample cashback in a chosen category.",
                                "body": "Sample term: up to 5 percent back on groceries. The figure is not a real offer. Edit it in the admin.",
                            },
                        ),
                        (
                            "ru",
                            {
                                "title": "Study Cashback",
                                "summary": "Учебный кешбэк в выбранной категории.",
                                "body": "Учебное условие: до 5 процентов за продукты. Цифра не является реальным предложением. Меняй её в админке.",
                            },
                        ),
                    ]
                ),
            },
            {
                "kind": "loan",
                "slug": "study-consumer",
                "interest_rate": "18.00",
                "currency": "AZN",
                "min_amount": "500",
                "max_amount": "15000",
                "min_months": 6,
                "max_months": 36,
                "sort_order": 1,
                "translations": translations(
                    [
                        (
                            "az",
                            {
                                "title": "Study istehlak krediti",
                                "summary": "500-dən 15 000 AZN-dək nümunə istehlak krediti.",
                                "body": "İllik nümunə faiz 18-dir. Aylıq ödənişi səhifədəki kalkulyator hesablayır. Müraciət yalnız lokal bazaya yazılır.",
                            },
                        ),
                        (
                            "en",
                            {
                                "title": "Study consumer loan",
                                "summary": "A sample consumer loan from 500 to 15,000 AZN.",
                                "body": "The sample annual rate is 18 percent. The calculator on this page estimates the monthly payment. An application is stored only in the local database.",
                            },
                        ),
                        (
                            "ru",
                            {
                                "title": "Study потребительский кредит",
                                "summary": "Учебный кредит от 500 до 15 000 AZN.",
                                "body": "Учебная годовая ставка 18 процентов. Калькулятор на странице считает ежемесячный платёж. Заявка сохраняется только в локальной базе.",
                            },
                        ),
                    ]
                ),
            },
            {
                "kind": "loan",
                "slug": "study-cash",
                "interest_rate": "22.00",
                "currency": "AZN",
                "min_amount": "300",
                "max_amount": "8000",
                "min_months": 3,
                "max_months": 24,
                "sort_order": 2,
                "translations": translations(
                    [
                        (
                            "az",
                            {
                                "title": "Study nağd kredit",
                                "summary": "Qısa müddətli nümunə nağd kredit.",
                                "body": "300-dən 8 000 AZN-dək, 3 aydan 24 aya qədər. Şərtləri admin panelində dəyiş, kalkulyator yeni rəqəmi götürəcək.",
                            },
                        ),
                        (
                            "en",
                            {
                                "title": "Study cash loan",
                                "summary": "A short sample cash loan.",
                                "body": "From 300 to 8,000 AZN, for 3 to 24 months. Change the terms in the admin and the calculator will use the new numbers.",
                            },
                        ),
                        (
                            "ru",
                            {
                                "title": "Study наличный кредит",
                                "summary": "Короткий учебный кредит наличными.",
                                "body": "От 300 до 8 000 AZN, на срок от 3 до 24 месяцев. Измени условия в админке, и калькулятор возьмёт новые цифры.",
                            },
                        ),
                    ]
                ),
            },
        ]

        for item in products:
            rows = item.pop("translations")
            product = Product.objects.create(**item)
            ProductTranslation.objects.bulk_create(
                [ProductTranslation(product=product, **row) for row in rows]
            )

        news_items = [
            {
                "slug": "study-hours",
                "published_at": datetime(2026, 9, 12, 10, 0, tzinfo=BAKU),
                "translations": translations(
                    [
                        (
                            "az",
                            {
                                "title": "Nümunə iş saatı",
                                "summary": "Dərs layihəsində filial saatı necə göstərilir.",
                                "body": "Bu xəbər uydurma elandır. Məqsəd xəbər siyahısı, detal səhifəsi və üç dilin admin-dən idarəsini öyrənməkdir.",
                            },
                        ),
                        (
                            "en",
                            {
                                "title": "Sample opening hours",
                                "summary": "How branch hours appear in the study project.",
                                "body": "This story is fictional. It exists so you can learn the news list, the detail page, and three languages in the admin.",
                            },
                        ),
                        (
                            "ru",
                            {
                                "title": "Учебные часы работы",
                                "summary": "Как в учебном проекте показываются часы филиала.",
                                "body": "Эта новость выдумана. Она нужна, чтобы изучить список, страницу новости и три языка в админке.",
                            },
                        ),
                    ]
                ),
            },
            {
                "slug": "study-app-update",
                "published_at": datetime(2026, 8, 3, 12, 0, tzinfo=BAKU),
                "translations": translations(
                    [
                        (
                            "az",
                            {
                                "title": "Saytın lokal versiyası",
                                "summary": "Bu layihə serverə çıxarılmır.",
                                "body": "Frontend Next.js, məzmun Django admin, məlumatlar PostgreSQL-dədir. Hamısı Docker ilə sənin kompüterində işləyir.",
                            },
                        ),
                        (
                            "en",
                            {
                                "title": "The local version of the site",
                                "summary": "This project is not deployed.",
                                "body": "The frontend is Next.js, content is edited in Django admin, and data lives in PostgreSQL. Docker runs all of it on your computer.",
                            },
                        ),
                        (
                            "ru",
                            {
                                "title": "Локальная версия сайта",
                                "summary": "Этот проект никуда не публикуется.",
                                "body": "Фронтенд на Next.js, контент правится в Django admin, данные лежат в PostgreSQL. Docker запускает всё на твоём компьютере.",
                            },
                        ),
                    ]
                ),
            },
        ]

        for item in news_items:
            rows = item.pop("translations")
            post = NewsPost.objects.create(**item)
            NewsTranslation.objects.bulk_create(
                [NewsTranslation(news=post, **row) for row in rows]
            )

        branches = [
            {
                "kind": "branch",
                "map_url": "https://www.google.com/maps/search/?api=1&query=Baku",
                "sort_order": 1,
                "translations": translations(
                    [
                        ("az", {"name": "Study Mərkəz", "address": "Bakı, Nümunə prospekti 1", "hours": "B.e.–C. 09:00–18:00"}),
                        ("en", {"name": "Study Center", "address": "Baku, Sample avenue 1", "hours": "Mon–Fri 09:00–18:00"}),
                        ("ru", {"name": "Study Центр", "address": "Баку, Учебный проспект 1", "hours": "Пн–Пт 09:00–18:00"}),
                    ]
                ),
            },
            {
                "kind": "branch",
                "map_url": "https://www.google.com/maps/search/?api=1&query=Baku",
                "sort_order": 2,
                "translations": translations(
                    [
                        ("az", {"name": "Study Sahil", "address": "Bakı, Nümunə küçəsi 8", "hours": "B.e.–Ş. 10:00–17:00"}),
                        ("en", {"name": "Study Seaside", "address": "Baku, Sample street 8", "hours": "Mon–Sat 10:00–17:00"}),
                        ("ru", {"name": "Study Приморский", "address": "Баку, Учебная улица 8", "hours": "Пн–Сб 10:00–17:00"}),
                    ]
                ),
            },
            {
                "kind": "atm",
                "map_url": "https://www.google.com/maps/search/?api=1&query=Baku",
                "sort_order": 3,
                "translations": translations(
                    [
                        ("az", {"name": "Study ATM", "address": "Bakı, Nümunə meydanı", "hours": "24 saat"}),
                        ("en", {"name": "Study ATM", "address": "Baku, Sample square", "hours": "24 hours"}),
                        ("ru", {"name": "Study ATM", "address": "Баку, Учебная площадь", "hours": "круглосуточно"}),
                    ]
                ),
            },
        ]

        for item in branches:
            rows = item.pop("translations")
            branch = Branch.objects.create(**item)
            BranchTranslation.objects.bulk_create(
                [BranchTranslation(branch=branch, **row) for row in rows]
            )

        ExchangeRate.objects.create(currency="USD", buy="1.6900", sell="1.7050")
        ExchangeRate.objects.create(currency="EUR", buy="1.8400", sell="1.8700")

        banners = [
            {
                "href": "/cards/study-debit",
                "sort_order": 1,
                "translations": translations(
                    [
                        ("az", {"title": "Study kartı", "subtitle": "Gündəlik ödəniş üçün sadə nümunə kart."}),
                        ("en", {"title": "Study card", "subtitle": "A simple sample card for everyday payments."}),
                        ("ru", {"title": "Карта Study", "subtitle": "Простая учебная карта для ежедневных платежей."}),
                    ]
                ),
            },
            {
                "href": "/loans/study-consumer",
                "sort_order": 2,
                "translations": translations(
                    [
                        ("az", {"title": "Study krediti", "subtitle": "Məbləği və müddəti kalkulyatorda yoxla."}),
                        ("en", {"title": "Study loan", "subtitle": "Check the amount and term in the calculator."}),
                        ("ru", {"title": "Кредит Study", "subtitle": "Проверь сумму и срок в калькуляторе."}),
                    ]
                ),
            },
        ]

        for item in banners:
            rows = item.pop("translations")
            banner = Banner.objects.create(**item)
            BannerTranslation.objects.bulk_create(
                [BannerTranslation(banner=banner, **row) for row in rows]
            )
