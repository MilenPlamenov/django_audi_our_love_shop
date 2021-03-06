from django.contrib.auth import get_user_model, login
from django.contrib.auth.views import LoginView
from django.shortcuts import redirect
from django.views.generic import CreateView, DetailView

from audi_our_love_shop_project.shop.models import Order
from audi_our_love_shop_project.shop_authentication.forms import RegisterUsers, LoginForm

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


class LoginAccount(LoginView):
    template_name = 'authentication/login_user.html'
    form_class = LoginForm


class AccountDetailsView(DetailView):
    model = ShopUser
    template_name = 'authentication/account-details.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['orders'] = Order.objects.filter(user=self.request.user)
        return context
