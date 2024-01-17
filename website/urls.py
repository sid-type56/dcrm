from django.urls import path , include
from . import views
from .views import *
from django.conf import settings
from django.conf.urls.static import static
urlpatterns = [
    path('',views.home,name='home'),
    # path('login/',views.login.user,name='login'),
    path('logout/',views.logout_user,name='logout'),
    path('register/',views.register_user,name='register'),
    path('api/my-interests/',views.show_records_of_interest,name='interests'),
    path('api/add-interests/',views.add_interests,name='add_interests'),
    path('api/add-images/',views.image_upload,name='image_upload'),
    path('api/tell-time/',views.tell_time,name='tell_time'),
    path('api/show-image/',views.show_image,name='show_image'),
]+static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)