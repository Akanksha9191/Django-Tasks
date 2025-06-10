from django.shortcuts import render
from django.http import HttpResponse, HttpResponseNotFound, HttpResponseRedirect

# Create your views here.
monthly_schedule = {
    'january':'Learning HTML',
    'february':'Learning CSS',
    'march': 'Learning Javascript',
    'april':'Learning Python',
    'may': 'Learing Django'
}  



# def month_schedule(request, month):  #january
#     # print(month)    #cmd
#     return HttpResponse(monthly_schedule[month])    #january

# ------path converted
# def month_schedule_number(request, month):    #month =1
#     return HttpResponse(month) # =1

# ----path convetred to month

def month_schedule_number(request, month):   #1
    monthlist = list(monthly_schedule.keys())  #[]
    print(monthlist)
    # length 5
    
    if (month > len(monthlist)):   #false above 5
        return HttpResponseNotFound('Invalid Month number ')
    
    redirectmonth = monthlist[month-1]   #[1]
    print(redirectmonth)
    return HttpResponseRedirect('/month/' + redirectmonth)   #8000/months/janaury


def month_schedule(request, month):    #january
    try:
        details_text = monthly_schedule[month]  #monthly_schedule['jan']
        return HttpResponse(details_text)
    except:
        return HttpResponseNotFound('This month is not supported')
