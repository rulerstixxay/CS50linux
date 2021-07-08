from django.shortcuts import render
import datetime

# Create your views here.
def index(request):
    now = datetime.datetime.now()
    return render(request, "phs/index.html", {
        "newyear": now.month == 1 and now.day == 1,
        "xmas": now.month == 12 and now.day == 25,
        "cny": now.month == 2 and (now.day == 12 or now.day == 13),
        "gfriday": now.month == 4 and now.day == 2,
        "lbour": now.month == 5 and now.day == 1 
    })