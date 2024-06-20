from django.contrib import admin
from django.urls import path
from Dashboard.views import *
from MemberList.views import *
from AddUser.views import *

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', Dashboard, name="Dashboard"),
    path('mem/', mem_view, name="mem"),
    path('addusr/', Add, name = "addusr"),
]
