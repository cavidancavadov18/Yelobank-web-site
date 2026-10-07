from django.db import models


class Language(models.TextChoices):
    AZ = "az", "AZ"
    EN = "en", "EN"
    RU = "ru", "RU"


class ProductKind(models.TextChoices):
    CARD = "card", "Kart"
    LOAN = "loan", "Kredit"
    DEPOSIT = "deposit", "Əmanət"


class BranchKind(models.TextChoices):
    BRANCH = "branch", "Filial"
    ATM = "atm", "ATM"


class Product(models.Model):
    kind = models.CharField("Növ", max_length=10, choices=ProductKind.choices)
    slug = models.SlugField("Slug", unique=True)
    interest_rate = models.DecimalField(
        "İllik faiz",
        max_digits=5,
        decimal_places=2,
        help_text="İllik faiz. Məsələn 18.00",
    )
    currency = models.CharField("Valyuta", max_length=3, default="AZN")
    min_amount = models.DecimalField("Minimum məbləğ", max_digits=12, decimal_places=2, default=0)
    max_amount = models.DecimalField("Maksimum məbləğ", max_digits=12, decimal_places=2, default=0)
    min_months = models.PositiveIntegerField("Minimum ay", default=1)
    max_months = models.PositiveIntegerField("Maksimum ay", default=12)
    image = models.ImageField(
        "Şəkil",
        upload_to="cards/",
        blank=True,
        null=True,
        help_text="Kart səhifəsində sağdakı kart şəkli, kredit səhifəsində sağdakı banner. PNG və ya JPG.",
    )
    is_published = models.BooleanField("Dərc", default=True)
    sort_order = models.PositiveIntegerField("Sıra", default=0)

    class Meta:
        ordering = ["sort_order", "slug"]
        verbose_name = "Məhsul"
        verbose_name_plural = "Məhsullar"

    def __str__(self):
        title = self.translations.filter(language=Language.AZ).values_list("title", flat=True).first()
        return title or self.slug


class ProductTranslation(models.Model):
    product = models.ForeignKey(Product, related_name="translations", on_delete=models.CASCADE)
    language = models.CharField("Dil", max_length=2, choices=Language.choices)
    title = models.CharField("Böyük başlıq", max_length=160, help_text="Kartdakı qalın başlıq.")
    summary = models.CharField("Alt başlıq", max_length=280, blank=True, help_text="Başlığın altındakı boz sətir.")
    spec_1_label = models.CharField("1-ci ad", max_length=40, blank=True, default="", help_text="Məsələn: Müddət")
    spec_1_value = models.CharField("1-ci dəyər", max_length=80, blank=True, default="", help_text="Məsələn: 5 il")
    spec_2_label = models.CharField("2-ci ad", max_length=40, blank=True, default="")
    spec_2_value = models.CharField("2-ci dəyər", max_length=80, blank=True, default="")
    spec_3_label = models.CharField("3-cü ad", max_length=40, blank=True, default="")
    spec_3_value = models.CharField("3-cü dəyər", max_length=80, blank=True, default="")
    spec_4_label = models.CharField("4-cü ad", max_length=40, blank=True, default="", help_text="Kredit kartında dördüncü sütun. Kartda boş saxla.")
    spec_4_value = models.CharField("4-cü dəyər", max_length=80, blank=True, default="")
    order_label = models.CharField("Qara düymə", max_length=40, blank=True, default="", help_text="Əyri qara düymənin yazısı.")
    more_label = models.CharField("Oxlu link", max_length=40, blank=True, default="", help_text="Düymənin yanındakı link.")
    body = models.TextField("Detal mətni", blank=True)

    class Meta:
        constraints = [
            models.UniqueConstraint(fields=["product", "language"], name="uniq_product_language"),
        ]
        verbose_name = "Tərcümə"
        verbose_name_plural = "Tərcümələr"

    def __str__(self):
        return f"{self.product_id} {self.language}"


class CardsPage(models.Model):
    class Meta:
        verbose_name = "Kartlar səhifəsi"
        verbose_name_plural = "Kartlar səhifəsi"

    def __str__(self):
        return "Kartlar səhifəsi"


class CardsPageTranslation(models.Model):
    page = models.ForeignKey(CardsPage, related_name="translations", on_delete=models.CASCADE)
    language = models.CharField("Dil", max_length=2, choices=Language.choices)
    heading = models.CharField(
        "Böyük başlıq",
        max_length=80,
        blank=True,
        help_text="Səhifənin ortasındakı böyük yazı.",
    )
    lead = models.TextField(
        "Boz mətn",
        blank=True,
        help_text="Başlığın altında, ortada, daha kiçik və boz.",
    )

    class Meta:
        constraints = [
            models.UniqueConstraint(fields=["page", "language"], name="uniq_cards_page_language"),
        ]
        verbose_name = "Dil"
        verbose_name_plural = "Başlıq və giriş mətni"

    def __str__(self):
        return self.language


