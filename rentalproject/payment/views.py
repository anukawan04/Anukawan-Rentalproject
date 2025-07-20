from django.http import HttpResponse
from django.shortcuts import render
from rest_framework.response import Response
from .models import Payment
from .serializer import PaymentSerializer
from rest_framework import status
from rest_framework import viewsets
from rest_framework.permissions import AllowAny


# Create your views here.
def create(request):
    return HttpResponse("This is a create page")


class PaymentViewSet(viewsets.ModelViewSet):
    queryset = Payment.objects.all()
    serializer_class = PaymentSerializer
    Permission_classes = [AllowAny]

    def delete(self, request, *args, **kwargs):
        Payment.objects.all().delete()
        return Response(status=status.HTTP_204_No_CONTENT)
