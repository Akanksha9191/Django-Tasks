from django.shortcuts import render
from django.http import HttpResponse, HttpResponseNotFound, HttpResponseRedirect
from django.urls import reverse
# Create your views here.
weekdemo_schedule ={
    'monday':'This ia Monday',
    'tuesday':'This is Tuesday',
    'wednesday': 'This is Wednseday',
    'thursday':'This is Thursday',
    'friday':'This is friday',
    'saturday': 'This is Saturday',
    'sunday':'This is Sunday'
}

# def week_schedule(request, weekdemo):
#     return HttpResponse(weekdemo_schedule[weekdemo])

def weekdemo_schedule_number(request, weekdemo):
    weekdemolist = list(weekdemo_schedule.keys())
    print(weekdemolist)
    
    if(weekdemo > len(weekdemolist)):
        return HttpResponseNotFound('This number is invalid')
    
    redirectweekdemo = weekdemolist[weekdemo - 1]
    print(redirectweekdemo)
    
    redirect_weekdemo_path = reverse('weekdemo-url', args=[redirectweekdemo])
    return HttpResponseRedirect(redirect_weekdemo_path)

def week_schedule(request, weekdemo):
    try:
        weekdemo_detail_text = weekdemo_schedule[weekdemo]
        print(weekdemo)
        print(weekdemo_detail_text)
        return render(request, 'week/week_detail.html', {
            'weekdemo': weekdemo,
            'weekdetail':weekdemo_detail_text
            
        })
    except:
        return HttpResponseNotFound('This week is not valid')