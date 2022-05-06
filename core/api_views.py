from time import time
from urllib import response
from django.shortcuts import render
from django.db.models import Q
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
from django.db.models import DurationField, F, ExpressionWrapper
import pytz

@api_view(('GET',))
@renderer_classes((JSONRenderer,))
def get_venues_visited(request):
    '''it catches the hku_id in the url as parameter, find out the venues that the member visited while infectuous and returns a list of the venue codes'''
    # Changing the GET schema: https://stackoverflow.com/questions/150505/capturing-url-parameters-in-request-get 
    hku_id = request.GET.get('hku_id', None)
    diagoseDateString = request.GET.get('diagnose_date', None) # format: 30-05-2022
    dt_format = "%Y-%m-%d"  # or suitable format
    diagnoseDate = datetime.strptime(diagoseDateString, dt_format).replace(tzinfo=pytz.UTC) # to
    days=timedelta(2)
    infectuous_date=diagnoseDate-days # from
    print(infectuous_date)
    visit_records_user = Record.objects.filter(member__hku_id=hku_id)
    print(visit_records_user)
    visit_records_in_range = visit_records_user.filter(dateTime__gte=datetime.combine(infectuous_date, time.min), dateTime__lte=datetime.combine(diagnoseDate, time.max))
    print(visit_records_in_range)
    venues = list(set([v.venue.venue_code for v in visit_records_in_range])) # find unique venue code (set operation)
    return Response(venues)

#this function should get the close contacts as defined by hku
@api_view(('GET',))
@renderer_classes((JSONRenderer,))
def get_close_contacts(request):
    # this function should get the close contacts as defined by hku
    hku_id = request.GET.get('hku_id', None)
    diagoseDateString = request.GET.get('diagnose_date', None) # format: 30-05-2022
    dt_format = "%Y-%m-%d"  # or suitable format
    diagnoseDate = datetime.strptime(diagoseDateString, dt_format).replace(tzinfo=pytz.UTC) # to
    days=timedelta(days=2)
    infectuous_date = diagnoseDate - days # need to make sure it is 00:00
    # time aware warning https://shanxiaoi.top/post/2021/06/22/_1407290762697248768/ 
    records_in_range = Record.objects.filter(dateTime__gte=datetime.combine(infectuous_date, time.min), dateTime__lte=datetime.combine(diagnoseDate, time.max))
    potentials_id = list(set([v.member.hku_id for v in records_in_range])) # find unique ids
    print("records:", records_in_range)
    print('potential_id', potentials_id)
    threshold = timedelta(minutes=30)
    result = []
    for id in potentials_id:
        enter_events = records_in_range.filter(member__hku_id=id, event='Entry')
        exit_events =  records_in_range.filter(member__hku_id=id, event='Exit')
        # To ensure the entry records match the exit record
        print("length check: ", len(enter_events), len(exit_events), 'Length Match:', len(enter_events)==len(exit_events)) 
        for i in range(min(len(enter_events), len(exit_events))): # to avoid index out of range
            duration = exit_events[i].dateTime - enter_events[i].dateTime # Check each pair of entry, leave event
            print(f"{id}: {duration}")
            if duration >= threshold:
               result.append(id)
               print(f"{id} confirmed")
               break
    return Response(result)

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

