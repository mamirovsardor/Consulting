from django.urls import path
from . import views


app_name="basic_app"

urlpatterns = [
    path('',views.Index.as_view(),name="index"),
    # path('blog/<int:id>/',views.Blog2.as_view(),name="blog2"),
    # path('blog/',views.Blog2.as_view(),name="blog2"),
 
    path('blog/<int:id>/',views.Blog, name="blog"),
    path('blog/',views.Blog, name="blog"),
    

]