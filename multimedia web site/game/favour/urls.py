from django.urls import path
from .views import image_list, upload_image, image_detail, delete_image

urlpatterns = [
    path('', image_list, name='image_list'),
    path('upload/', upload_image, name='upload_image'),
    path('<int:pk>/', image_detail, name='image_detail'),
    path('<int:pk>/delete/', delete_image, name='delete_image'),
]