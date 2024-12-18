from rest_framework import generics
from .models import Publisher, DonationCurrency, Customer, Genre, Game, GamePurchase, VideoGameRental, Bid, Auction, SoldGameCopy, AuctionWinner, Sale, Payment, User
from .serializers import PublisherSerializer, DonationCurrencySerializer, CustomerSerializer, GenreSerializer, GameSerializer, GamePurchaseSerializer, VideoGameRentalSerializer, BidSerializer, AuctionSerializer, SoldGameCopySerializer, AuctionWinnerSerializer, SaleSerializer, PaymentSerializer
from rest_framework.pagination import PageNumberPagination
from django.shortcuts import render, redirect
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from .models import UserProfile
import hashlib
import secrets

def login_view(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        try:
            user = User.objects.get(username=username, password=password)
            request.session['user_id'] = user.id
            return redirect('home')  # Перенаправление на домашнюю страницу
        except User.DoesNotExist:
            error_message = "Invalid username or password"
            return render(request, 'templates/login.html', {'error_message': error_message})
    else:
        return render(request, 'templates/login.html')

def home(request):
    user_id = request.session.get('user_id')
    if user_id:
        user = User.objects.get(id=user_id)
        return render(request, 'templates/home.html', {'user': user})
    else:
        return redirect('login')

# Генерация соли
def generate_salt():
    return secrets.token_hex(16)

# Хэширование пароля с использованием соли
def hash_password(password, salt):
    return hashlib.sha256((password + salt).encode('utf-8')).hexdigest()

@api_view(['GET', 'POST'])
def publisher_list(request):
    if request.method == 'GET':
        publishers = Publisher.objects.filter(is_deleted=False)
        serializer = PublisherSerializer(publishers, many=True)
        return Response(serializer.data)

    elif request.method == 'POST':
        serializer = PublisherSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

@api_view(['GET', 'PUT', 'PATCH'])
def publisher_detail(request, pk):
    try:
        publisher = Publisher.objects.get(pk=pk)
    except Publisher.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)

    if request.method == 'GET':
        serializer = PublisherSerializer(publisher)
        return Response(serializer.data)

    elif request.method in ['PUT', 'PATCH']:
        publisher.is_deleted = not publisher.is_deleted  # Изменяем состояние логического удаления
        publisher.save()
        serializer = PublisherSerializer(publisher)
        return Response(serializer.data)



@api_view(['POST'])
def register(request):
    if request.method == 'POST':
        username = request.data.get('username')
        password = request.data.get('password')

        # Проверяем, существует ли пользователь с таким именем
        if UserProfile.objects.filter(username=username).exists():
            return Response({'error': 'Username already exists'}, status=status.HTTP_400_BAD_REQUEST)

        # Генерируем соль
        salt = generate_salt()
        # Хэшируем пароль с использованием соли
        hashed_password = hash_password(password, salt)

        # Создаем нового пользователя
        user = UserProfile.objects.create(username=username, password=hashed_password, salt=salt)

        # Возвращаем сообщение об успешной регистрации
        return Response({'message': 'Registration successful'}, status=status.HTTP_201_CREATED)

@api_view(['POST'])
def user_login(request):
    if request.method == 'POST':
        username = request.data.get('username')
        password = request.data.get('password')

        try:
            # Получаем данные пользователя по его имени
            user = UserProfile.objects.get(username=username)
        except UserProfile.DoesNotExist:
            user = None

        if user is not None:
            # Хэшируем введенный пароль с использованием соли
            hashed_password = hash_password(password, user.salt)
            # Проверяем совпадение хэша пароля
            if hashed_password == user.password:
                return Response({'message': 'Login successful'})

        return Response({'error': 'Invalid username or password'}, status=status.HTTP_400_BAD_REQUEST)

class CustomPagination(PageNumberPagination):
    page_size = 10
    page_size_query_param = 'page_size'
    max_page_size = 100

class PublisherListCreate(generics.ListCreateAPIView):
    queryset = Publisher.objects.all()
    serializer_class = PublisherSerializer
    pagination_class = CustomPagination

class PublisherRetrieveUpdateDestroy(generics.RetrieveUpdateDestroyAPIView):
    queryset = Publisher.objects.all()
    serializer_class = PublisherSerializer

class DonationCurrencyListCreate(generics.ListCreateAPIView):
    queryset = DonationCurrency.objects.all()
    serializer_class = DonationCurrencySerializer
    pagination_class = CustomPagination

