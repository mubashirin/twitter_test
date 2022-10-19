from itertools import tee
from django.urls import path
from twitter_pars.views import (
    index,
    lists_link,
    teen
)


urlpatterns = [
    path('', index, name='index'),
    path('links/', lists_link, name='list_links'),
    path('teen/<int:id_user>/', teen, name='teen'),
]
