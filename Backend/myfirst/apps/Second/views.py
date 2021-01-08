from django.http import HttpResponse


def info(request):
    return HttpResponse("Ало")
