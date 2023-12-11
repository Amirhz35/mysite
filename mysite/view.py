
from django.http import HttpResponse,JsonResponse
def http_test(requests):
    return HttpResponse('<h1>hello</h1>')
    
def json_test(requests):
    return JsonResponse({'hi':{'hello':'ali'}})