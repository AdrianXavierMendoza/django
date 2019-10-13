from django.shortcuts import render, redirect
from django.utils.crypto import get_random_string

# Create your views here.
def index(request):
    if 'attempts' not in request.session:
        request.session['attempts'] = 0
    else:
        request.session['attempts'] += 1
    context = {
        'attempts':request.session['attempts'],
        'word':get_random_string(length=20),
    }

    return render(request, "wg/index.html", context)

def reset(request):
    request.session.clear()
    return redirect("/")