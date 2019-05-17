from django.contrib.auth.forms import (
    PasswordChangeForm,
    UserCreationForm,
)
from django.contrib.auth.views import (
    PasswordChangeView,
    PasswordChangeDoneView,
)
from django.urls import reverse_lazy
from django.views.generic import CreateView


class Register(CreateView):
    template_name = 'accounts/register.html'
    form_class = UserCreationForm
    success_url = reverse_lazy('blog:post_list')


class PasswordChange(PasswordChangeView):
    form_class = PasswordChangeForm
    success_url = reverse_lazy('accounts:password_change_done')
    template_name = 'accounts/password_change.html'


class PasswordChangeDone(PasswordChangeDoneView):
    template_name = 'accounts/password_change_done.html'
