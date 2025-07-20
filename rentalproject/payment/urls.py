from django.urls import include, path
from . import views
from rest_framework.routers import DefaultRouter


urlpatterns = [
    path('create/', views.create, name="create-page")

]
router = DefaultRouter()
router.register("payment", views.PaymentViewSet)
urlpatterns += router.urls
