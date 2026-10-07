import django.db.models.deletion
from django.db import migrations, models


def create_loans_page(apps, schema_editor):
    LoansPage = apps.get_model("content", "LoansPage")
    LoansPageTranslation = apps.get_model("content", "LoansPageTranslation")
    Product = apps.get_model("content", "Product")
    ProductTranslation = apps.get_model("content", "ProductTranslation")

    page = LoansPage.objects.order_by("id").first() or LoansPage.objects.create()
    copy = {
        "az": (
            "Kreditlər",
            "Başlıq ortada və iridir. Bu mətn onun altında, daha kiçik və boz durur. Mətni admin paneldən dəyişin.",
        ),
        "en": (
            "Loans",
            "The title is centered and large. This text sits under it, smaller and gray. Change it in the admin.",
        ),
        "ru": (
            "Кредиты",
            "Заголовок по центру и крупный. Этот текст ниже, меньше и серый. Меняется в админ-панели.",
        ),
    }
    for language, (heading, lead) in copy.items():
        LoansPageTranslation.objects.get_or_create(
            page=page,
            language=language,
            defaults={"heading": heading, "lead": lead},
        )

    samples = {
        "study-consumer": {
            "az": ("Məbləğ", "500 – 15 000 AZN", "Müddət", "6 – 36 ay", "İllik faiz", "18%", "FİFD", "nümunə", "Müraciət", "Ətraflı"),
            "en": ("Amount", "500 – 15 000 AZN", "Term", "6 – 36 months", "Annual rate", "18%", "APR", "sample", "Apply", "Details"),
            "ru": ("Сумма", "500 – 15 000 AZN", "Срок", "6 – 36 мес.", "Ставка", "18%", "ГЭСВ", "образец", "Заявка", "Подробнее"),
        },
        "study-cash": {
            "az": ("Məbləğ", "300 – 8 000 AZN", "Müddət", "3 – 24 ay", "İllik faiz", "22%", "FİFD", "nümunə", "Müraciət", "Ətraflı"),
            "en": ("Amount", "300 – 8 000 AZN", "Term", "3 – 24 months", "Annual rate", "22%", "APR", "sample", "Apply", "Details"),
            "ru": ("Сумма", "300 – 8 000 AZN", "Срок", "3 – 24 мес.", "Ставка", "22%", "ГЭСВ", "образец", "Заявка", "Подробнее"),
        },
    }
    for slug, languages in samples.items():
        product = Product.objects.filter(slug=slug).first()
        if product is None:
            continue
        for language, values in languages.items():
            translation = ProductTranslation.objects.filter(product=product, language=language).first()
            if translation is None or translation.spec_1_label:
                continue
            (
                translation.spec_1_label,
                translation.spec_1_value,
                translation.spec_2_label,
                translation.spec_2_value,
                translation.spec_3_label,
                translation.spec_3_value,
                translation.spec_4_label,
                translation.spec_4_value,
                translation.order_label,
                translation.more_label,
            ) = values
            translation.save()


def remove_loans_page(apps, schema_editor):
    LoansPage = apps.get_model("content", "LoansPage")
    LoansPage.objects.all().delete()


class Migration(migrations.Migration):

    dependencies = [
        ("content", "0002_cards_page"),
    ]

    operations = [
        migrations.AddField(
            model_name="producttranslation",
            name="spec_4_label",
            field=models.CharField(
                blank=True,
                default="",
                help_text="Kredit kartında dördüncü sütun. Kartda boş saxla.",
                max_length=40,
                verbose_name="4-cü ad",
            ),
        ),
        migrations.AddField(
            model_name="producttranslation",
            name="spec_4_value",
            field=models.CharField(blank=True, default="", max_length=80, verbose_name="4-cü dəyər"),
        ),
        migrations.AlterField(
            model_name="product",
            name="image",
            field=models.ImageField(
                blank=True,
                help_text="Kart səhifəsində sağdakı kart şəkli, kredit səhifəsində sağdakı banner. PNG və ya JPG.",
                null=True,
                upload_to="cards/",
                verbose_name="Şəkil",
            ),
        ),
        migrations.CreateModel(
            name="LoansPage",
            fields=[
                ("id", models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name="ID")),
            ],
            options={
                "verbose_name": "Kreditlər səhifəsi",
                "verbose_name_plural": "Kreditlər səhifəsi",
            },
        ),
        migrations.CreateModel(
            name="LoansPageTranslation",
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
                        to="content.loanspage",
                    ),
                ),
            ],
            options={
                "verbose_name": "Dil",
                "verbose_name_plural": "Başlıq və giriş mətni",
                "constraints": [
                    models.UniqueConstraint(fields=("page", "language"), name="uniq_loans_page_language")
                ],
            },
        ),
        migrations.RunPython(create_loans_page, remove_loans_page),
    ]
