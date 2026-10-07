from django.db import migrations


def update_deposit_copy(apps, schema_editor):
    Product = apps.get_model("content", "Product")
    ProductTranslation = apps.get_model("content", "ProductTranslation")
    DepositsPageTranslation = apps.get_model("content", "DepositsPageTranslation")

    leads = {
        "az": "Nümunə əmanət şərtləri. Rəqəmlər real tarif deyil.",
        "en": "Sample deposit terms. The figures are not a real tariff.",
        "ru": "Учебные условия вклада. Цифры не являются реальным тарифом.",
    }
    for language, lead in leads.items():
        DepositsPageTranslation.objects.filter(language=language).update(lead=lead)

    product = Product.objects.filter(slug="study-deposit").first()
    if product is None:
        return
    product.min_amount = "100"
    product.min_months = 3
    product.max_months = 24
    product.save(update_fields=["min_amount", "min_months", "max_months"])

    texts = {
        "az": {
            "title": "Study sabit",
            "summary": "Nümunə müddətli əmanət.",
            "spec_1_label": "Məbləğ",
            "spec_1_value": "min. 100\nAZN",
            "spec_2_label": "Müddət",
            "spec_2_value": "3 / 6 / 12 / 18 /\n24 ay",
            "spec_3_label": "Faizlərin ödənişi",
            "spec_3_value": "nümunə, aylıq və ya\nsonda",
            "spec_4_label": "",
            "spec_4_value": "",
            "order_label": "",
            "more_label": "Daha ətraflı",
        },
        "en": {
            "title": "Study fixed",
            "summary": "A sample term deposit.",
            "spec_1_label": "Amount",
            "spec_1_value": "min. 100\nAZN",
            "spec_2_label": "Term",
            "spec_2_value": "3 / 6 / 12 / 18 /\n24 months",
            "spec_3_label": "Interest payment",
            "spec_3_value": "sample, monthly or\nat the end",
            "spec_4_label": "",
            "spec_4_value": "",
            "order_label": "",
            "more_label": "More details",
        },
        "ru": {
            "title": "Study фиксированный",
            "summary": "Учебный срочный вклад.",
            "spec_1_label": "Сумма",
            "spec_1_value": "мин. 100\nAZN",
            "spec_2_label": "Срок",
            "spec_2_value": "3 / 6 / 12 / 18 /\n24 мес.",
            "spec_3_label": "Выплата процентов",
            "spec_3_value": "учебно, ежемесячно\nили в конце",
            "spec_4_label": "",
            "spec_4_value": "",
            "order_label": "",
            "more_label": "Подробнее",
        },
    }
    for language, fields in texts.items():
        ProductTranslation.objects.filter(product=product, language=language).update(**fields)


def restore_deposit_copy(apps, schema_editor):
    Product = apps.get_model("content", "Product")
    ProductTranslation = apps.get_model("content", "ProductTranslation")
    DepositsPageTranslation = apps.get_model("content", "DepositsPageTranslation")
    leads = {
        "az": "Başlıq ortada və iridir. Bu mətn onun altında, daha kiçik və boz durur. Mətni admin paneldən dəyişin.",
        "en": "The title is centered and large. This text sits under it, smaller and gray. Change it in the admin.",
        "ru": "Заголовок по центру и крупный. Этот текст ниже, меньше и серый. Меняется в админ-панели.",
    }
    for language, lead in leads.items():
        DepositsPageTranslation.objects.filter(language=language).update(lead=lead)
    product = Product.objects.filter(slug="study-deposit").first()
    if product is None:
        return
    product.min_amount = "500"
    product.save(update_fields=["min_amount"])
    texts = {
        "az": {
            "title": "Study əmanət",
            "summary": "500-dən 20 000 AZN-dək nümunə müddətli əmanət.",
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
    for language, fields in texts.items():
        ProductTranslation.objects.filter(product=product, language=language).update(**fields)


class Migration(migrations.Migration):

    dependencies = [
        ("content", "0004_deposits_page"),
    ]

    operations = [
        migrations.RunPython(update_deposit_copy, restore_deposit_copy),
    ]
