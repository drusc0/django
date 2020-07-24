from django.shortcuts import render, redirect
from .models import Miniurl
#from .utils import get_random_alphnum

def get_url(request, short):
    miniurl = Miniurl.objects.get(short_url=short)
    if miniurl is None or not miniurl:
        print("Nothing to retrieve")

    print("miniurl: ", miniurl)
    return redirect(miniurl.original_url)

