from django.shortcuts import render
from django.http import HttpResponse
from .models import PlayStore

# Create your views here.


def storeHome(request):
    allPlayStoreAppLinks = PlayStore.objects.all()
    context = {"allPlayStoreAppLinks": allPlayStoreAppLinks}
    return render(request, "store/store.html", context)


def storeApp(request, slug):
    appInfo = PlayStore.objects.filter(slug=slug).first()

    if appInfo == None:
        return render(request, '404NotFound.html')

    appInfo.views = appInfo.views + 1
    appInfo.save()

    context = {"appInfo": appInfo}
    return render(request, 'store/storeApp.html', context)
