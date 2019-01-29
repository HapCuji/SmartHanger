"""
Definition of urls for polls viewing and voting.
"""

from django.conf.urls import url
from gateway.models import Poll

import gateway.views

urlpatterns = [
    url(r'^$',
        gateway.views.PollListView.as_view(
            queryset=Poll.objects.order_by('-pub_date')[:5],
            context_object_name='latest_poll_list',
            template_name='gateway/index.html',),
        name='home'),
    url(r'^(?P<pk>\d+)/$',
        gateway.views.PollDetailView.as_view(
            template_name='gateway/details.html'),
        name='detail'),
    url(r'^(?P<pk>\d+)/results/$',
        gateway.views.PollResultsView.as_view(
            template_name='gateway/results.html'),
        name='results'),
    url(r'^(?P<poll_id>\d+)/vote/$', gateway.views.vote, name='vote'),
]
