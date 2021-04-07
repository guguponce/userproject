from django.conf.urls import url
from users import views

app_name = 'users'

urlpatterns = [
    url(r'^$', views.users, name='users'),

    # url(r'^forms/',views.formulario, name='forms')


]
