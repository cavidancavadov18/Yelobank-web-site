from django import forms
from django.contrib import admin
from django.forms.models import BaseInlineFormSet
from unfold.admin import ModelAdmin, StackedInline, TabularInline

from content.models import (
    Banner,
    BannerTranslation,
    Branch,
    BranchTranslation,
    CardsPage,
    CardsPageTranslation,
    CashbackPack,
    CashbackPackTranslation,
    CashbackPage,
    CashbackPageTranslation,
    ExchangeRate,
    DepositsPage,
    DepositsPageTranslation,
    LoansPage,
    LoansPageTranslation,
    NewsPost,
    NewsTranslation,
    Product,
    ProductTranslation,
)


class TranslationFormSet(BaseInlineFormSet):
    def __init__(self, *args, **kwargs):
        kwargs.setdefault(
            "initial",
            [{"language": "az"}, {"language": "en"}, {"language": "ru"}],
        )
        super().__init__(*args, **kwargs)


class TranslationInline(TabularInline):
    extra = 3
    formset = TranslationFormSet
    translation_accessor = "translations"

    def get_extra(self, request, obj=None, **kwargs):
        if obj and obj.pk and getattr(obj, self.translation_accessor).exists():
            return 0
        return 3

    def formfield_for_dbfield(self, db_field, request, **kwargs):
        if db_field.name in {"body", "summary", "subtitle", "address"}:
            kwargs["widget"] = forms.Textarea(attrs={"rows": 2})
        return super().formfield_for_dbfield(db_field, request, **kwargs)


class ProductTranslationInline(StackedInline):
    model = ProductTranslation
    formset = TranslationFormSet
    extra = 3
    translation_accessor = "translations"
    verbose_name = "Dil bloku"
    verbose_name_plural = "Səhifədəki yazılar — hər dil üçün bir blok"
    fieldsets = (
        (
            "Başlıqlar",
            {
                "fields": ("language", "title", "summary"),
                "description": "Böyük başlıq solda qalındır. Alt başlıq onun altında, daha kiçik və bozdur.",
            },
        ),
        (
            "Göstəricilər",
            {
                "fields": (
                    "spec_1_label",
                    "spec_1_value",
                    "spec_2_label",
                    "spec_2_value",
                    "spec_3_label",
                    "spec_3_value",
                    "spec_4_label",
                    "spec_4_value",
                ),
                "description": "Soldan sağa. Kartda 3 sütun, kreditdə 4 sütun. Ad kiçik və boz, dəyər qalın. Boş sütun görünmür.",
            },
        ),
        (
            "Düymələr",
            {
                "fields": ("order_label", "more_label"),
                "description": "Qara düymə əyri görünür. Oxlu link onun sağında durur.",
            },
        ),
        (
            "Detal səhifə",
            {
                "fields": ("body",),
                "description": "Kartın adına keçəndə açılan səhifənin mətni.",
            },
        ),
    )

    def get_extra(self, request, obj=None, **kwargs):
        if obj and obj.pk and obj.translations.exists():
            return 0
        return 3

    def formfield_for_dbfield(self, db_field, request, **kwargs):
        if db_field.name in {"summary", "body"}:
            kwargs["widget"] = forms.Textarea(attrs={"rows": 3})
        return super().formfield_for_dbfield(db_field, request, **kwargs)


class NewsTranslationInline(TranslationInline):
    model = NewsTranslation
    fields = ("language", "title", "summary", "body")


class BranchTranslationInline(TranslationInline):
    model = BranchTranslation
    fields = ("language", "name", "address", "hours")


class BannerTranslationInline(TranslationInline):
    model = BannerTranslation
    fields = ("language", "title", "subtitle")


def az_title(obj):
    translation = obj.translations.filter(language="az").first()
    if translation is None:
        return "—"
    return getattr(translation, "title", None) or getattr(translation, "name", "—")


@admin.register(Product)
class ProductAdmin(ModelAdmin):
    list_display = ("title_az", "kind", "interest_rate", "currency", "is_published", "sort_order")
    list_filter = ("kind", "is_published")
    search_fields = ("slug", "translations__title")
    list_editable = ("is_published", "sort_order")
    inlines = [ProductTranslationInline]
    fieldsets = (
        (
            "Əsas",
            {
                "fields": ("slug", "kind", "is_published", "sort_order"),
                "description": "Slug ünvanın bir hissəsidir. Kart siyahısında sıra kiçik rəqəmdən başlayır.",
            },
        ),
        (
            "Şəkil",
            {
                "fields": ("image",),
                "description": "Kart səhifəsində sağdakı kart şəkli. Kredit səhifəsində blokun sağındakı banner.",
            },
        ),
        (
            "Kredit kalkulyatoru",
            {
                "fields": ("interest_rate", "currency", "min_amount", "max_amount", "min_months", "max_months"),
                "description": "Yalnız kredit səhifəsindəki kalkulyator üçündür.",
                "classes": ("collapse",),
            },
        ),
    )

    @admin.display(description="Başlıq")
    def title_az(self, obj):
        return az_title(obj)


