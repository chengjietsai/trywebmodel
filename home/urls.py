from django.urls import path
from . import views
urlpatterns = [
    path('',views.index),
    path('transfermypic/',views.transfermypic),
    path('delmypic/',views.transfermypic,name='uplaodfile')
]
