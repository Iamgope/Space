from django.urls import path
from . import views

urlpatterns = [
    path('', views.getSpaces, name='getSpaces'),
    path('category/owned/', views.Myspace, name='owned_spaces'),
    path('<slug:slug>/', views.spaces, name="A_Space"),
    path('create/space/', views.CreateSpace, name="create"),
    path('<slug:slug>/singlePost/<int:pk>/',
         views.SinglePost, name="singlePost"),
    path('<slug:slug>/Edit/',views.EditSpace,name="EditSpace"),
    path('join/today/',views.Search_Space,name="Join_Space")
    # path('create/post/',)
]
