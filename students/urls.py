from students.views import *
#from . import views
#from .views import home

from django.urls import path

app_name = 'students' # if we use namespace while include this app in main route then we should provide app_name


urlpatterns = [

    
    path('ali/', ali_hassan, name="ali_hassan"),
    path('waseem/', waseem, name="waseem"),
    path('sir-rashid/', rashid, name="rashid")

]


