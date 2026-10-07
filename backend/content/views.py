from django.shortcuts import get_object_or_404
from rest_framework.response import Response
from rest_framework.views import APIView

from content.models import (
    Banner,
    Branch,
    CardsPage,
    CashbackPack,
    CashbackPage,
    DepositsPage,
    ExchangeRate,
    LoansPage,
    NewsPost,
    Product,
)
from content.serializers import (
    banner_payload,
    branch_payload,
    cards_page_payload,
    cashback_payload,
    clean_lang,
    news_payload,
    product_payload,
    rate_payload,
)


def published_products(kind=None):
    queryset = Product.objects.filter(is_published=True).prefetch_related("translations")
    if kind in {"card", "loan", "deposit"}:
        queryset = queryset.filter(kind=kind)
    return queryset


class HomeView(APIView):
    def get(self, request):
        lang = clean_lang(request.query_params.get("lang"))
        banners = Banner.objects.filter(is_published=True).prefetch_related("translations")
        rates = ExchangeRate.objects.all()
        return Response(
            {
                "banners": [banner_payload(item, lang) for item in banners],
                "cards": [product_payload(item, lang) for item in published_products("card")],
                "loans": [product_payload(item, lang) for item in published_products("loan")],
                "deposits": [product_payload(item, lang) for item in published_products("deposit")],
                "rates": [rate_payload(item) for item in rates],
            }
        )


class CardsPageView(APIView):
    def get(self, request):
        lang = clean_lang(request.query_params.get("lang"))
        page = CardsPage.objects.prefetch_related("translations").first()
        return Response(cards_page_payload(page, lang))


class DepositsPageView(APIView):
    def get(self, request):
        lang = clean_lang(request.query_params.get("lang"))
        page = DepositsPage.objects.prefetch_related("translations").first()
        return Response(cards_page_payload(page, lang))


class CashbackPageView(APIView):
    def get(self, request):
        lang = clean_lang(request.query_params.get("lang"))
        page = CashbackPage.objects.prefetch_related("translations").first()
        packs = CashbackPack.objects.filter(is_published=True).prefetch_related("translations")
        return Response(cashback_payload(page, packs, lang))


class LoansPageView(APIView):
    def get(self, request):
        lang = clean_lang(request.query_params.get("lang"))
        page = LoansPage.objects.prefetch_related("translations").first()
        return Response(cards_page_payload(page, lang))


class ProductListView(APIView):
    def get(self, request):
        lang = clean_lang(request.query_params.get("lang"))
        kind = request.query_params.get("type")
        return Response([product_payload(item, lang) for item in published_products(kind)])


class ProductDetailView(APIView):
    def get(self, request, slug):
        lang = clean_lang(request.query_params.get("lang"))
        product = get_object_or_404(
            Product.objects.filter(is_published=True).prefetch_related("translations"),
            slug=slug,
        )
        return Response(product_payload(product, lang, detail=True))


class NewsListView(APIView):
    def get(self, request):
        lang = clean_lang(request.query_params.get("lang"))
        posts = NewsPost.objects.filter(is_published=True).prefetch_related("translations")
        return Response([news_payload(item, lang) for item in posts])


class NewsDetailView(APIView):
    def get(self, request, slug):
        lang = clean_lang(request.query_params.get("lang"))
        post = get_object_or_404(
            NewsPost.objects.filter(is_published=True).prefetch_related("translations"),
            slug=slug,
        )
        return Response(news_payload(post, lang, detail=True))


class BranchListView(APIView):
    def get(self, request):
        lang = clean_lang(request.query_params.get("lang"))
        branches = Branch.objects.filter(is_published=True).prefetch_related("translations")
        return Response([branch_payload(item, lang) for item in branches])
