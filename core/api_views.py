from time import time
from urllib import response
from django.shortcuts import render
from rest_framework.decorators import api_view, renderer_classes
from rest_framework.response import Response
from rest_framework import viewsets
from .serializers import *
from datetime import datetime, timedelta, time
from rest_framework import status, viewsets
from .models import *
# Create your views here.
# this function gets the venues visited by the member
from rest_framework.renderers import JSONRenderer, TemplateHTMLRenderer

@api_view(('GET',))
@renderer_classes((JSONRenderer,))
def get_venues_visited(request, hku_id):
    '''it catches the hku_id in the url as parameter, find out the venues that the member visited while infectuous and returns a list of the venue codes'''
    member=HKUMember.objects.get(hku_id=hku_id)
    diagnoseDate=member.diagnoseDate
    days=timedelta(2)
    days_=timedelta(14)
    # date the member first became infectuous
    infectuous_date=diagnoseDate-days
    # date the member become safe
    safe_date=diagnoseDate+days_
    visit_records=Record.objects.filter(member__hku_id=member.hku_id, enter_datetime__lte=datetime.combine(safe_date, time.max), enter_datetime__gte=datetime.combine(infectuous_date, time.min))
    # get the list of venue codes
    venues=[visit_record.venue.venue_code for visit_record in visit_records]
    return Response(venues)

#this function should get the close contacts as defined by hku
def get_close_contacts(request, hku_id):

    pass

class VenueViewSet(viewsets.ModelViewSet):
    # lookup_field='venue_code'
    queryset=Venue.objects.all()
    serializer_class=VenueSerializer


class RecordViewSet(viewsets.ModelViewSet):
    queryset=Record.objects.all()
    serializer_class=RecordSerialzer

class MemberViewSet(viewsets.ModelViewSet):
    queryset=HKUMember.objects.all()
    serializer_class=HKUmemberSerializer

