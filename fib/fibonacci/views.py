from django.http import JsonResponse, HttpResponseBadRequest
from django.shortcuts import render
from fibonacci.fib_gen import fibonacci
from models import FibonacciParameters
import time


def fibonacci_view(request):
    start_time = time.time()
    n = request.GET.get('name', '')

    try:
        n = int(n)
    except ValueError:
        return HttpResponseBadRequest("Only integer values are allowed for query parameter 'name'!")

    if n < 0:
        return HttpResponseBadRequest("Negative integers are not allowed")
    if n > 100000:
        return HttpResponseBadRequest("Request timeout ")
    res = fibonacci(n)
    j = time.time() - start_time
    l = []
    l.append([res,j])

    fp = FibonacciParameters(type_id=1,exec_time=j,input_parameter=n,result=res)
    fp.save()


    return JsonResponse(l, safe=False)

def results_view(request):
    res = FibonacciParameters.objects.all()

    l = []
    for r in res:
        l.append([r.id,r.type_id,r.exec_time,r.input_parameter,r.result])

    return JsonResponse(l,safe=False)

def delete_view(request):
    id = request.GET.get('id','')
    try:
        fp = FibonacciParameters.objects.get(id=id)
        fp.delete()
        l = "gone"
    except:
        l = "already gone"


    return JsonResponse(l, safe=False)


