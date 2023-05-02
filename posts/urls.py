from django.urls import path

from posts.views import *


urlpatterns = [
    path('thought', ThoughtList.as_view()),
    path('thought/<pk>/', ThoughtDetail.as_view()),
    path('reply', ReplyList.as_view()),
    path('reply/<pk>/', ReplyDetail.as_view()),



]
