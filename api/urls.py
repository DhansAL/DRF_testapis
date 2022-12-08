from .views import ItemList,ItemDetail,LocationList,LocationDetail
from django.urls import path


urlpatterns = [
 path("items/",ItemList.as_view()),   
 path("item/<int:pk>/",ItemDetail.as_view()),   
 path("location/",LocationList.as_view()),   
 path("location/<int:pk>/",LocationDetail.as_view()),   
  ]
