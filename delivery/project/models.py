from django.db import models
from datetime import datetime
# python manage.py runserver 192.168.219.195:8000
# Create your models here.
class Users(models.Model):          # 사용자
    kakao_id = models.CharField(default = 1, null=True,max_length=30) # 아이디
    nickname = models.CharField(primary_key=True, default=1,max_length=20) # 닉네임1
    steamed = models.TextField(null=True)  # 찜한 상품 목록(가게 아이디 값 저장)
    location = models.TextField(null=True) # 주소명(위치 주소)   
    location_gps = models.TextField(null=True) # gps 
    # order_history = models.TextField(null=True) # 주문한 가게 목록(가게 아이디 값 저장)
    # order_list = models.TextField(null=True) # 장바구니(그 가게의 물건 번호 저장)
    # ArrayField(models.CharField(max_length=200), blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    update_at = models.DateTimeField(auto_now = True)

class Storekeepers(models.Model):    # 점주
    kakao_id = models.CharField(blank=True, null=True, max_length=30) # 아이디
    nickname = models.CharField(blank=True, null=True, max_length=20) # 닉네임2
    location = models.TextField(blank=True, null=True) # 주소명(위치 주소)
    location_gps = models.TextField(blank=True, null=True) # gps
    #정보 - 공지사항
    store_notice = models.TextField(blank=True, null=True)

    # Store_info
    store_img = models.TextField(blank=True, null=True)
    store_name = models.CharField(default = 1, primary_key=True,max_length=30)
    star = models.FloatField(blank=True, null=True, default=0) # 주문이 완료 될 경우 별점 더해서 나누기 작업하기
    review_count = models.IntegerField(blank=True, null=True, default=0)
    # 아래꺼는 정보에서 사용
    order_count = models.IntegerField(blank=True, null=True, default=0)
    Steamed_count = models.IntegerField(blank=True, null=True, default=0)
    category_type = models.CharField(null=True, blank=True,max_length=16)

    # 음식점정보
    operation_time = models.CharField(max_length=50)
    no_operation_time = models.CharField(max_length=50)
    phone_number = models.CharField(max_length=20)
    possible_delivery = models.CharField(blank=True, null=True, max_length=50)

    # 배달팁
    delivery_fee = models.IntegerField(blank=True, null=True)

    # 메뉴 목록
    recommend = models.TextField(blank=True, null=True)
    main = models.TextField(blank=True, null=True)
    side = models.TextField(blank=True, null=True)

class Reviews(models.Model):    # 리뷰

    store_name = models.CharField(null=True, max_length=50)
    nickname = models.CharField(null=True, max_length=20)
    comment = models.TextField(null=True)
    star = models.IntegerField(null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    custom_img = models.ImageField(blank=True, upload_to="images", null=True)

# 주문내역
class Order_info(models.Model):
    # 주문한 내역들도 변수 만들기
    id = models.AutoField(primary_key=True)
    store_name = models.CharField(default = 1,max_length=30)
    user = models.CharField(null=True,max_length=20)
    rider_name = models.TextField(null=True,blank=True)
    selected_food = models.TextField(blank=True, null=True)
    order_price = models.TextField(blank=True, null=True)
    delivery_fee = models.TextField(blank=True, null=True)
    price_all = models.TextField(blank=True, null=True)
    order_now = models.TextField(blank=True, null=True, max_length=10) # 주문 상황 ( 주문완료, 배달중, 배달완료)
    order_time = models.DateTimeField(default=datetime.now)

#fields = ('store_name', 'user','selected_food','order_price','delivery_fee','price_all','rider_name')
# 클래스 배달 현황 만들기(유저아이디, 점주 아이디)
