from django.shortcuts import render
from django.http import HttpResponse
from django.contrib.auth.decorators import login_required
from . import forms
import re

# Create your views here.
@login_required(login_url='/register/login')
def comment(request):
    if request.method == 'POST':
        form = forms.createcomment(request.POST)
        if form.is_valid():
            a = request.POST.get('content')
            regex = re.compile('[^a-zA-Z]')
            e = regex.sub('', a)
            b = ['fuck','crap','shit','asshole','bitch','fucker']
            d = 0
            for c in b:
                if (e.find(c) != -1):
                    d = d+1
            if d==0:
                instance = form.save(commit=False)
                instance.author = request.user
                instance.save()
                return HttpResponse('comment is {}'.format(e))
            else:
                return HttpResponse('Do not use bad words')
    else:
        form = forms.createcomment()
    return render(request,'comment/create.html',{'form':form})
