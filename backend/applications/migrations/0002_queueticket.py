from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("applications", "0001_initial"),
    ]

    operations = [
        migrations.CreateModel(
            name="QueueTicket",
            fields=[
                ("id", models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name="ID")),
                ("full_name", models.CharField(max_length=120, verbose_name="Ad və soyad")),
                ("phone", models.CharField(max_length=32, verbose_name="Telefon")),
                ("branch_name", models.CharField(max_length=160, verbose_name="Filial")),
                ("service", models.CharField(max_length=40, verbose_name="Xidmət")),
                ("visit_date", models.DateField(verbose_name="Gün")),
                ("visit_time", models.CharField(max_length=5, verbose_name="Saat")),
                ("code", models.CharField(max_length=8, unique=True, verbose_name="Növbə kodu")),
                ("created_at", models.DateTimeField(auto_now_add=True, verbose_name="Tarix")),
            ],
            options={
                "verbose_name": "Onlayn növbə",
                "verbose_name_plural": "Onlayn növbələr",
                "ordering": ["-created_at"],
            },
        ),
    ]
