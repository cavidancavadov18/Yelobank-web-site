import django.db.models.deletion
from django.db import migrations, models


def seed_cashback(apps, schema_editor):
    CashbackPage = apps.get_model("content", "CashbackPage")
    CashbackPageTranslation = apps.get_model("content", "CashbackPageTranslation")
    CashbackPack = apps.get_model("content", "CashbackPack")
    CashbackPackTranslation = apps.get_model("content", "CashbackPackTranslation")

    page = CashbackPage.objects.order_by("id").first() or CashbackPage.objects.create()
    page_copy = {
        "az": ("Nümunə keşbek kartı", "Sifariş et"),
        "en": ("Sample cashback card", "Order"),
        "ru": ("Учебная карта кешбэка", "Заказать"),
    }
    for language, (heading, button_label) in page_copy.items():
        CashbackPageTranslation.objects.get_or_create(
            page=page,
            language=language,
            defaults={"heading": heading, "button_label": button_label},
        )

    packs = {
        "simple": {
            "sort_order": 1,
            "az": ("Sadə", "Nümunə paket. Rəqəmlər real tarif deyil.", "Market", "Nümunə market ödənişində 2% geri qayıdır.", "Kafe", "Nümunə kafe ödənişində 2% geri qayıdır.", "Geyim", "Nümunə geyim alışında 3% geri qayıdır."),
            "en": ("Simple", "Sample pack. The figures are not a real tariff.", "Grocery", "Sample grocery payments return 2%.", "Cafe", "Sample cafe payments return 2%.", "Clothes", "Sample clothing payments return 3%."),
            "ru": ("Простой", "Учебный пакет. Цифры не являются тарифом.", "Маркет", "Учебный возврат 2% за оплату в маркете.", "Кафе", "Учебный возврат 2% за оплату в кафе.", "Одежда", "Учебный возврат 3% за одежду."),
        },
        "mid": {
            "sort_order": 2,
            "az": ("Orta", "Nümunə paket. Rəqəmlər real tarif deyil.", "Market", "Nümunə market ödənişində 4% geri qayıdır.", "Kafe", "Nümunə kafe ödənişində 4% geri qayıdır.", "Nəqliyyat", "Nümunə nəqliyyat ödənişində 3% geri qayıdır."),
            "en": ("Middle", "Sample pack. The figures are not a real tariff.", "Grocery", "Sample grocery payments return 4%.", "Cafe", "Sample cafe payments return 4%.", "Transit", "Sample transit payments return 3%."),
            "ru": ("Средний", "Учебный пакет. Цифры не являются тарифом.", "Маркет", "Учебный возврат 4% за оплату в маркете.", "Кафе", "Учебный возврат 4% за оплату в кафе.", "Транспорт", "Учебный возврат 3% за транспорт."),
        },
        "wide": {
            "sort_order": 3,
            "az": ("Geniş", "Nümunə paket. Rəqəmlər real tarif deyil.", "Market", "Nümunə market ödənişində 6% geri qayıdır.", "Kafe", "Nümunə kafe ödənişində 6% geri qayıdır.", "Əyləncə", "Nümunə əyləncə ödənişində 5% geri qayıdır."),
            "en": ("Wide", "Sample pack. The figures are not a real tariff.", "Grocery", "Sample grocery payments return 6%.", "Cafe", "Sample cafe payments return 6%.", "Leisure", "Sample leisure payments return 5%."),
            "ru": ("Широкий", "Учебный пакет. Цифры не являются тарифом.", "Маркет", "Учебный возврат 6% за оплату в маркете.", "Кафе", "Учебный возврат 6% за оплату в кафе.", "Досуг", "Учебный возврат 5% за досуг."),
        },
    }
    for slug, data in packs.items():
        if CashbackPack.objects.filter(slug=slug).exists():
            continue
        pack = CashbackPack.objects.create(slug=slug, sort_order=data["sort_order"])
        for language in ("az", "en", "ru"):
            label, note, t1, x1, t2, x2, t3, x3 = data[language]
            CashbackPackTranslation.objects.create(
                pack=pack,
                language=language,
                label=label,
                note=note,
                item_1_title=t1,
                item_1_text=x1,
                item_2_title=t2,
                item_2_text=x2,
                item_3_title=t3,
                item_3_text=x3,
            )


