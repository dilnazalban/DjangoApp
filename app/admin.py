from django.contrib import admin
from .models import Category, App, AppImage, Rating, MyUser

# Register your models here.


admin.site.register(Category)
admin.site.register(App)
admin.site.register(Rating)
