# 미디어
from django.conf import settings
from django.conf.urls.static import static

#URL Conf생성
from django.contrib import admin
from django.urls import include, path
from django.conf.urls import url, include
from rest_framework import routers
# 모델 추가시 이 곳에!
from project import views 	#이 부분 수정함

#
router = routers.DefaultRouter()
router.register(r'users', views.UsersViewSet)
router.register(r'storekeepers', views.StorekeepersViewSet)
router.register(r'reviews', views.ReviewsViewSet)
router.register(r'orderinfos', views.Order_infoViewSet)

urlpatterns = [
    path('project/', include('project.urls')),
    path('admin/', admin.site.urls),
    url(r'^', include(router.urls)),
    url(r'^api-auth/', include('rest_framework.urls', namespace='rest_framework'))
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)