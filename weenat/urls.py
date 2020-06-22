from django.contrib import admin
from django.urls import path, include
from rest_framework import routers

from app.views import UsersViewSet


router = routers.DefaultRouter()
# router = routers.DefaultRouter(trailing_slash=False)
router.register(r'users', UsersViewSet)

urlpatterns = [
    path('', include(router.urls)),
    path('users/<int:year>', UsersViewSet.as_view({'get': 'list'})),
    path('admin/', admin.site.urls),
]


