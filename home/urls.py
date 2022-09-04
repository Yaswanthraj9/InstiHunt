from django.urls import path
from . import views

urlpatterns = [
    path('', views.home_page,name='home_page'),
    path('engineering/college_list/', views.engineering_college_list,name='engineering_college_list'),
    path('design/college_list/', views.design_college_list,name='design_college_list'),
    path('law/college_list/', views.law_college_list,name='law_college_list'),
    path('medical/college_list/', views.medical_college_list,name='medical_college_list'),
    path('mba/college_list/', views.mba_college_list,name='mba_college_list'),
    path('science/college_list/', views.science_college_list,name='science_college_list'),
    path('analytics_page/',views.analytics_page,name="analytics_page"),
    path('engineering/',views.engineering,name="engineering"),
    path('design/',views.design,name="design"),
    path('law/',views.law,name="law"),
    path('medical/',views.medical,name="medical"),
    path('mba/',views.mba,name="mba"),
    path('science/',views.science,name="science"),
]