class LoansPage(models.Model):
    class Meta:
        verbose_name = "Kreditlər səhifəsi"
        verbose_name_plural = "Kreditlər səhifəsi"

    def __str__(self):
        return "Kreditlər səhifəsi"


class LoansPageTranslation(models.Model):
    page = models.ForeignKey(LoansPage, related_name="translations", on_delete=models.CASCADE)
    language = models.CharField("Dil", max_length=2, choices=Language.choices)
    heading = models.CharField(
        "Böyük başlıq",
        max_length=80,
        blank=True,
        help_text="Səhifənin ortasındakı böyük yazı.",
    )
    lead = models.TextField(
        "Boz mətn",
        blank=True,
        help_text="Başlığın altında, ortada, daha kiçik və boz.",
    )

    class Meta:
        constraints = [
            models.UniqueConstraint(fields=["page", "language"], name="uniq_loans_page_language"),
        ]
        verbose_name = "Dil"
        verbose_name_plural = "Başlıq və giriş mətni"

    def __str__(self):
        return self.language


class DepositsPage(models.Model):
    class Meta:
        verbose_name = "Əmanətlər səhifəsi"
        verbose_name_plural = "Əmanətlər səhifəsi"

    def __str__(self):
        return "Əmanətlər səhifəsi"


class DepositsPageTranslation(models.Model):
    page = models.ForeignKey(DepositsPage, related_name="translations", on_delete=models.CASCADE)
    language = models.CharField("Dil", max_length=2, choices=Language.choices)
    heading = models.CharField(
        "Böyük başlıq",
        max_length=80,
        blank=True,
        help_text="Səhifənin ortasındakı böyük yazı.",
    )
    lead = models.TextField(
        "Boz mətn",
        blank=True,
        help_text="Başlığın altında, ortada, daha kiçik və boz.",
    )

    class Meta:
        constraints = [
            models.UniqueConstraint(fields=["page", "language"], name="uniq_deposits_page_language"),
        ]
        verbose_name = "Dil"
        verbose_name_plural = "Başlıq və giriş mətni"

    def __str__(self):
        return self.language


class NewsPost(models.Model):
    slug = models.SlugField("Slug", unique=True)
    published_at = models.DateTimeField("Tarix")
    is_published = models.BooleanField("Dərc", default=True)

    class Meta:
        ordering = ["-published_at"]
        verbose_name = "Xəbər"
        verbose_name_plural = "Xəbərlər"

    def __str__(self):
        title = self.translations.filter(language=Language.AZ).values_list("title", flat=True).first()
        return title or self.slug


class NewsTranslation(models.Model):
    news = models.ForeignKey(NewsPost, related_name="translations", on_delete=models.CASCADE)
    language = models.CharField("Dil", max_length=2, choices=Language.choices)
    title = models.CharField("Başlıq", max_length=160)
    summary = models.CharField("Qısa mətn", max_length=280)
    body = models.TextField("Mətn")

    class Meta:
        constraints = [
            models.UniqueConstraint(fields=["news", "language"], name="uniq_news_language"),
        ]
        verbose_name = "Tərcümə"
        verbose_name_plural = "Tərcümələr"

    def __str__(self):
        return f"{self.news_id} {self.language}"


class Branch(models.Model):
    kind = models.CharField("Növ", max_length=10, choices=BranchKind.choices)
    map_url = models.URLField("Xəritə linki", blank=True)
    is_published = models.BooleanField("Dərc", default=True)
    sort_order = models.PositiveIntegerField("Sıra", default=0)

    class Meta:
        ordering = ["sort_order", "id"]
        verbose_name = "Filial"
        verbose_name_plural = "Filiallar"

    def __str__(self):
        name = self.translations.filter(language=Language.AZ).values_list("name", flat=True).first()
        return name or f"{self.kind} {self.pk}"


class BranchTranslation(models.Model):
    branch = models.ForeignKey(Branch, related_name="translations", on_delete=models.CASCADE)
    language = models.CharField("Dil", max_length=2, choices=Language.choices)
    name = models.CharField("Ad", max_length=160)
    address = models.CharField("Ünvan", max_length=240)
    hours = models.CharField("İş saatı", max_length=160)

    class Meta:
        constraints = [
            models.UniqueConstraint(fields=["branch", "language"], name="uniq_branch_language"),
        ]
        verbose_name = "Tərcümə"
        verbose_name_plural = "Tərcümələr"

    def __str__(self):
        return f"{self.branch_id} {self.language}"


