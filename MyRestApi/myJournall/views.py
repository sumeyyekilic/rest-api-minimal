from django.shortcuts import render
from django.http import JsonResponse
from .models import bulletJournal

from rest_framework.decorators import api_view
from rest_framework.response import Response
from .serializers import JournallSerializer

@api_view(['GET'])
def apiView(request):
    api_journal_url={
        'Detail View':'/task-detail/<str:pk>/'
    }

    return Response(api_journal_url)



@api_view(['GET'])
def journalTaskDetail(request, pk):
	journalTask = bulletJournal.objects.get(id=pk)
	serializer = bulletJournal(journalTask, many=False)
	return Response(serializer.data)
