"""
URL configuration for rentalproject project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.2/topics/http/urls/
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
from django.contrib import admin
from django.urls import path, include
from payment import urls as payment_urls
from users import urls as users_urls
from vehicles import urls as vehicles_urls
from booking import urls as booking_urls
from orders import urls as orders_urls

from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
)


import rentalproject.my_admin  # Only keep if used for admin customization

urlpatterns = [
    path('admin/', admin.site.urls),
    path('payment/', include(payment_urls)),
    path('users/', include(users_urls)),
    path('vehicles/', include(vehicles_urls)),
    path('booking/', include(booking_urls)),
    path('orders/', include(orders_urls)),
    path('api/token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('api/token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
]
