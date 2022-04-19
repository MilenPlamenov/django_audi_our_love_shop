from django.contrib.auth import get_user_model, login
from django.shortcuts import redirect
from django.views.generic import CreateView

from audi_our_love_shop_project.shop_authentication.forms import RegisterUsers

ShopUser = get_user_model()


class CreateAccount(CreateView):
    model = ShopUser
    form_class = RegisterUsers
    template_name = 'authentication/create_account.html'
    success_url = '/'

    def form_valid(self, form):
        user = form.save(commit=False)
        user.save()
        login(self.request, user)
        return redirect('index')
