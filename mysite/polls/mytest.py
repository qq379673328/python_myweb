#! /usr/bin/env python
#coding=utf-8
from polls.models import Poll, Choice;
from django.utils import timezone;

p = Poll(question='你的名字是什么？', pub_date=timezone.now())
print p