class DonationCurrencyRetrieveUpdateDestroy(generics.RetrieveUpdateDestroyAPIView):
    queryset = DonationCurrency.objects.all()
    serializer_class = DonationCurrencySerializer

class CustomerListCreate(generics.ListCreateAPIView):
    queryset = Customer.objects.all()
    serializer_class = CustomerSerializer
    pagination_class = CustomPagination

class CustomerRetrieveUpdateDestroy(generics.RetrieveUpdateDestroyAPIView):
    queryset = Customer.objects.all()
    serializer_class = CustomerSerializer

class GenreListCreate(generics.ListCreateAPIView):
    queryset = Genre.objects.all()
    serializer_class = GenreSerializer
    pagination_class = CustomPagination

class GenreRetrieveUpdateDestroy(generics.RetrieveUpdateDestroyAPIView):
    queryset = Genre.objects.all()
    serializer_class = GenreSerializer

class GameListCreate(generics.ListCreateAPIView):
    queryset = Game.objects.all()
    serializer_class = GameSerializer
    pagination_class = CustomPagination

class GameRetrieveUpdateDestroy(generics.RetrieveUpdateDestroyAPIView):
    queryset = Game.objects.all()
    serializer_class = GameSerializer

class GamePurchaseListCreate(generics.ListCreateAPIView):
    queryset = GamePurchase.objects.all()
    serializer_class = GamePurchaseSerializer
    pagination_class = CustomPagination

class GamePurchaseRetrieveUpdateDestroy(generics.RetrieveUpdateDestroyAPIView):
    queryset = GamePurchase.objects.all()
    serializer_class = GamePurchaseSerializer

class VideoGameRentalListCreate(generics.ListCreateAPIView):
    queryset = VideoGameRental.objects.all()
    serializer_class = VideoGameRentalSerializer
    pagination_class = CustomPagination

class VideoGameRentalRetrieveUpdateDestroy(generics.RetrieveUpdateDestroyAPIView):
    queryset = VideoGameRental.objects.all()
    serializer_class = VideoGameRentalSerializer

class BidListCreate(generics.ListCreateAPIView):
    queryset = Bid.objects.all()
    serializer_class = BidSerializer
    pagination_class = CustomPagination

class BidRetrieveUpdateDestroy(generics.RetrieveUpdateDestroyAPIView):
    queryset = Bid.objects.all()
    serializer_class = BidSerializer

class AuctionListCreate(generics.ListCreateAPIView):
    queryset = Auction.objects.all()
    serializer_class = AuctionSerializer
    pagination_class = CustomPagination

class AuctionRetrieveUpdateDestroy(generics.RetrieveUpdateDestroyAPIView):
    queryset = Auction.objects.all()
    serializer_class = AuctionSerializer

class SoldGameCopyListCreate(generics.ListCreateAPIView):
    queryset = SoldGameCopy.objects.all()
    serializer_class = SoldGameCopySerializer
    pagination_class = CustomPagination

class SoldGameCopyRetrieveUpdateDestroy(generics.RetrieveUpdateDestroyAPIView):
    queryset = SoldGameCopy.objects.all()
    serializer_class = SoldGameCopySerializer

class AuctionWinnerListCreate(generics.ListCreateAPIView):
    queryset = AuctionWinner.objects.all()
    serializer_class = AuctionWinnerSerializer
    pagination_class = CustomPagination

class AuctionWinnerRetrieveUpdateDestroy(generics.RetrieveUpdateDestroyAPIView):
    queryset = AuctionWinner.objects.all()
    serializer_class = AuctionWinnerSerializer

class SaleListCreate(generics.ListCreateAPIView):
    queryset = Sale.objects.all()
    serializer_class = SaleSerializer
    pagination_class = CustomPagination

class SaleRetrieveUpdateDestroy(generics.RetrieveUpdateDestroyAPIView):
    queryset = Sale.objects.all()
    serializer_class = SaleSerializer

class PaymentListCreate(generics.ListCreateAPIView):
    queryset = Payment.objects.all()
    serializer_class = PaymentSerializer
    pagination_class = CustomPagination

class PaymentRetrieveUpdateDestroy(generics.RetrieveUpdateDestroyAPIView):
    queryset = Payment.objects.all()
    serializer_class = PaymentSerializer