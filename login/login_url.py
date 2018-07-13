from django.urls import re_path
from login.views import login, logout

urlpatterns = [
    re_path(r'logout/', logout),
    re_path(r'login/', login)
]