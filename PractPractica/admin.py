from django.contrib import admin
from .models import *

admin.site.register(models.Publisher)

@admin.register(Publisher)
class PublisherAdmin(admin.ModelAdmin):
    list_display = ('publisher_name', 'publisher_country', 'is_deleted')


@admin.register(DonationCurrency)
class DonationCurrencyAdmin(admin.ModelAdmin):
    list_display = ('currency_type', 'currency_price', 'is_deleted')


@admin.register(Customer)
class CustomerAdmin(admin.ModelAdmin):
    list_display = ('customer_name', 'customer_email', 'password', 'is_deleted')


@admin.register(Genre)
class GenreAdmin(admin.ModelAdmin):
    list_display = ('genre_description', 'genre_name', 'is_deleted')


@admin.register(Game)
class GameAdmin(admin.ModelAdmin):
    list_display = ('game_title', 'publisher', 'release_date', 'price', 'genre', 'donation_currency', 'is_deleted')


@admin.register(GamePurchase)
class GamePurchaseAdmin(admin.ModelAdmin):
    list_display = ('game', 'card_details', 'address_details', 'customer', 'is_deleted')


@admin.register(VideoGameRental)
class VideoGameRentalAdmin(admin.ModelAdmin):
    list_display = ('game', 'customer', 'time_period', 'price_per_time', 'is_deleted')


@admin.register(Bid)
class BidAdmin(admin.ModelAdmin):
    list_display = ('bid_amount', 'bid_date', 'is_deleted')


@admin.register(Auction)
class AuctionAdmin(admin.ModelAdmin):
    list_display = ('bid', 'customer', 'start_date', 'end_date', 'starting_price', 'is_deleted')


@admin.register(SoldGameCopy)
class SoldGameCopyAdmin(admin.ModelAdmin):
    list_display = ('copies_sold', 'games_sold_for_year', 'game_purchase', 'is_deleted')


@admin.register(AuctionWinner)
class AuctionWinnerAdmin(admin.ModelAdmin):
    list_display = ('auction', 'winning_bid_amount', 'winning_bid_date', 'is_deleted')


@admin.register(Sale)
class SaleAdmin(admin.ModelAdmin):
    list_display = (
    'video_game_rental', 'sold_game_copy', 'auction_winner', 'customer', 'sale_date', 'price', 'total_sale_amount',
    'is_deleted')


@admin.register(Payment)
class PaymentAdmin(admin.ModelAdmin):
    list_display = ('customer', 'payment_amount', 'payment_date', 'is_deleted')
