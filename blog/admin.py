from django.contrib import admin
from .models import BlogCategories, Blog, Author ,PassportInfo


admin.site.register([Blog, BlogCategories, Author,PassportInfo])
