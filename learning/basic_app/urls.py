from django.urls import path
from . import views


## template tagging


app_name = 'basic_app'


urlpatterns = [
   path(r'relative/',views.relative,name='relative'),
   path(r'other/',views.other,name='other'),
]
