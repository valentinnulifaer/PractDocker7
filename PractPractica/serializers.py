from rest_framework import serializers
from .models import Publisher, DonationCurrency, Customer, Genre, Game, GamePurchase, VideoGameRental, Bid, Auction, SoldGameCopy, AuctionWinner, Sale, Payment

class PublisherSerializer(serializers.ModelSerializer):
    class Meta:
        model = Publisher
        fields = '__all__'

class DonationCurrencySerializer(serializers.ModelSerializer):
    class Meta:
        model = DonationCurrency
        fields = '__all__'

class CustomerSerializer(serializers.ModelSerializer):
    class Meta:
        model = Customer
        fields = '__all__'

class GenreSerializer(serializers.ModelSerializer):
    class Meta:
        model = Genre
        fields = '__all__'

class GameSerializer(serializers.ModelSerializer):
    class Meta:
        model = Game
        fields = '__all__'

class GamePurchaseSerializer(serializers.ModelSerializer):
    class Meta:
        model = GamePurchase
        fields = '__all__'

class VideoGameRentalSerializer(serializers.ModelSerializer):
    class Meta:
        model = VideoGameRental
        fields = '__all__'

class BidSerializer(serializers.ModelSerializer):
    class Meta:
        model = Bid
        fields = '__all__'

class AuctionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Auction
        fields = '__all__'

class SoldGameCopySerializer(serializers.ModelSerializer):
    class Meta:
        model = SoldGameCopy
        fields = '__all__'

class AuctionWinnerSerializer(serializers.ModelSerializer):
    class Meta:
        model = AuctionWinner
        fields = '__all__'

class SaleSerializer(serializers.ModelSerializer):
    class Meta:
        model = Sale
        fields = '__all__'

class PaymentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Payment
        fields = '__all__'