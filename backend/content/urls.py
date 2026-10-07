from django.urls import path

from content.views import (
    BranchListView,
    CardsPageView,
    CashbackPageView,
    DepositsPageView,
    LoansPageView,
    HomeView,
    NewsDetailView,
    NewsListView,
    ProductDetailView,
    ProductListView,
)

urlpatterns = [
    path("cards-page/", CardsPageView.as_view()),
    path("loans-page/", LoansPageView.as_view()),
    path("deposits-page/", DepositsPageView.as_view()),
    path("cashback/", CashbackPageView.as_view()),
    path("home/", HomeView.as_view()),
    path("products/", ProductListView.as_view()),
    path("products/<slug:slug>/", ProductDetailView.as_view()),
    path("news/", NewsListView.as_view()),
    path("news/<slug:slug>/", NewsDetailView.as_view()),
    path("branches/", BranchListView.as_view()),
]
