from django.shortcuts import render
from rest_framework import viewsets, generics
from clubs.models import Club, Event
from clubs.serializers import ClubSerializer, EventSerializer


class ClubViewSet(viewsets.ModelViewSet):
    queryset = Club.objects.all()
    serializer_class = ClubSerializer
    http_method_names = ['get']


class EventViewSet(viewsets.ModelViewSet):
    queryset = Event.objects.all()
    serializer_class = EventSerializer
    http_method_names = ['get']