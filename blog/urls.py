from django.urls import path
from . import views


app_name = 'blog'


urlpatterns = [
# post views
    path('', views.post_list, name='post_list'), #since i created function rather than a class in views.py, thus we will not use .get_view() here
    path('<int:year>/<int:month>/<int:day>/<slug:post>/',views.post_detail,name='post_detail'),
]