from django.conf.urls import url
from plots.views import AlgoCreateView, AlgoListView, AlgoPlotView

urlpatterns = [
    url(r'^$', view=AlgoListView.as_view(), name='list'),
    url(r'^create/$', view=AlgoCreateView.as_view(), name='create'),
    url(r'^plot/(?P<id>[0-9]+)/$', view=AlgoPlotView.as_view(), name='plot'),
]