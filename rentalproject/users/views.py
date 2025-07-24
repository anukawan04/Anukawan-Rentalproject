from django.http import HttpResponse
from django.shortcuts import render
from rest_framework import generics
from rest_framework.response import Response
from .models import Users
from .serializer import UserSerializer
from rest_framework import status
from rest_framework import viewsets
from .permission import IsAdminOrReadOnly


# Create your views here.
def create(request):
    return HttpResponse("This is a create page")


class UserViewSet(viewsets.ModelViewSet):
    queryset = Users.objects.all()
    serializer_class = UserSerializer
    Permission_classes = [IsAdminOrReadOnly]

    def delete(self, request, *args, **kwargs):
        Users.objects.all().delete()
        return Response(status=status.HTTP_204_No_CONTENT)


# class UsersCreateList(generics.ListCreateAPIView):
#     queryset = Users.objects.all();
#     serializer_class =UserSerializer;

    # def delete(self,request,*args, **kwargs):
    #     Users.objects.all().delete()
    #     return Response(status = status.HTTP_204_No_CONTENT)

# class UserUpdateDelete(generics.RetrieveUpdateDestroyAPIView):
#     queryset = Users.objects.all();
#     serializer_class =UserSerializer;
#     lookup_field = "pk"
