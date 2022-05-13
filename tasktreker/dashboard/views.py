from django.shortcuts import render
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views import View
#from django.views.generic import TemplateView

# Create your views here.
# dashboard view using the TemplateView
#class DashboardView(LoginRequiredMixin, TemplateView):
    #template_name = 'dashboard/dashboard.html'

# dashboard view using the vanilla view
class DashboardView(LoginRequiredMixin, View):
    def get(self, request, *args, **kwargs):
        # codes = CodeModel.objects.all()
        # context = {'codes' = codes}
        return render(request, 'dashboard/dashboard.html')

    #def get_queryset(self):
        #pass
