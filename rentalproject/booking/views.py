from django.http import HttpResponse
from django.shortcuts import render
from rest_framework.response import Response
from .models import Booking
from .serializer import BookingSerializer
from rest_framework import status
from rest_framework import viewsets
from rest_framework.permissions import AllowAny


# Create your views here.
def create(request):
    return HttpResponse("This is a create page")


class BookingViewSet(viewsets.ModelViewSet):
    queryset = Booking.objects.all()
    serializer_class = BookingSerializer
    Permission_classes = [AllowAny]

    def delete(self, request, *args, **kwargs):
        Booking.objects.all().delete()
        return Response(status=status.HTTP_204_No_CONTENT)
