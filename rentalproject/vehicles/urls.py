from django.urls import include, path
from . import views
from rest_framework.routers import DefaultRouter


urlpatterns = [
    path('create/', views.create, name="create-page")

]
router = DefaultRouter()
router.register("vechicles", views.VechiclesViewSet)
urlpatterns += router.urls
