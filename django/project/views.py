from django.http import HttpResponse, JsonResponse



def hello(request):
    return HttpResponse("Hello World")

def first(request):
    return HttpResponse("<h1>my first web page<h1>")

def sec(request):
    return HttpResponse("<h1>my second web page<h1>")

def parameter(request, *args, **kwargs):
    print kwargs
    return HttpResponse("<h1>the id entered in the url is "+str(kwargs['id'])+"</h1>")

def json_res(request, *args, **kwargs):
    print kwargs
    return JsonResponse(kwargs)