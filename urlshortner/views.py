from django.shortcuts import render, get_object_or_404
from django.http import HttpResponseRedirect, HttpResponse
from django.urls import reverse
from .models import Url
from django import forms

# Create your views here.
def index(request):
    return render(request, 'urlshortner/index.html')

def redirect(request, short_url):
    try :
        url = Url.objects.get(short_url = short_url)
        main_url = url.main_url
    except :
        return HttpResponse("url does not exist")
    else :
        context = {'main_url': main_url}
        return render(request, 'urlshortner/redirect.html', context)

def results(request, url_id):
    url = get_object_or_404(Url, pk = url_id)
    context = {
        'main_url': url.main_url,
        'short_url': url.short_url
    }
    return render(request, 'urlshortner/results.html', context)

def add(request):
    main_url = request.POST['main_url']
    f=forms.URLField()
    try:
        f.clean(main_url)
    except:
        message = f'Invalid URL'
        context = { 'message': message }
        return render(request, 'urlshortner/index.html', context)
    else:
        new_url = Url(main_url=main_url)
        new_url.save()
        return HttpResponseRedirect(reverse('urlshortner:results', args=(new_url.id, )))
