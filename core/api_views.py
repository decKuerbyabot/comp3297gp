from urllib import response
from django.shortcuts import render
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import viewsets
from .serializers import *
from rest_framework import status, viewsets
from .models import *
# Create your views here.
# this function gets the venues visited by the member

def get_venues_visited(request):
    
    pass


#this function should get the close contacts as defined by hku
def get_close_contacts(request):

    pass

class VenueViewSet(viewsets.ModelViewSet):
    queryset=Venue.objects.all()
    serializer_class=VenueSerializer

class RecordViewSet(viewsets.ModelViewSet):
    queryset=Record.objects.all()
    serializer_class=RecordSerialzer

class MemberViewSet(viewsets.ModelViewSet):
    queryset=HKUMember.objects.all()
    serializer_class=RecordSerialzer


# @api_view(['GET',])
# def all_records(request):
#     records=Record.objects.all()
#     record_serializer=RecordSerialzer(records, many=True)
#     return Response(record_serializer.data)

#this function inserts a visit record generated by devices into the Record database.
# @api_view(['POST'])
# def add_record(request):
#     serializer=RecordSerialzer(data=request.data)
#     if serializer.is_valid():
#         serializer.save()
#         return Response(serializer.data, statue=status.HTTP_201_CREATED)
#     return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

# @api_view(['POST',])
# def update_record(request):
#     # find venue code, uid match in the database whose leave_datetime is null
#     record=Record.objects.filter(
#         venue__id=request.data.venue_pk,
#         member__hku_id=request.data.hku_id,
#         leave_datetime=None
#     )

#     serializer=RecordSerialzer(record, data=request.data)
#     return Response(serializer.data)