class ExchangeRate(models.Model):
    currency = models.CharField("Valyuta", max_length=3, unique=True)
    buy = models.DecimalField("Alış", max_digits=12, decimal_places=4)
    sell = models.DecimalField("Satış", max_digits=12, decimal_places=4)
    updated_at = models.DateTimeField("Yenilənib", auto_now=True)

    class Meta:
        ordering = ["currency"]
        verbose_name = "Məzənnə"
        verbose_name_plural = "Məzənnə"

    def __str__(self):
        return self.currency


class Banner(models.Model):
    href = models.CharField(
        "Keçid",
        max_length=160,
        blank=True,
        help_text="Dilsiz yol. Məsələn /cards/study-debit",
    )
    is_published = models.BooleanField("Dərc", default=True)
    sort_order = models.PositiveIntegerField("Sıra", default=0)

    class Meta:
        ordering = ["sort_order", "id"]
        verbose_name = "Banner"
        verbose_name_plural = "Bannerlər"

    def __str__(self):
        title = self.translations.filter(language=Language.AZ).values_list("title", flat=True).first()
        return title or f"Banner {self.pk}"


class BannerTranslation(models.Model):
    banner = models.ForeignKey(Banner, related_name="translations", on_delete=models.CASCADE)
    language = models.CharField("Dil", max_length=2, choices=Language.choices)
    title = models.CharField("Başlıq", max_length=160)
    subtitle = models.CharField("Alt başlıq", max_length=280)

    class Meta:
        constraints = [
            models.UniqueConstraint(fields=["banner", "language"], name="uniq_banner_language"),
        ]
        verbose_name = "Tərcümə"
        verbose_name_plural = "Tərcümələr"

    def __str__(self):
        return f"{self.banner_id} {self.language}"


class CashbackPage(models.Model):
    class Meta:
        verbose_name = "Keşbek səhifəsi"
        verbose_name_plural = "Keşbek səhifəsi"

    def __str__(self):
        return "Keşbek səhifəsi"


class CashbackPageTranslation(models.Model):
    page = models.ForeignKey(CashbackPage, related_name="translations", on_delete=models.CASCADE)
    language = models.CharField("Dil", max_length=2, choices=Language.choices)
    heading = models.CharField("Böyük başlıq", max_length=120, blank=True)
    button_label = models.CharField("Sarı düymə", max_length=40, blank=True)

    class Meta:
        constraints = [
            models.UniqueConstraint(fields=["page", "language"], name="uniq_cashback_page_language"),
        ]
        verbose_name = "Dil"
        verbose_name_plural = "Başlıq və düymə"

    def __str__(self):
        return self.language


class CashbackPack(models.Model):
    slug = models.SlugField("Slug", unique=True)
    sort_order = models.PositiveIntegerField("Sıra", default=0)
    is_published = models.BooleanField("Dərc", default=True)

    class Meta:
        ordering = ["sort_order", "id"]
        verbose_name = "Keşbek paketi"
        verbose_name_plural = "Keşbek paketləri"

    def __str__(self):
        label = self.translations.filter(language=Language.AZ).values_list("label", flat=True).first()
        return label or self.slug


class CashbackPackTranslation(models.Model):
    pack = models.ForeignKey(CashbackPack, related_name="translations", on_delete=models.CASCADE)
    language = models.CharField("Dil", max_length=2, choices=Language.choices)
    label = models.CharField("Paket adı", max_length=40, blank=True)
    note = models.CharField("Qeyd", max_length=280, blank=True)
    item_1_title = models.CharField("1-ci kateqoriya", max_length=80, blank=True)
    item_1_text = models.CharField("1-ci mətn", max_length=280, blank=True)
    item_2_title = models.CharField("2-ci kateqoriya", max_length=80, blank=True)
    item_2_text = models.CharField("2-ci mətn", max_length=280, blank=True)
    item_3_title = models.CharField("3-cü kateqoriya", max_length=80, blank=True)
    item_3_text = models.CharField("3-cü mətn", max_length=280, blank=True)

    class Meta:
        constraints = [
            models.UniqueConstraint(fields=["pack", "language"], name="uniq_cashback_pack_language"),
        ]
        verbose_name = "Dil"
        verbose_name_plural = "Paket yazıları"

    def __str__(self):
        return f"{self.pack_id} {self.language}"
