
from django.contrib import admin
from django.urls import path
from main.views import home
from scripts.views import *
urlpatterns = [
    path('admin/', admin.site.urls),
    path('',home,name='home'),
    path('organize-files',organize_files,name='organize-files'),
    path('organize-files-api',organize_api,name='organize-api'),
    path('bulk_renaming',renaming_api,name='renaming-api'),
    path('diff-tool',diff_api,name='diff-api'),
    path('resize-tool',image_resize_api,name='resize-api'),
    path('find-all',crawler_all_links,name='find-all'),
    path('find-all-api',crawler_all_links_api,name='find-all-api'),
]
