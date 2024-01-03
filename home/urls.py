from django.urls import path
from django.conf import settings
from django.conf.urls.static import static
from .views import Index, TemplateView

urlpatterns = [
    path('', Index.as_view(), name='home'),
   
]