
from django.urls import path

from . import views

urlpatterns = [

    path('cakes/',views.CakeListCreateView.as_view()),

    path('cake/<int:id>/',views.CakeRetrieveUpdateDeleteView.as_view()),

    path('category/',views.CategoryListCreateView.as_view()),

    path('category/<int:id>/',views.CategoryRetrieveUpdateDeleteView.as_view()),

    path('shape/',views.ShapeListCreateView.as_view()),

    path('shape/<int:id>/',views.ShapeRetrieveUpdateDeleteView.as_view()),

    path('weight/',views.WeightListCreateView.as_view()),

    path('weight/<int:id>/',views.WeightRetrieveUpdateDeleteView.as_view()),
    
    

]
