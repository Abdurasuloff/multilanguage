from django.urls import path
from .views import index, CreateNew



urlpatterns = (
      path('', index, name='home'),
      path('new/', CreateNew.as_view(), name='new'),
)