from django.contrib import messages
from django.contrib.auth import logout
from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth.views import LoginView
from django.core.paginator import Paginator
from django.shortcuts import render, redirect
from django.urls import reverse_lazy
from django.views.generic import ListView, FormView, TemplateView, DetailView, CreateView

from . import models
from .forms import *
from .models import App, Category
from .utils import DataMixin


class Index(DataMixin, TemplateView):
    template_name = 'index.html'

    def get_context_data(self, **kwargs):
        return self.get_user_context(title="main page")


# def appIndex(request):
#     appList = models.App.objects.all()
#     paginator = Paginator(appList, 3)
#     page_num = request.GET.get('page')
#     appList = paginator.get_page(page_num)
#     return render(request, 'app/index.html', {'object_list': appList})


class AppIndex(DataMixin, ListView):
    paginate_by = 3
    model = App
    template_name = 'app/index.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        mixin = self.get_user_context(title="apps page")
        return dict(list(context.items()) + list(mixin.items()))


def AppShow(request, slug):
    app = models.App.objects.get(url=slug)
    if request.method == "POST":
        curUser = request.user.pk
        message = request.POST.get("comment", None)
        star = request.POST.get("star", None)
        title = request.POST.get("title", None)

    return render(request, 'app/show.html', {"app": app})


def categoryView(request, url):
    cat = Category.objects.get(url=url)
    context = {"cats": Category.objects.all(), "object": cat}

    return render(request, "app/category.html", context)


# def handler404(request, exception):
#     return render(request, '404page.html', status=404)
#
#
# def handler500(exception):
#     return render(template_name='404page.html', status=500)

# class AppShow(DetailView):
#     model = models.App
#     slug_field = "url"
#     template_name = "app/show.html"

class ContactView(DataMixin, FormView):
    success_url = 'app_index'
    template_name = 'app/contact.html'
    form_class = ContactForm

    def get_context_data(self, **kwargs):
        return self.get_user_context(title="contact page")

    def form_valid(self, form):
        messages.add_message(self.request, messages.SUCCESS, 'success!')
        return redirect('app_index')


class RegisterView(DataMixin, CreateView):
    form_class = UserRegisterForm
    template_name = "register.html"
    success_url = reverse_lazy('login')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        mixin = self.get_user_context(title="register")
        return dict(list(context.items()) + list(mixin.items()))


class Login(DataMixin, LoginView):
    form_class = AuthenticationForm
    template_name = "login.html"
    success_url = reverse_lazy('home')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        mixin = self.get_user_context(title="register")
        return dict(list(context.items()) + list(mixin.items()))


@login_required
def logout_form(request):
    logout(request)
    return redirect("login")
