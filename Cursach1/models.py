from django.db import models
from django.contrib.auth.models import User


class User(models.Model):
    username = models.CharField(max_length=100, unique=True)
    password = models.CharField(max_length=255)
    
    class Meta:
        app_label = 'PractPractica'
        db_table = 'Users'

class UserProfile(models.Model):
    username = models.CharField(max_length=100, unique=True)
    password = models.CharField(max_length=100)
    salt = models.CharField(max_length=100)
    is_deleted = models.BooleanField(default=False)
    class Meta:
        app_label = 'PractPractica'
        db_table = 'UserProfile'

class Publisher(models.Model):
    publisher_name = models.CharField(max_length=255)
    publisher_country = models.CharField(max_length=255)
    is_deleted = models.BooleanField(default=False)
    class Meta:
        app_label = 'PractPractica'
        db_table = 'Publishers'

class DonationCurrency(models.Model):
    currency_type = models.CharField(max_length=255)
    currency_price = models.DecimalField(max_digits=10, decimal_places=2)
    is_deleted = models.BooleanField(default=False)
    class Meta:
        app_label = 'PractPractica'
        db_table = 'Donation_Currency'

class Customer(models.Model):
    customer_name = models.CharField(max_length=255)
    customer_email = models.EmailField()
    password = models.CharField(max_length=255)
    is_deleted = models.BooleanField(default=False)
    class Meta:
        app_label = 'PractPractica'
        db_table = 'Customers'

class Genre(models.Model):
    genre_description = models.CharField(max_length=255)
    genre_name = models.CharField(max_length=255)
    is_deleted = models.BooleanField(default=False)
    class Meta:
        app_label = 'PractPractica'
        db_table = 'Genres'

class Game(models.Model):
    game_title = models.CharField(max_length=255)
    publisher = models.ForeignKey(Publisher, on_delete=models.CASCADE)
    release_date = models.DateField()
    price = models.DecimalField(max_digits=10, decimal_places=2)
    genre = models.ForeignKey(Genre, on_delete=models.CASCADE)
    donation_currency = models.ForeignKey(DonationCurrency, on_delete=models.CASCADE)
    is_deleted = models.BooleanField(default=False)
    class Meta:
        app_label = 'PractPractica'
        db_table = 'Games'

class GamePurchase(models.Model):
    game = models.ForeignKey(Game, on_delete=models.CASCADE)
    card_details = models.CharField(max_length=255)
    address_details = models.CharField(max_length=255)
    customer = models.ForeignKey(Customer, on_delete=models.CASCADE)
    is_deleted = models.BooleanField(default=False)
    class Meta:
        app_label = 'PractPractica'
        db_table = 'Game_Purchase'

class VideoGameRental(models.Model):
    game = models.ForeignKey(Game, on_delete=models.CASCADE)
    customer = models.ForeignKey(Customer, on_delete=models.CASCADE)
    time_period = models.IntegerField()
    price_per_time = models.DecimalField(max_digits=10, decimal_places=2)
    is_deleted = models.BooleanField(default=False)
    class Meta:
        app_label = 'PractPractica'
        db_table = 'Video_Game_Rentals'

class Bid(models.Model):
    bid_amount = models.DecimalField(max_digits=10, decimal_places=2)
    bid_date = models.DateTimeField(auto_now_add=True)
    is_deleted = models.BooleanField(default=False)
    class Meta:
        app_label = 'PractPractica'
        db_table = 'Bids'

class Auction(models.Model):
    bid = models.OneToOneField(Bid, on_delete=models.CASCADE)
    customer = models.ForeignKey(Customer, on_delete=models.CASCADE)
    start_date = models.DateField()
    end_date = models.DateField()
    starting_price = models.DecimalField(max_digits=10, decimal_places=2)
    is_deleted = models.BooleanField(default=False)
    class Meta:
        app_label = 'PractPractica'
        db_table = 'Auctions'

class SoldGameCopy(models.Model):
    copies_sold = models.IntegerField()
    games_sold_for_year = models.DateField()
    game_purchase = models.OneToOneField(GamePurchase, on_delete=models.CASCADE)
    is_deleted = models.BooleanField(default=False)
    class Meta:
        app_label = 'PractPractica'
        db_table = 'Sold_Game_Copies'

class AuctionWinner(models.Model):
    auction = models.OneToOneField(Auction, on_delete=models.CASCADE)
    winning_bid_amount = models.DecimalField(max_digits=10, decimal_places=2)
    winning_bid_date = models.DateField()
    is_deleted = models.BooleanField(default=False)
    class Meta:
        app_label = 'PractPractica'
        db_table = 'Auction_Winners'

class Sale(models.Model):
    video_game_rental = models.OneToOneField(VideoGameRental, on_delete=models.CASCADE)
    sold_game_copy = models.OneToOneField(SoldGameCopy, on_delete=models.CASCADE)
    auction_winner = models.OneToOneField(AuctionWinner, on_delete=models.CASCADE)
    customer = models.ForeignKey(Customer, on_delete=models.CASCADE)
    sale_date = models.DateField()
    price = models.DecimalField(max_digits=10, decimal_places=2)
    total_sale_amount = models.DecimalField(max_digits=10, decimal_places=2)
    is_deleted = models.BooleanField(default=False)
    class Meta:
        app_label = 'PractPractica'
        db_table = 'Sales'

class Payment(models.Model):
    customer = models.ForeignKey(Customer, on_delete=models.CASCADE)
    payment_amount = models.DecimalField(max_digits=10, decimal_places=2)
    payment_date = models.DateField()
    is_deleted = models.BooleanField(default=False)
    class Meta:
        app_label = 'PractPractica'
        db_table = 'Payments'

