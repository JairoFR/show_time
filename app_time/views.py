from django.shortcuts import render, redirect
from time import gmtime, strftime

# Create your views here.
def index(request):
    return redirect('show_time/')

def show_time(request):
    context = {
        'date': strftime("%a, %d %b %Y", gmtime()),
        'time': strftime("%H:%M %p", gmtime())
    }
    return render(request, 'show_time.html', context)