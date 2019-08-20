"""main URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.2/topics/http/urls/
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

from django.conf.urls import url, include
from django.urls import path
from rest_framework import routers

from .views.enterprise import EnterpriseViewSet
from .views.company import CompanyViewSet
from .views.city import CityViewSet
from .views.category import CategoryViewSet
from .views.product import ProductViewSet
from .views.price import PriceViewSet
from .views.district import DistrictViewSet

router = routers.DefaultRouter()
router.register(r'enterprise',  EnterpriseViewSet)
router.register(r'organizations', CompanyViewSet)
router.register(r'city', CityViewSet)
router.register(r'category', CategoryViewSet)
router.register(r'product', ProductViewSet)
router.register(r'price', PriceViewSet)
router.register(r'distirict', DistrictViewSet)

urlpatterns = [
    path('', include(router.urls))

]

