from django.shortcuts import render
from twitter import *
import tempfile
from twitter_pars.services import (
    get_user_data,
    get_user_timeline
)


def index(request):
    template = 'list.html'
    return render(request, template_name=template)


def lists_link(request):
    data = []
    template = 'index.html'

    if request.method == 'POST':
        l = request.POST.get('text')
        tmp = tempfile.TemporaryFile()
        tmp.write(l.encode('utf-8'))
        tmp.seek(0)

        for line in tmp.readlines():
            data.append(get_user_data(line.decode('utf-8').split('/')[-1]))

    context = {
        'users': data,
    }
    return render(request, template_name=template, context=context)


def teen(request, id_user):
    template = 'teen_post.html'
    context = {
        'posts': get_user_timeline(user_id=id_user)[:10]
    }
    return render(request, template_name=template, context=context)
