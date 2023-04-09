from django.contrib import messages
from django.contrib.auth import logout
from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth.views import LoginView
from django.shortcuts import render, redirect
from django.urls import reverse_lazy
from django.views.generic import ListView, FormView, TemplateView, CreateView

from .forms import *
from .models import App, Category, Comment
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
    app = App.objects.get(url=slug)
    if request.method == "POST":
        currentUser = request.user
        star = request.POST.get("star", None)
        comment = request.POST.get("comment", None)
        if star:
            ratingUser = None
            if app.rating_set.count() > 0:
                ratingUser = Rating.objects.get(author=currentUser.pk, app=app.pk)
            if not ratingUser and int(star):
                rat = Rating()
                rat.app = app
                rat.star = int(star)
                rat.author = currentUser
                rat.save()
            elif ratingUser and int(star):
                rat = Rating.objects.get(author=currentUser, app=app)
                rat.star = int(star)
                rat.save()
        if comment:
            com = Comment()
            com.app = app
            com.user = currentUser
            com.message = comment
            com.save()

    ratings = app.rating_set.all()
    if ratings.count() > 0:
        summa = 0
        for rating in ratings:
            summa += rating.star
        ratingV = summa / ratings.count()
        a = [{"isStar": True} if ratingV > x else {"isStar": False} for x in range(0, 10)]
    else:
        a = None
    comments = Comment.objects.select_related("user").filter(app=app.pk)
    return render(request, 'app/show.html', {"app": app, "rating": a, "comments": comments})


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
