# from django.conf.urls import url
# from Employee import views

from django.urls import re_path,path
from Employee import views

from django.conf.urls.static import static
from django.conf import settings

urlpatterns=[
    re_path(r'^department$',views.departmentApi),
    re_path(r'^department/([0-9]+)$',views.departmentApi),

    re_path(r'^employee$',views.departmentApi),
    re_path(r'^employee/([0-9]+)$',views.departmentApi),

    re_path(r'^employee/savefile',views.SaveFile)
]+static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)