from django.urls import path, re_path
from . import views
from .views import DetailList, CreateWebpage, ListV, Base, Cap, Update, DeleteV
from .models import Webpage
app_name = 'myapp'

urlpatterns = [
    path('create/', CreateWebpage.as_view(), name='cwp'),
    path('list/', ListV.as_view(), name='list'),
    path('myapp/cap/', Cap.as_view(), name='cap'),
    path('myapp/base/', Base.as_view(), name='base'),
    path('detail/<pk>', DetailList.as_view(), name='detail'),
    path('delete/<pk>', DeleteV.as_view(), name='delete'),
    path('update/<pk>', Update.as_view(), name='update'),
    #path(r'^(?P<wepdetail_id>\d+)/share/$', views.wepdetail_share,
    # name='wepdetail_share'),
]
