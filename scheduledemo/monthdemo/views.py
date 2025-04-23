from django.shortcuts import render
from django.http import HttpResponse, HttpResponseNotFound, HttpResponseRedirect
from django.urls import reverse

# Create your views here.
monthlydemo_schedule = {
    'january':'Learning HTML',
    'february':'Learning CSS',
    'march': 'Learning Javascript',
    'april':'Learning React',
    'may': 'Learing Python',
    'june':'Learning SQL',
    'july':'Learning Django',
    'august':'Learning Java',
    'september':'Learning RPA',
    'october':'Learing C++',
    'november':'Learning Mongodb',
    'december':'Learning node.js'
}

def monthdemo_schedule_number(request, monthdemo):
    monthdemolist = list(monthlydemo_schedule.keys())
    print(monthdemolist)
    
    if (monthdemo > len(monthdemolist)) :
        return HttpResponseNotFound('Invalid Month Number')
    
    redirectmonthdemo = monthdemolist[monthdemo-1] 
    print(redirectmonthdemo)
    
    redirect_month_path = reverse('monthdemo-url', args=[redirectmonthdemo])
    return HttpResponseRedirect(redirect_month_path)

# def week_schedule(request, monthdemo):
#     return HttpResponse(monthdemo_schedule[monthdemo])

def monthdemo_schedule(request, monthdemo):
    try:
        month_details_text = monthlydemo_schedule[monthdemo]
        return HttpResponse(month_details_text)
    except:
        return HttpResponseNotFound('This month is not valid')
        