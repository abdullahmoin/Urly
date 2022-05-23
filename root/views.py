from django.shortcuts import render, redirect
from root.models import Url


# Create your views here.

def home(request):
    if request.method == "POST":
        full_url = request.POST.get('full_url')
        obj = Url.create(full_url)
        context = {
            'full_url': obj.full_url,
            'short_url': request.get_host() + '/' + obj.short_url
        }
        return render(request, "root/index.html", context)

    return render(request, "root/index.html")


def routeToUrl(request, key):
    try:
        obj = Url.objects.get(short_url=key)
        return redirect(obj.full_url)
    except:
        return redirect(home)
    if obj:
        pass
    return redirect(home)
