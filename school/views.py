from django.http import HttpResponse


def school_page(request):
    return HttpResponse('This is my school app')

