from django.shortcuts import render, HttpResponse
from time import gmtime, strftime
# import datetime

# Create your views here.
def index(request):
    context = {
        "time": strftime("%Y-%m-%d %H:%M %p", gmtime())
        # "time": datetime.datetime.now().strftime("%I:%M%p on %B %d, %Y")
    }
    return render(request, 'index.html', context)

def time_display(request):
    return HttpResponse(index(request))