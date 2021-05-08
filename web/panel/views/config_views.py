import subprocess

from django.views.generic import FormView
from django.contrib import messages
from django.utils.translation import ugettext_lazy as _
from django.conf import settings

from panel.forms.config_form import BaseConfigForm, StandardConfigForm, DevelopConfigForm
from panel.utils import read_config

class ConfigView(FormView):
    template_name = 'settings.html'
    success_url = 'settings'
    form_class = BaseConfigForm

    def get_context_data(self, **kwargs):
        context = super(ConfigView, self).get_context_data(**kwargs)

        if read_config()['distro'] == settings.DEVELOP_DISTRO:
            context['showUpgrade'] = False # test True
        else:
            context['showUpgrade'] = False

        return context

    def __init__(self, *args, **kwargs):
        super(ConfigView, self).__init__(*args, **kwargs)

        if read_config()['distro'] == settings.DEVELOP_DISTRO:
            self.form_class = DevelopConfigForm
        else:
            self.form_class = StandardConfigForm

    def form_valid(self, form):
        form.write_config()
        messages.success(self.request, _('Saved successfully'))

        # Restart
        if 'save-and-restart' in form.data:
            subprocess.Popen(['sudo', 'reboot'])

        return super(ConfigView, self).form_valid(form)

    def get_initial(self):
        return self.form_class.read_config()
