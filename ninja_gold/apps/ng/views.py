from django.shortcuts import render, redirect
import random
from datetime import datetime

def index(request):
    if 'gold' not in request.session:
        request.session['gold'] = 0
        request.session['activity'] = []
    else:
        request.session['gold'] += 1
    context = {
        "wallet": request.session['gold'],
        "activity": request.session['activity'],
    }
    return render(request,'ng/index.html', context)

def process(request):
    if request.method == "POST":
        if 'farm' in request.POST:
            farm_gold = random.randint(10,20)
            request.session['gold'] += farm_gold
            request.session['activity'].append('You earned ' + str(farm_gold) + ' gold from the ' + request.POST['farm'] + ' ' + '(' + str(datetime.now().strftime("%m-%d-%Y %H:%M.%S")) + ')')
        if 'cave' in request.POST:
            cave_gold = random.randint(5,10)
            request.session['gold'] += cave_gold
            request.session['activity'].append('You earned ' + str(cave_gold) + ' gold from the ' + request.POST['cave'] + ' ' + '(' + str(datetime.now().strftime("%m-%d-%Y %H:%M.%S")) + ')')
        if 'house' in request.POST:
            house_gold = random.randint(2,5)
            request.session['gold'] += house_gold
            request.session['activity'].append('You earned ' + str(house_gold) + ' gold from the ' + request.POST['house'] + ' ' + '(' + str(datetime.now().strftime("%m-%d-%Y %H:%M.%S")) + ')')
        if 'casino' in request.POST:
            casino_gold = random.randint(-50,50)
            request.session['gold'] += casino_gold
            if casino_gold >=0:
                request.session['activity'].append('You earned ' + str(casino_gold) + ' gold from the ' + request.POST['casino'] + ' ' + '(' + str(datetime.now().strftime("%m-%d-%Y %H:%M.%S")) + ')')
            else:
                request.session['activity'].append('You lost ' + str(casino_gold) + ' gold from the ' + request.POST['casino'] + ' ' + '(' + str(datetime.now().strftime("%m-%d-%Y %H:%M.%S")) + ')')
    return redirect('/')

def reset(request):
    request.session.clear()
    return redirect("/")