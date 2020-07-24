from django.shortcuts import render, redirect, get_list_or_404
from .models import Miniurl
from .forms import MiniurlForm
#from .utils import get_random_alphnum


def miniurl_home(request):
    template = 'miniurl_home.html'

    if request.method == 'POST':
        miniurl_form = MiniurlForm(data=request.POST)
        if miniurl_form.is_valid():
            new_miniurl = miniurl_form.save(commit=True)
            new_miniurl.save()
    else:
        miniurl_form = MiniurlForm()

    miniurls = Miniurl.objects.order_by('-created_on')[:10]
    print(miniurls)
    return render(request, template, {'miniurls': miniurls, 'miniurl_form': miniurl_form})

def get_url(request, short):
    miniurl = Miniurl.objects.get(short_url=short)
    if miniurl is None or not miniurl:
        print("Nothing to retrieve")

    print("miniurl: ", miniurl)
    return redirect(miniurl.original_url)