def remove_cashback(apps, schema_editor):
    apps.get_model("content", "CashbackPage").objects.all().delete()
    apps.get_model("content", "CashbackPack").objects.all().delete()


class Migration(migrations.Migration):

    dependencies = [
        ("content", "0005_deposit_offer_copy"),
    ]

    operations = [
        migrations.CreateModel(
            name="CashbackPage",
            fields=[
                ("id", models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name="ID")),
            ],
            options={"verbose_name": "Keşbek səhifəsi", "verbose_name_plural": "Keşbek səhifəsi"},
        ),
        migrations.CreateModel(
            name="CashbackPack",
            fields=[
                ("id", models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name="ID")),
                ("slug", models.SlugField(unique=True, verbose_name="Slug")),
                ("sort_order", models.PositiveIntegerField(default=0, verbose_name="Sıra")),
                ("is_published", models.BooleanField(default=True, verbose_name="Dərc")),
            ],
            options={
                "verbose_name": "Keşbek paketi",
                "verbose_name_plural": "Keşbek paketləri",
                "ordering": ["sort_order", "id"],
            },
        ),
        migrations.CreateModel(
            name="CashbackPageTranslation",
            fields=[
                ("id", models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name="ID")),
                ("language", models.CharField(choices=[("az", "AZ"), ("en", "EN"), ("ru", "RU")], max_length=2, verbose_name="Dil")),
                ("heading", models.CharField(blank=True, max_length=120, verbose_name="Böyük başlıq")),
                ("button_label", models.CharField(blank=True, max_length=40, verbose_name="Sarı düymə")),
                (
                    "page",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        related_name="translations",
                        to="content.cashbackpage",
                    ),
                ),
            ],
            options={"verbose_name": "Dil", "verbose_name_plural": "Başlıq və düymə"},
        ),
        migrations.CreateModel(
            name="CashbackPackTranslation",
            fields=[
                ("id", models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name="ID")),
                ("language", models.CharField(choices=[("az", "AZ"), ("en", "EN"), ("ru", "RU")], max_length=2, verbose_name="Dil")),
                ("label", models.CharField(blank=True, max_length=40, verbose_name="Paket adı")),
                ("note", models.CharField(blank=True, max_length=280, verbose_name="Qeyd")),
                ("item_1_title", models.CharField(blank=True, max_length=80, verbose_name="1-ci kateqoriya")),
                ("item_1_text", models.CharField(blank=True, max_length=280, verbose_name="1-ci mətn")),
                ("item_2_title", models.CharField(blank=True, max_length=80, verbose_name="2-ci kateqoriya")),
                ("item_2_text", models.CharField(blank=True, max_length=280, verbose_name="2-ci mətn")),
                ("item_3_title", models.CharField(blank=True, max_length=80, verbose_name="3-cü kateqoriya")),
                ("item_3_text", models.CharField(blank=True, max_length=280, verbose_name="3-cü mətn")),
                (
                    "pack",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        related_name="translations",
                        to="content.cashbackpack",
                    ),
                ),
            ],
            options={"verbose_name": "Dil", "verbose_name_plural": "Paket yazıları"},
        ),
        migrations.AddConstraint(
            model_name="cashbackpagetranslation",
            constraint=models.UniqueConstraint(fields=("page", "language"), name="uniq_cashback_page_language"),
        ),
        migrations.AddConstraint(
            model_name="cashbackpacktranslation",
            constraint=models.UniqueConstraint(fields=("pack", "language"), name="uniq_cashback_pack_language"),
        ),
        migrations.RunPython(seed_cashback, remove_cashback),
    ]
