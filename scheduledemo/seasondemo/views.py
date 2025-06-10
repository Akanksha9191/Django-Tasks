from django.shortcuts import render
from django.http import HttpResponse, HttpResponseNotFound, HttpResponseRedirect
from django.urls import reverse

# Create your views here.
seasondemo_schedule ={
    'summer': 'Visit to Wet n Joy Waterpark',
    'monsoon':'Visit to nature place',
    'winter':'Visit to manali'
}

# def season_schedule(request, seasondemo):
#     season_details_text = seasondemo_schedule[seasondemo]
#     return HttpResponse(season_details_text)

def season_schedule_number(request, seasondemo):
    seasondemolist = list(seasondemo_schedule.keys())
    print(seasondemolist)
    
    if(seasondemo > len(seasondemo)):
        return HttpResponseNotFound('This is invalid number')
    
    redirectseasondemo = seasondemolist[seasondemo-1]
    print(redirectseasondemo)
    
    redirect_path_season = reverse('seasondemo-url', args=[redirectseasondemo])
    return HttpResponseRedirect(redirect_path_season)

def season_schedule(request, seasondemo):
    # try:
        season_details_text = seasondemo_schedule[seasondemo]
        print(season_details_text)
        return render(request, 'season/seasondetail.html', {
            'seasondemo':seasondemo,
            'seasondetail':season_details_text
        })
    # except:
        return HttpResponseNotFound('This season is not valid')