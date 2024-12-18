"""
URL configuration for PractPractica project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from .views import (
    PublisherListCreate, PublisherRetrieveUpdateDestroy,
    DonationCurrencyListCreate, DonationCurrencyRetrieveUpdateDestroy,
    CustomerListCreate, CustomerRetrieveUpdateDestroy,
    GenreListCreate, GenreRetrieveUpdateDestroy,
    GameListCreate, GameRetrieveUpdateDestroy,
    GamePurchaseListCreate, GamePurchaseRetrieveUpdateDestroy,
    VideoGameRentalListCreate, VideoGameRentalRetrieveUpdateDestroy,
    BidListCreate, BidRetrieveUpdateDestroy,
    AuctionListCreate, AuctionRetrieveUpdateDestroy,
    SoldGameCopyListCreate, SoldGameCopyRetrieveUpdateDestroy,
    AuctionWinnerListCreate, AuctionWinnerRetrieveUpdateDestroy,
    SaleListCreate, SaleRetrieveUpdateDestroy,
    PaymentListCreate, PaymentRetrieveUpdateDestroy,
    register, user_login, login_view, home
)

urlpatterns = [

    path('admin/', admin.site.urls),
    path('home/', home, name='home'),
    path('login_view/', login_view, name='login'),


    # Publisher URLs
    path('publishers/', PublisherListCreate.as_view()),
    path('publishers/<int:pk>/', PublisherRetrieveUpdateDestroy.as_view()),

    # DonationCurrency URLs
    path('donation-currencies/', DonationCurrencyListCreate.as_view()),
    path('donation-currencies/<int:pk>/', DonationCurrencyRetrieveUpdateDestroy.as_view()),

    # Customer URLs
    path('customers/', CustomerListCreate.as_view()),
    path('customers/<int:pk>/', CustomerRetrieveUpdateDestroy.as_view()),

    # Genre URLs
    path('genres/', GenreListCreate.as_view()),
    path('genres/<int:pk>/', GenreRetrieveUpdateDestroy.as_view()),

    # Game URLs
    path('games/', GameListCreate.as_view()),
    path('games/<int:pk>/', GameRetrieveUpdateDestroy.as_view()),

    # GamePurchase URLs
    path('game-purchases/', GamePurchaseListCreate.as_view()),
    path('game-purchases/<int:pk>/', GamePurchaseRetrieveUpdateDestroy.as_view()),

    # VideoGameRental URLs
    path('video-game-rentals/', VideoGameRentalListCreate.as_view()),
    path('video-game-rentals/<int:pk>/', VideoGameRentalRetrieveUpdateDestroy.as_view()),

    # Bid URLs
    path('bids/', BidListCreate.as_view()),
    path('bids/<int:pk>/', BidRetrieveUpdateDestroy.as_view()),

    # Auction URLs
    path('auctions/', AuctionListCreate.as_view()),
    path('auctions/<int:pk>/', AuctionRetrieveUpdateDestroy.as_view()),

    # SoldGameCopy URLs
    path('sold-game-copies/', SoldGameCopyListCreate.as_view()),
    path('sold-game-copies/<int:pk>/', SoldGameCopyRetrieveUpdateDestroy.as_view()),

    # AuctionWinner URLs
    path('auction-winners/', AuctionWinnerListCreate.as_view()),
    path('auction-winners/<int:pk>/', AuctionWinnerRetrieveUpdateDestroy.as_view()),

    # Sale URLs
    path('sales/', SaleListCreate.as_view()),
    path('sales/<int:pk>/', SaleRetrieveUpdateDestroy.as_view()),

    # Payment URLs
    path('payments/', PaymentListCreate.as_view()),
    path('payments/<int:pk>/', PaymentRetrieveUpdateDestroy.as_view()),

# URL для авторизации
    path('login/', user_login, name='login'),          # Путь к функции аутентификации

    # URL для регистрации
    path('register/', register, name='register'),
]
