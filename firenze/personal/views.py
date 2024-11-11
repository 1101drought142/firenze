from django.views.generic import TemplateView

class FavouritesView(TemplateView):
    template_name = "favourites.html"

class AccountView(TemplateView):
    template_name = "account.html"

class OrdersView(TemplateView):
    template_name = "orders.html"
    
class LoginView(TemplateView):
    template_name = "login.html"

class SignUpView(TemplateView):
    template_name = "sign_up.html"