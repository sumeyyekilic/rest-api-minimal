from django.shortcuts import render
from django.http import JsonResponse
from .models import bulletJournal

from rest_framework.decorators import api_view
from rest_framework.response import Response
from .serializers import JournallSerializer

@api_view(['GET'])
def apiView(request):
    api_journal_url={
        'List':'/journalTask-list/',
        'Detail View':'/journalTask-detail/<str:pk>/',
        'Create':'/journalTask-create/',
		'Update':'/journalTask-update/<str:pk>/',
		'Delete':'/journalTask-delete/<str:pk>/',
    }

    return Response(api_journal_url)



@api_view(['GET'])
def journalTaskDetail(request, pk):
	journalTask = bulletJournal.objects.get(id=pk)
	serializer = JournallSerializer(journalTask, many=False)
	return Response(serializer.data)


@api_view(['GET'])
def journalTaskList(request):
	journalTask = bulletJournal.objects.all().order_by('-id')
	serializer = JournallSerializer(journalTask, many=True)
	return Response(serializer.data)


