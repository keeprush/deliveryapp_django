from django.shortcuts import render

#
from rest_framework import viewsets
from .serializers import UsersSerializer, StorekeepersSerializer,ReviewsSerializer,Order_infoSerializer
from .models import Users,Storekeepers,Reviews,Order_info


#

# Create your views here.
from django.http import HttpResponse


def index(request):
    return HttpResponse("Hello, world. You're at the polls index.")
# 이곳에 뷰 셋
class UsersViewSet(viewsets.ModelViewSet):
    queryset = Users.objects.all()
    serializer_class = UsersSerializer

class StorekeepersViewSet(viewsets.ModelViewSet):
    queryset = Storekeepers.objects.all()
    serializer_class = StorekeepersSerializer

class ReviewsViewSet(viewsets.ModelViewSet):
    queryset = Reviews.objects.all()
    serializer_class = ReviewsSerializer

class Order_infoViewSet(viewsets.ModelViewSet):
    queryset = Order_info.objects.all()
    serializer_class = Order_infoSerializer
