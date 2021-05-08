from django.shortcuts import render
from django.views import View
from django.conf import settings

from panel.utils import read_config

class HomeView(View):

    template_name = 'home.html'
    template_name_watson = 'home-Develop.html'

    def get(self, request):
        if read_config()['distro'] == settings.DEVELOP_DISTRO:
            return render(request, self.template_name_develop)
        else:
            return render(request, self.template_name)
