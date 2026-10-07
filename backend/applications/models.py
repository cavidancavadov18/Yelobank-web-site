from django.db import models

from content.models import Product


class ApplicationStatus(models.TextChoices):
    NEW = "new", "Yeni"
    SEEN = "seen", "Baxılıb"


class Application(models.Model):
    full_name = models.CharField("Ad və soyad", max_length=120)
    phone = models.CharField("Telefon", max_length=32)
    product = models.ForeignKey(
        Product,
        verbose_name="Məhsul",
        null=True,
        blank=True,
        on_delete=models.SET_NULL,
        related_name="applications",
    )
    note = models.TextField("Qeyd", blank=True)
    status = models.CharField(
        "Status",
        max_length=10,
        choices=ApplicationStatus.choices,
        default=ApplicationStatus.NEW,
    )
    created_at = models.DateTimeField("Tarix", auto_now_add=True)

    class Meta:
        ordering = ["-created_at"]
        verbose_name = "Müraciət"
        verbose_name_plural = "Müraciətlər"

    def __str__(self):
        return f"{self.full_name} ({self.phone})"


class QueueTicket(models.Model):
    full_name = models.CharField("Ad və soyad", max_length=120)
    phone = models.CharField("Telefon", max_length=32)
    branch_name = models.CharField("Filial", max_length=160)
    service = models.CharField("Xidmət", max_length=40)
    visit_date = models.DateField("Gün")
    visit_time = models.CharField("Saat", max_length=5)
    code = models.CharField("Növbə kodu", max_length=8, unique=True)
    created_at = models.DateTimeField("Tarix", auto_now_add=True)

    class Meta:
        ordering = ["-created_at"]
        verbose_name = "Onlayn növbə"
        verbose_name_plural = "Onlayn növbələr"

    def __str__(self):
        return f"{self.code} · {self.branch_name}"
