from django.http import Http404
from django.shortcuts import render, redirect
from django.views.decorators.http import require_http_methods, require_GET

from .forms import MiniurlForm
from .models import Miniurl


# from .utils import get_random_alphnum

@require_http_methods(["GET", "POST"])
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

    return render(request, template, {'miniurls': miniurls, 'miniurl_form': miniurl_form})


@require_GET
def get_url(request, short):
    try:
        miniurl = Miniurl.objects.get(short_url=short)
        print(miniurl)
        return redirect(miniurl.original_url)
    except Miniurl.DoesNotExist:
        raise Http404("Miniurl object: {} does not exist".format(short))
