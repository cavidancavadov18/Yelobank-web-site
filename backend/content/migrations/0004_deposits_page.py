import django.db.models.deletion
from django.db import migrations, models


def create_deposits(apps, schema_editor):
    DepositsPage = apps.get_model("content", "DepositsPage")
    DepositsPageTranslation = apps.get_model("content", "DepositsPageTranslation")
    Product = apps.get_model("content", "Product")
    ProductTranslation = apps.get_model("content", "ProductTranslation")

    page = DepositsPage.objects.order_by("id").first() or DepositsPage.objects.create()
    copy = {
        "az": (
            "Əmanətlər",
            "Başlıq ortada və iridir. Bu mətn onun altında, daha kiçik və boz durur. Mətni admin paneldən dəyişin.",
        ),
        "en": (
            "Deposits",
            "The title is centered and large. This text sits under it, smaller and gray. Change it in the admin.",
        ),
        "ru": (
            "Вклады",
            "Заголовок по центру и крупный. Этот текст ниже, меньше и серый. Меняется в админ-панели.",
        ),
    }
    for language, (heading, lead) in copy.items():
        DepositsPageTranslation.objects.get_or_create(
            page=page,
            language=language,
            defaults={"heading": heading, "lead": lead},
        )

    if Product.objects.filter(slug="study-deposit").exists():
        return
    product = Product.objects.create(
        kind="deposit",
        slug="study-deposit",
        interest_rate="8.00",
        currency="AZN",
        min_amount="500",
        max_amount="20000",
        min_months=3,
        max_months=24,
        sort_order=1,
    )
    texts = {
        "az": {
            "title": "Study əmanət",
            "summary": "500-dən 20 000 AZN-dək nümunə müddətli əmanət.",
            "body": "İllik nümunə faiz 8-dir. Müraciət yalnız lokal bazaya yazılır.",
            "spec_1_label": "Məbləğ",
            "spec_1_value": "500 – 20 000 AZN",
            "spec_2_label": "Müddət",
            "spec_2_value": "3 – 24 ay",
            "spec_3_label": "İllik faiz",
            "spec_3_value": "8%",
            "spec_4_label": "Valyuta",
            "spec_4_value": "AZN",
            "order_label": "Müraciət",
            "more_label": "Ətraflı",
        },
        "en": {
            "title": "Study deposit",
            "summary": "A sample term deposit from 500 to 20,000 AZN.",
            "body": "The sample annual rate is 8 percent. An application is stored only in the local database.",
            "spec_1_label": "Amount",
            "spec_1_value": "500 – 20 000 AZN",
            "spec_2_label": "Term",
            "spec_2_value": "3 – 24 months",
            "spec_3_label": "Annual rate",
            "spec_3_value": "8%",
            "spec_4_label": "Currency",
            "spec_4_value": "AZN",
            "order_label": "Apply",
            "more_label": "Details",
        },
        "ru": {
            "title": "Study вклад",
            "summary": "Учебный срочный вклад от 500 до 20 000 AZN.",
            "body": "Учебная годовая ставка 8 процентов. Заявка пишется только в локальную базу.",
            "spec_1_label": "Сумма",
            "spec_1_value": "500 – 20 000 AZN",
            "spec_2_label": "Срок",
            "spec_2_value": "3 – 24 мес.",
            "spec_3_label": "Ставка",
            "spec_3_value": "8%",
            "spec_4_label": "Валюта",
            "spec_4_value": "AZN",
            "order_label": "Заявка",
            "more_label": "Подробнее",
        },
    }
    ProductTranslation.objects.bulk_create(
        [ProductTranslation(product=product, language=language, **fields) for language, fields in texts.items()]
    )


def remove_deposits(apps, schema_editor):
    DepositsPage = apps.get_model("content", "DepositsPage")
    Product = apps.get_model("content", "Product")
    DepositsPage.objects.all().delete()
    Product.objects.filter(slug="study-deposit").delete()


class Migration(migrations.Migration):

    dependencies = [
        ("content", "0003_loans_page"),
    ]

    operations = [
        migrations.AlterField(
            model_name="product",
            name="kind",
            field=models.CharField(
                choices=[("card", "Kart"), ("loan", "Kredit"), ("deposit", "Əmanət")],
                max_length=10,
                verbose_name="Növ",
            ),
        ),
        migrations.CreateModel(
            name="DepositsPage",
            fields=[
                ("id", models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name="ID")),
            ],
            options={
                "verbose_name": "Əmanətlər səhifəsi",
                "verbose_name_plural": "Əmanətlər səhifəsi",
            },
        ),
        migrations.CreateModel(
            name="DepositsPageTranslation",
            fields=[
                ("id", models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name="ID")),
                (
                    "language",
                    models.CharField(
                        choices=[("az", "AZ"), ("en", "EN"), ("ru", "RU")],
                        max_length=2,
                        verbose_name="Dil",
                    ),
                ),
                (
                    "heading",
                    models.CharField(
                        blank=True,
                        help_text="Səhifənin ortasındakı böyük yazı.",
                        max_length=80,
                        verbose_name="Böyük başlıq",
                    ),
                ),
                (
                    "lead",
                    models.TextField(
                        blank=True,
                        help_text="Başlığın altında, ortada, daha kiçik və boz.",
                        verbose_name="Boz mətn",
                    ),
                ),
                (
                    "page",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        related_name="translations",
                        to="content.depositspage",
                    ),
                ),
            ],
            options={
                "verbose_name": "Dil",
                "verbose_name_plural": "Başlıq və giriş mətni",
                "constraints": [
                    models.UniqueConstraint(fields=("page", "language"), name="uniq_deposits_page_language")
                ],
            },
        ),
        migrations.RunPython(create_deposits, remove_deposits),
    ]
