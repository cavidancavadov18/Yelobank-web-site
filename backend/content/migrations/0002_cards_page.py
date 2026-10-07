import django.db.models.deletion
from django.db import migrations, models


def create_cards_page(apps, schema_editor):
    CardsPage = apps.get_model("content", "CardsPage")
    CardsPageTranslation = apps.get_model("content", "CardsPageTranslation")
    if CardsPage.objects.exists():
        page = CardsPage.objects.order_by("id").first()
    else:
        page = CardsPage.objects.create()
    for language in ("az", "en", "ru"):
        CardsPageTranslation.objects.get_or_create(
            page=page,
            language=language,
            defaults={"heading": "", "lead": ""},
        )


def remove_cards_page(apps, schema_editor):
    CardsPage = apps.get_model("content", "CardsPage")
    CardsPage.objects.all().delete()


class Migration(migrations.Migration):

    dependencies = [
        ("content", "0001_initial"),
    ]

    operations = [
        migrations.AddField(
            model_name="product",
            name="image",
            field=models.ImageField(
                blank=True,
                null=True,
                help_text="Sağdakı kartın şəkli. PNG və ya JPG yüklə.",
                upload_to="cards/",
                verbose_name="Kartın şəkli",
            ),
        ),
        migrations.AlterField(
            model_name="producttranslation",
            name="title",
            field=models.CharField(
                help_text="Kartdakı qalın başlıq.",
                max_length=160,
                verbose_name="Böyük başlıq",
            ),
        ),
        migrations.AlterField(
            model_name="producttranslation",
            name="summary",
            field=models.CharField(
                blank=True,
                help_text="Başlığın altındakı boz sətir.",
                max_length=280,
                verbose_name="Alt başlıq",
            ),
        ),
        migrations.AlterField(
            model_name="producttranslation",
            name="body",
            field=models.TextField(blank=True, verbose_name="Detal mətni"),
        ),
        migrations.AddField(
            model_name="producttranslation",
            name="spec_1_label",
            field=models.CharField(blank=True, default="", help_text="Məsələn: Müddət", max_length=40, verbose_name="1-ci ad"),
        ),
        migrations.AddField(
            model_name="producttranslation",
            name="spec_1_value",
            field=models.CharField(blank=True, default="", help_text="Məsələn: 5 il", max_length=80, verbose_name="1-ci dəyər"),
        ),
        migrations.AddField(
            model_name="producttranslation",
            name="spec_2_label",
            field=models.CharField(blank=True, default="", max_length=40, verbose_name="2-ci ad"),
        ),
        migrations.AddField(
            model_name="producttranslation",
            name="spec_2_value",
            field=models.CharField(blank=True, default="", max_length=80, verbose_name="2-ci dəyər"),
        ),
        migrations.AddField(
            model_name="producttranslation",
            name="spec_3_label",
            field=models.CharField(blank=True, default="", max_length=40, verbose_name="3-cü ad"),
        ),
        migrations.AddField(
            model_name="producttranslation",
            name="spec_3_value",
            field=models.CharField(blank=True, default="", max_length=80, verbose_name="3-cü dəyər"),
        ),
        migrations.AddField(
            model_name="producttranslation",
            name="order_label",
            field=models.CharField(
                blank=True,
                default="",
                help_text="Əyri qara düymənin yazısı.",
                max_length=40,
                verbose_name="Qara düymə",
            ),
        ),
        migrations.AddField(
            model_name="producttranslation",
            name="more_label",
            field=models.CharField(
                blank=True,
                default="",
                help_text="Düymənin yanındakı link.",
                max_length=40,
                verbose_name="Oxlu link",
            ),
        ),
        migrations.CreateModel(
            name="CardsPage",
            fields=[
                ("id", models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name="ID")),
            ],
            options={
                "verbose_name": "Kartlar səhifəsi",
                "verbose_name_plural": "Kartlar səhifəsi",
            },
        ),
        migrations.CreateModel(
            name="CardsPageTranslation",
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
                        to="content.cardspage",
                    ),
                ),
            ],
            options={
                "verbose_name": "Dil",
                "verbose_name_plural": "Başlıq və giriş mətni",
                "constraints": [
                    models.UniqueConstraint(fields=("page", "language"), name="uniq_cards_page_language")
                ],
            },
        ),
        migrations.RunPython(create_cards_page, remove_cards_page),
    ]
