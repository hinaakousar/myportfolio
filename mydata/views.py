from django.shortcuts import HttpResponse

def first_view(request):
    return HttpResponse("My first View")

