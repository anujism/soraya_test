from django.urls import reverse_lazy

# Create your views here.
from django.views.generic.edit import CreateView
from django.views.generic.list import ListView
from django.views.generic import TemplateView

from plots.models import Algo
from plots.utils import algo_result

import requests


class AlgoCreateView(CreateView):
    model = Algo
    fields = '__all__'
    success_url = reverse_lazy('list')


class AlgoListView(ListView):
    model = Algo
    fields = '__all__'


class AlgoPlotView(TemplateView):
    template_name = 'plots/algo_plot.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['data'] = self.data(self.kwargs['id'])
        return context

    def data(self, id):
        # get algo info from db
        # TODO: handle exception if id does not exist
        algo = Algo.objects.get(id=id)
        # call iex api
        # prices = [1.2, 3,2, 4.3, 3.3, 5.3, 1.2, 3, 3.7, 3.2, 4.4]
        response = requests.get('https://api.iextrading.com/1.0/stock/{}/chart/1y'.format(algo.ticker))
        prices = [x.get('close') for x in response.json()]
        # call function
        # TODO: Assumption that function will always works
        positions, pnl = algo_result(algo.signal, algo.trade, prices)
        x_data = [i for i in range(1, len(positions) + 1)]
        return x_data, positions, pnl