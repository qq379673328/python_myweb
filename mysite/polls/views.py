#! /usr/bin/env python
#coding=utf-8
# Create your views here.

from django.http import HttpResponse, Http404
# from django.template import RequestContext, loader
from django.shortcuts import render, get_object_or_404

from polls.models import Poll

#主页
def index(request):
    latest_poll_list = Poll.objects.order_by('-pub_date')[:5]
    #output = ' '.join([p.question for p in latest_poll_list])
    #template = loader.get_template('polls/index.html')
    # context = RequestContext(request,{
    #     'latest_poll_list': latest_poll_list,
    # })
    context = {
        'latest_poll_list' : latest_poll_list
    }
    #return HttpResponse(template.render(context))
    return render(request, 'polls/index.html', context)

#详细页
def detail(request, poll_id):
    # try:
    #     poll = Poll.objects.get(pk=poll_id)
    # except Poll.DoesNotExixt:
    #     raise Http404
    poll = get_object_or_404(Poll, pk=poll_id)
    return render(request, 'polls/detail.html', {'poll':poll})

#投票结果页
def results(request, poll_id):
    return HttpResponse("Results vote %s ." % poll_id)

#投票页
def vote(request, poll_id):
    return HttpResponse("Vote %s ." % poll_id)