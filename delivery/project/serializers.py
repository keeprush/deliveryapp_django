from rest_framework import serializers
from .models import Users,Storekeepers,Reviews,Order_info
from drf_extra_fields.fields import Base64ImageField
from django.core.files.base import ContentFile
# 이곳에 시리얼라이저
class UsersSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Users
        fields = ('kakao_id','nickname','steamed','location','location_gps','created_at','update_at')


class StorekeepersSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Storekeepers
        fields = ('kakao_id','nickname','location','location_gps','store_notice','store_img','store_name','star','review_count','order_count','Steamed_count','category_type','operation_time','no_operation_time','phone_number','possible_delivery','delivery_fee','recommend','main','side')
class ReviewsSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Reviews
        fields = ('store_name','nickname', 'comment','star','created_at','custom_img')

class Order_infoSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Order_info
        fields = ('id','store_name', 'user','rider_name','selected_food','order_price','delivery_fee','price_all','order_now','order_time')
