from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.

def view_all_polls(request):
    return HttpResponse('polls')

def create_poll(request):
    return HttpResponse("create")

def view_poll_by_id(request,id):
    return HttpResponse('view poll' +str(id))

def vote_poll(request,id):
    return HttpResponse('view poll 1' +str(id))

def update_poll(request,id):
    return HttpResponse('view poll up' +str(id))

def delete_poll(request,id):
    return HttpResponse('view poll delete' +str(id))