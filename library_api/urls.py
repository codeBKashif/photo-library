from django.urls import path
from .views import PhotoView


urlpatterns = [
    path('photos/', PhotoView.as_view()),
    path('photos/<int:id>', PhotoView.as_view())
]