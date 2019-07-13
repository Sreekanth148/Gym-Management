"""vsu_project URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.1/topics/http/urls/
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
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path
from django.views.generic import TemplateView

from app import views
from vsu_project import settings

urlpatterns = [
    path('admin/', admin.site.urls),
    path('',TemplateView.as_view(template_name="Index.html")),
    path('register/',TemplateView.as_view(template_name="Register.html")),
    path('userlogin/', TemplateView.as_view(template_name="Login.html")),
    #path('user/',TemplateView.as_view(template_name="Register.html")),
    path('registerdetails/',views.RegisterDetails),
    path('logindetails/',views.LoginDetails),
    path('traineeDetails/',views.TraineeDetails),
    path('gymDetails/',views.gymDetails),
    path('show/',views.Show),
    path('show_gym/',views.Show_Gym),
    path('update/',views.UpdateUserProfile),
    path('userUpdate/',views.UserUpdateProfile),
    path('home/',views.Home),
    path('logout/',views.logout),
    path('feedback/',views.Feed_back),
    path('feedbackdetails/',views.FeedbackDetails),
    path('contact/',views.Contact),
    path('forgetdetails/',views.ForgetDetails),
    path('resetpassword/',views.ResetPassword),

    path('forgetpassword/',views.ForgetPassword),

]
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
