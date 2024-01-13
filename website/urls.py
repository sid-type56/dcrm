from django.urls import path , include
from . import views
from .views import MyModelListAPIView
from .views import show_records_of_interest ,add_interests
urlpatterns = [
    path('',views.home,name='home'),
    # path('login/',views.login.user,name='login'),
    path('logout/',views.logout_user,name='logout'),
    path('register/',views.register_user,name='register'),
    path('api/my-model/', MyModelListAPIView.as_view(), name='my-model-list'),
    path('api/my-interests/',views.show_records_of_interest,name='interests'),
    path('api/add-interests/',views.add_interests,name='add_interests')
]