class CardsPageTranslationInline(StackedInline):
    model = CardsPageTranslation
    formset = TranslationFormSet
    extra = 3
    max_num = 3
    verbose_name_plural = "AZ, EN və RU — başlıq ortada böyük, mətn onun altında kiçik və boz"
    fields = ("language", "heading", "lead")

    def get_extra(self, request, obj=None, **kwargs):
        if obj and obj.pk and obj.translations.exists():
            return 0
        return 3

    def formfield_for_dbfield(self, db_field, request, **kwargs):
        if db_field.name == "lead":
            kwargs["widget"] = forms.Textarea(attrs={"rows": 4})
        return super().formfield_for_dbfield(db_field, request, **kwargs)


@admin.register(CardsPage)
class CardsPageAdmin(ModelAdmin):
    inlines = [CardsPageTranslationInline]
    readonly_fields = ("hint",)
    fields = ("hint",)

    @admin.display(description="Harada görünür")
    def hint(self, obj):
        return "Böyük başlıq səhifənin ortasındadır. Boz mətn onun altındadır və daha kiçikdir. Kartın başlığı, 3 göstərici, düymə və şəkil Məhsullar bölməsindədir."

    def has_add_permission(self, request):
        return not CardsPage.objects.exists()

    def has_delete_permission(self, request, obj=None):
        return False


class LoansPageTranslationInline(StackedInline):
    model = LoansPageTranslation
    formset = TranslationFormSet
    extra = 3
    max_num = 3
    verbose_name_plural = "AZ, EN və RU — başlıq ortada böyük, mətn onun altında kiçik və boz"
    fields = ("language", "heading", "lead")

    def get_extra(self, request, obj=None, **kwargs):
        if obj and obj.pk and obj.translations.exists():
            return 0
        return 3

    def formfield_for_dbfield(self, db_field, request, **kwargs):
        if db_field.name == "lead":
            kwargs["widget"] = forms.Textarea(attrs={"rows": 4})
        return super().formfield_for_dbfield(db_field, request, **kwargs)


@admin.register(LoansPage)
class LoansPageAdmin(ModelAdmin):
    inlines = [LoansPageTranslationInline]
    readonly_fields = ("hint",)
    fields = ("hint",)

    @admin.display(description="Harada görünür")
    def hint(self, obj):
        return "Böyük başlıq səhifənin ortasındadır. Boz mətn onun altındadır. Hər kreditin başlığı, 4 göstəricisi, düyməsi və şəkli Məhsullardadır. Növü Kredit olsun."

    def has_add_permission(self, request):
        return not LoansPage.objects.exists()

    def has_delete_permission(self, request, obj=None):
        return False


class DepositsPageTranslationInline(StackedInline):
    model = DepositsPageTranslation
    formset = TranslationFormSet
    extra = 3
    max_num = 3
    verbose_name_plural = "AZ, EN və RU — başlıq ortada böyük, mətn onun altında kiçik və boz"
    fields = ("language", "heading", "lead")

    def get_extra(self, request, obj=None, **kwargs):
        if obj and obj.pk and obj.translations.exists():
            return 0
        return 3

    def formfield_for_dbfield(self, db_field, request, **kwargs):
        if db_field.name == "lead":
            kwargs["widget"] = forms.Textarea(attrs={"rows": 4})
        return super().formfield_for_dbfield(db_field, request, **kwargs)


@admin.register(DepositsPage)
class DepositsPageAdmin(ModelAdmin):
    inlines = [DepositsPageTranslationInline]
    readonly_fields = ("hint",)
    fields = ("hint",)

    @admin.display(description="Harada görünür")
    def hint(self, obj):
        return "Böyük başlıq səhifənin ortasındadır. Boz mətn onun altındadır. Hər əmanətin başlığı, göstəriciləri, düyməsi və şəkli Məhsullardadır. Növü Əmanət olsun."

    def has_add_permission(self, request):
        return not DepositsPage.objects.exists()

    def has_delete_permission(self, request, obj=None):
        return False


