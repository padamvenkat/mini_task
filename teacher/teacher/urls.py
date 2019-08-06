"""teacher URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path,include
from information.rest_services import api_best_student_maths
from information.rest_services import api_hrc,api_lrc,api_avg,api_more90,api_less40,api_above40

urlpatterns = [
    path('admin/', admin.site.urls),
    path('ven/',view=api_best_student_maths),
    path('venky/',view=api_hrc),
    path('tej/',view=api_lrc),
    path('ch/',view=api_avg),
    path('cha/',view=api_more90),
    path('hello/',view=api_less40),
    path('sing/',view=api_above40)
    
]
