"""PUCSD_LiveHealth URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.11/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf.urls import url
from django.contrib import admin
from studentMgt.views import *
urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^login/', renderlogin),
    url(r'^dashboard/', login),
    url(r'^logout/', logout_view),
    url(r'^add_entry_in_department/', add_entry_in_department ),
    url(r'^department_list_table/', department_list_table),
    url(r'^render_add_department/', render_add_department),
    url(r'^add_course/', add_course),
    url(r'^add_entry_in_course/', add_entry_in_course),
    url(r'^sessionValues/',sessionValues),
    url(r'^course_list/', course_list),
    url(r'^student_registration/',student_registration),
    #url(r'^addStudent/',addStudent),
    url(r'^teacher_registration/',teacher_registration),
    url(r'^addTeacher/',addTeacher),
]
