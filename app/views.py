from django.contrib import messages
from django.contrib.auth import logout, login, authenticate
from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth.views import LoginView
from django.db.models import Q
from django.shortcuts import render, redirect
from django.urls import reverse_lazy
from django.views.generic import ListView, FormView, TemplateView, CreateView
from rest_framework import viewsets, permissions, status, generics
from rest_framework.authentication import SessionAuthentication
from rest_framework.decorators import api_view
from rest_framework.pagination import PageNumberPagination
from rest_framework.permissions import IsAuthenticated, AllowAny
from rest_framework.response import Response
from rest_framework.views import APIView

from .forms import *
from .models import App, Category, Comment
from .serializers import UserSerializer, AppSerializer, UserLoginSerializer, RegisterSerializer, AppCategorySerializer
from .utils import DataMixin


class Index(DataMixin, TemplateView):
    template_name = 'index.html'

    def get_context_data(self, **kwargs):
        return self.get_user_context(title="main page")


class ProfileView(DataMixin, TemplateView):
    template_name = "profile.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        mixin = self.get_user_context(title="register")
        return dict(list(context.items()) + list(mixin.items()))


class AppIndex(DataMixin, ListView):
    paginate_by = 3
    model = App
    template_name = 'app/index.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        mixin = self.get_user_context(title="apps page")
        return dict(list(context.items()) + list(mixin.items()))

    def get_queryset(self):
        query = self.request.GET.get("app_name")
        object_list = App.objects.all()
        if query:
            self.paginate_by = 10
            object_list = App.objects.filter(Q(name__icontains=query) | Q(name__icontains=query))

        return object_list


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


def handler404(request, exception):
    return render(request, '404page.html', status=404)


def handler500(exception):
    return ("<h1>eror 500 </h1>")


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


class TopAppsView(DataMixin, TemplateView):
    template_name = "app/top_apps.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["top_apps"] = Rating.objects.select_related("app").order_by("-star")
        mixin = self.get_user_context(title="register")
        return dict(list(context.items()) + list(mixin.items()))

    # def get(self, request, *args, **kwargs):


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


class Pagination(PageNumberPagination):
    page_size = 3
    page_size_query_param = 'page_size'
    max_page_size = 10000


class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer
    pagination_class = Pagination


class AppViewSet(viewsets.ModelViewSet):
    permission_classes = (permissions.AllowAny,)
    queryset = App.objects.all()
    serializer_class = AppSerializer


class AppCategoryViewSet(viewsets.ModelViewSet):
    permission_classes = (permissions.AllowAny,)
    queryset = Category.objects.all()
    serializer_class = AppCategorySerializer


class UserLogin(APIView):
    permission_classes = (permissions.AllowAny,)
    authentication_classes = (SessionAuthentication,)

    ##
    def post(self, request):
        data = request.data
        serializer = UserLoginSerializer(data=data)
        if serializer.is_valid(raise_exception=True):
            user = serializer.check_user(data)
            authUser = User.objects.filter(username=data.get("username")).values()
            login(request, user)
            return Response(authUser[0], status=status.HTTP_200_OK)


class UserLogout(APIView):
    permission_classes = (permissions.AllowAny,)
    authentication_classes = ()

    def post(self, request):
        logout(request)
        return Response(status=status.HTTP_200_OK)


class UserView(APIView):
    permission_classes = (permissions.IsAuthenticated,)
    authentication_classes = (SessionAuthentication,)

    ##
    def get(self, request):
        serializer = UserSerializer(request.user)
        return Response({'user': serializer.data}, status=status.HTTP_200_OK)


class RegisterViewAPI(generics.CreateAPIView):
    queryset = User.objects.all()
    permission_classes = (AllowAny,)
    serializer_class = RegisterSerializer


@api_view(["POST"])
# @permission_classes([IsAuthenticated])
def APILogout(request):
    print(request.user)
    logout(request)
    return Response({"message": "User successfully Logged out"})
