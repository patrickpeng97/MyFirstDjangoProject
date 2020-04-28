from django.shortcuts import render
from django.http import HttpResponse
from first_app.models import Topic, WebPage, AccessRecord


# Create your views here.


def index(request):
    web_pages_list = AccessRecord.objects.order_by("date")
    date_dict = {"access_records": web_pages_list}
    return render(request, "first_app/index.html", context=date_dict)


def helps(request):
    context_dict = {
        "links": "you can click this link to get help: <br></br> <a href='https://www.google.com'>google</a>"
    }
    return render(request, "first_app/helps.html", context=context_dict)
