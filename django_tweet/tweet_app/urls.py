from django.urls import path
from . import views
app_name='tweetapp'
urlpatterns = [
    path('addtweet/', views.addtweet,name="addtweet"),
    path('', views.listtweet,name="listtweet"),
    path('logout/', views.custom_logout, name='logout'),
    path('signup/',views.SignUpView.as_view(), name="signup"),
    path('deletetweet/<int:id>',views.delete,name="deletetweet")
    # path('addtweetbyform/',views.addtweetbyform,name="addtweetbyform"),
]
