from django.contrib.auth.models import Group
from django.shortcuts import render
from django.http import Http404
from rest_framework import permissions, viewsets, generics, views, status
from rest_framework.response import Response

from users.models import CustomUser
from .models import Umugani
from .serializers import (UserSerializer,
                          GroupSerializer,
                          UmuganiCreateSerializer,
                          UmuganiSerializer,)


def ahabanza(request):
    imigani = Umugani.objects.all()
    context = {
        'imigani': imigani,
    }
    return render(request, "core/ahabanza.html", context)


# API Stuff

class UserViewSet(viewsets.ModelViewSet):
    """
    API endpoints that allows groups to be viewed or edited
    """
    queryset = CustomUser.objects.all().order_by('-date_joined')
    serializer_class = UserSerializer
    permission_classes = [permissions.IsAuthenticated]


class GroupViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows groups to be viewed or edited
    """
    queryset = Group.objects.all()
    serializer_class = GroupSerializer
    permission_classes = [permissions.IsAuthenticated]


# Stuff zijyanye n'imigani

class UmuganiCreateView(generics.CreateAPIView):
    """
    Ongeraho umugani mushyashya hano
    """
    serializer_class = UmuganiCreateSerializer


class UmuganiView(generics.RetrieveAPIView):
    queryset = Umugani.objects.all()

    def get(self, request, *args, **kwargs):
        queryset = self.get_queryset()
        serializer = UmuganiSerializer(queryset, many=True)
        return Response(serializer.data)


class UmuganiDetail(views.APIView):
    """ Gukurura, Guhindura, no gukoresha umugani """

    def get_object(self, pk):
        try:
            return Umugani.objects.get(pk=pk)
        except Umugani.DoesNotExist:
            raise Http404

    def get(self, request, pk):
        user = self.get_object(pk)
        serializer = UmuganiSerializer(user, data=request.data)
        if serializer.is_valid():
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_404_NOT_FOUND)

    def put(self, request, pk):
        user = self.get_object(pk)
        serializer = UmuganiSerializer(user, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk):
        umugani = self.get_object(pk)
        umugani.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
