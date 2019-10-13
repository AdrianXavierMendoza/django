from django.shortcuts import render
from time import gmtime, strftime

def index(request):
    context = {
    	"date":strftime("%B %d, %Y", gmtime()),
        "time":strftime("%m-%d-%Y"+"    "+"%H:%M.%S %p", gmtime()),
    }
    return render(request, "td/index.html", context)