class CashbackPageTranslationInline(StackedInline):
    model = CashbackPageTranslation
    formset = TranslationFormSet
    extra = 3
    max_num = 3
    verbose_name_plural = "AZ, EN və RU — böyük başlıq və sarı düymə"
    fields = ("language", "heading", "button_label")

    def get_extra(self, request, obj=None, **kwargs):
        if obj and obj.pk and obj.translations.exists():
            return 0
        return 3


@admin.register(CashbackPage)
class CashbackPageAdmin(ModelAdmin):
    inlines = [CashbackPageTranslationInline]
    readonly_fields = ("hint",)
    fields = ("hint",)

    @admin.display(description="Harada görünür")
    def hint(self, obj):
        return "Böyük başlıq keşbek səhifəsinin solundadır. Sarı düymə onun altındadır. Paketlər ayrıca Keşbek paketləri bölməsindədir."

    def has_add_permission(self, request):
        return not CashbackPage.objects.exists()

    def has_delete_permission(self, request, obj=None):
        return False


class CashbackPackTranslationInline(StackedInline):
    model = CashbackPackTranslation
    formset = TranslationFormSet
    extra = 3
    verbose_name = "Dil bloku"
    verbose_name_plural = "Paket yazıları — hər dil üçün bir blok"
    fieldsets = (
        ("Paket", {"fields": ("language", "label", "note")}),
        (
            "Kateqoriyalar",
            {
                "fields": (
                    "item_1_title",
                    "item_1_text",
                    "item_2_title",
                    "item_2_text",
                    "item_3_title",
                    "item_3_text",
                ),
                "description": "Hər cüt bir kart olur: qalın ad və altındakı mətn. Boş cüt görünmür.",
            },
        ),
    )

    def get_extra(self, request, obj=None, **kwargs):
        if obj and obj.pk and obj.translations.exists():
            return 0
        return 3

    def formfield_for_dbfield(self, db_field, request, **kwargs):
        if db_field.name in {"note", "item_1_text", "item_2_text", "item_3_text"}:
            kwargs["widget"] = forms.Textarea(attrs={"rows": 2})
        return super().formfield_for_dbfield(db_field, request, **kwargs)


@admin.register(CashbackPack)
class CashbackPackAdmin(ModelAdmin):
    list_display = ("label_az", "slug", "is_published", "sort_order")
    list_editable = ("is_published", "sort_order")
    search_fields = ("slug", "translations__label")
    inlines = [CashbackPackTranslationInline]
    fieldsets = (
        (
            "Əsas",
            {
                "fields": ("slug", "is_published", "sort_order"),
                "description": "Sıra kiçik rəqəmdən başlayır. Dərc söndürüləndə paket saytda görünmür.",
            },
        ),
    )

    @admin.display(description="Paket")
    def label_az(self, obj):
        translation = obj.translations.filter(language="az").first()
        return translation.label if translation else obj.slug


@admin.register(NewsPost)
class NewsPostAdmin(ModelAdmin):
    list_display = ("title_az", "published_at", "is_published")
    list_filter = ("is_published",)
    search_fields = ("slug", "translations__title")
    inlines = [NewsTranslationInline]
    fieldsets = (("Əsas", {"fields": ("slug", "published_at", "is_published")}),)

    @admin.display(description="Başlıq")
    def title_az(self, obj):
        return az_title(obj)


@admin.register(Branch)
class BranchAdmin(ModelAdmin):
    list_display = ("name_az", "kind", "is_published", "sort_order")
    list_filter = ("kind", "is_published")
    search_fields = ("translations__name", "translations__address")
    inlines = [BranchTranslationInline]
    fieldsets = (("Əsas", {"fields": ("kind", "map_url", "is_published", "sort_order")}),)

    @admin.display(description="Ad")
    def name_az(self, obj):
        translation = obj.translations.filter(language="az").first()
        return translation.name if translation else "—"


@admin.register(ExchangeRate)
class ExchangeRateAdmin(ModelAdmin):
    list_display = ("currency", "buy", "sell", "updated_at")
    list_editable = ("buy", "sell")
    ordering = ("currency",)


@admin.register(Banner)
class BannerAdmin(ModelAdmin):
    list_display = ("title_az", "href", "is_published", "sort_order")
    list_editable = ("is_published", "sort_order")
    inlines = [BannerTranslationInline]
    fieldsets = (("Əsas", {"fields": ("href", "is_published", "sort_order")}),)

    @admin.display(description="Başlıq")
    def title_az(self, obj):
        return az_title(obj)
